from lxml import etree
import re
import html
import requests
import unicodecsv
import csv
import sys
import codecs
import io

fullfile = [['mfid', 'incident_year', 'computer_id', 'incident_district', 'incident_vdc', 'incident_ward', 'incident_toll', 'origin_district', 'origin_vdc', 'origin_ward', 'origin_toll']]

for person_id in range(0, 10802):
    current_record = []

    # Requesting the data looping over several person IDs
    url = "http://www.insec.org.np/victim/candidate_details_user.php?MFID=" + str(person_id)
    response = requests.request("GET", url)
    
    response.encoding = "UTF-8"
    responsestring = response.text
    print(person_id)
    if len(responsestring)>20000:
        
        # MFID:
        current_record.append(str(person_id))

        # Incident Year:
        search_pattern = re.compile(r'(&#2360;&#2366;&#2354;:\s)<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            current_record.append(wanteddata.strip())
        else: current_record.append('NA')

        # Computer ID:
        search_pattern = re.compile(r'(&#2325;&#2350;&#2381;&#2346;&#2381;&#2351;&#2369;&#2335;&#2352; &#2309;\. &#2344;&#2306;\.\n                      )<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            current_record.append(wanteddata.strip())
        else: current_record.append('NA')

        # District of Incidence:
        search_pattern = re.compile(r'(&#2328;&#2335;&#2344;&#2366; &#2349;&#2319;&#2325;&#2379; &#2332;&#2367;&#2354;&#2381;&#2354;&#2366;:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            if "&#" not in wanteddata:
                current_record.append(wanteddata.strip())
            else:    
                current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Incidet VDC:
        search_pattern = re.compile(r'(<td width="214">&#2327;&#2366;&#2357;&#2367;&#2360;:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            if "&#" not in wanteddata:
                current_record.append(wanteddata.strip())
            else:    
                current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Incident Ward:
        search_pattern = re.compile(r'(<td width="135">&#2357;&#2366;&#2352;&#2381;&#2337; &#2344;&#2306;\.:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Incidet Toll:
        search_pattern = re.compile(r'(<td>&#2335;&#2379;&#2354;&#2325;&#2379; &#2344;&#2366;&#2350;:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            if "&#" not in wanteddata:
                current_record.append(wanteddata.strip())
            else:    
                current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Origin District:
        search_pattern = re.compile(r'(<td width="191"><strong>&nbsp;</strong>&#2332;&#2367;&#2354;&#2381;&#2354;&#2366;:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            if "&#" not in wanteddata:
                current_record.append(wanteddata.strip())
            else:
                current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Origin VDC:
        search_pattern = re.compile(r'(<td colspan="2">&#2327;&#2366;&#2357;&#2367;&#2360;:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            if "&#" not in wanteddata:
                current_record.append(wanteddata.strip())
            else:    
                current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Origin Ward:
        search_pattern = re.compile(r'(<td>&#2357;&#2366;&#2352;&#2381;&#2337; &#2344;&#2306;\.:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        # Origin Toll:
        search_pattern = re.compile(r'(<td colspan="2">&#2335;&#2379;&#2354;:)\s<i>(.+)</i>')
        founddata = search_pattern.search(responsestring)
        if founddata != None:
            wanteddata = founddata.groups()[1]
            if "&#" not in wanteddata:
                current_record.append(wanteddata.strip())
            else:    
                current_record.append(html.unescape(wanteddata.strip()))
        else: current_record.append('NA')

        fullfile.append(current_record)

 
for line in fullfile:
    stringline = ';'.join(line)
    print(stringline)

##encodedfile = []
##for line in fullfile:
##     encodedline = [x.encode('UTF8') for x in line]
##     encodedfile.append(encodedline)
##print(encodedfile)
##
##with codecs.open('nepali_data.csv', 'a') as myfile:
##    wr = csv.writer(myfile)
##    for line in fullfile:
##        stringline = ','.join(line)
##        wr.writerow(stringline)
##
##with io.open('nepali_data.csv', 'w', encoding='iso-8859-1') as myfile:
##    for line in fullfile:
##        stringline = ','.join(line)
##        myfile.write(stringline)
##
##with open('nepali_data.csv', 'wb') as myfile:
##    wr = unicodecsv.writer(myfile, encoding='cp1252')
##    wr.writerows(fullfile)


