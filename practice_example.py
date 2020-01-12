##### The following codes aim at web-scraping the information of all faculty members from Booth School of Business at The University of Chicago. ######


### We need to install two external packages: requests and BeautifulSoup
import time
import requests
import random
from bs4 import BeautifulSoup


###
headers = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}, \
           {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}, \
           {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}, \
           {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}, \
           {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}, \
           {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}, \
           {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}, \
           {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}, \
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}, \
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}, \
           {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'}, \
           {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

## First, we need to find the website link by hand.
url = 'https://www.chicagobooth.edu/faculty/directory'

## The following codes help us get the html source of the above URL.
htmlorg = requests.get(url, headers=headers[random.randint(0, len(headers) - 1)], timeout=50).text
bs = BeautifulSoup(htmlorg, 'html.parser')
faculty_list = bs.find_all('div', {'class': 'twelve columns faculty-listing'})

for ele in faculty_list:
    name = ele.find('a').text.replace(' ', '').replace('\r\n', ' ').strip()
    link = 'https://www.chicagobooth.edu' + ele.find('a').attrs['href']
    htmlorg = requests.get(link, headers=headers[random.randint(0, len(headers) - 1)], timeout=50).text
    img = BeautifulSoup(htmlorg, 'html.parser').find('div', {'class': 'faculty-bio-container'}).find('img').attrs['src']
    try:
        title = ele.find('div', {'class': 'nine columns faculty-listing-title'}).text.split(' of')[0].strip()
    except:
        title = ''
    try:
        department = ele.find('div', {'class': 'nine columns faculty-listing-title'}).text.split(' of')[1].strip()
    except:
        department = ''
    print(name, ';', link, ';', title, ';', department, ';', img)

    ## We may wait for 3 seconds between two adjacent loops. Space out each request so the server isn’t overwhelmed.
    time.sleep(3)



