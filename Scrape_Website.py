# This program pulls data for the ships ariving at Swan Island
# from the Columbia River Pilots website

import requests
from bs4 import BeautifulSoup

# headers required to avoid 403 error
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
page = requests.get("https://colrip.com/dispatch-info/dispatch-status/", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')  #formats data into list

swan_island_port_list = ['301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', 'DD6', 'TMPOR']
list = []    #List of all lists boat_list
for tr in soup.find_all('tr'):  #for each table row
    tds = tr.find_all('td')     #store the data from the row as tds
    for port in swan_island_port_list:  #for each port in list
        if (port == tds[1].text or port == tds[2].text):   #if the port in data row matches swan island port then create list for that boat
            boat_list = []
            for i in range(len(tds)):  #for each item in list, create list with text only
                boat_list.append(tds[i].text)
            list.append(boat_list) #append list for a boat onto the list for all boats that port in swan island

print(list)

