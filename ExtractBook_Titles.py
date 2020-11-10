import re, requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import csv

p = {'http': 'http://A-4767:TRVMibs%40105@webproxy.ibsplc.com:80','https': 'https://A-4767:TRVMibs%40105@webproxy.ibsplc.com:80'}

total_list = []

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = 'https://www.nextgenerationautomation.com/automation-library'
page = requests.get(url, proxies=p, verify=False)
soup = BeautifulSoup(page.text, 'lxml')

for section, fframe in zip(soup.select('h5.font_5 > span'),[x.get('data-src') for x in soup.find_all('iframe', attrs={'name': 'htmlComp-iframe'})]):
    ipage=requests.get(fframe, proxies=p, verify=False)
    ipage_soup = BeautifulSoup(ipage.text, 'lxml')

    for ibook in [x.get('src') for x in ipage_soup.find_all('iframe')]:
        ibook_page=requests.get('http:'+ibook, proxies=p, verify=False)
        ibook_soup = BeautifulSoup(ibook_page.text, 'lxml')
        total_list.append([section.text,ibook_soup.find('a',id='titlehref').text])
        
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    for item_property_list in total_list:
        writer.writerow(item_property_list)