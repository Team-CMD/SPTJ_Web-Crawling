import re , csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

def WriteCsv(filename,the_list):
    f = open(filename,'w',newline='')
    a = csv.writer(f,delimiter=',')
    a.writerows(the_list)
    f.close()

def search_URL():
    source = requests.get("http://www.hannam.ac.kr/guide/guide_0200.html")
    soup = bs(source.content, "html.parser")

    search_url = soup.find(class_ = 'borad_frame').find_all('iframe')
    for i in search_url:
        url = i.attrs['src']

    html = ur.urlopen(url).read()
    tt = bs(html, 'html.parser')

    a = tt.findAll('input')
    Plus = []
    for i in a:
        name = i.get('name')
        value = i.get('value')
        Plus.append([name,value])
    
    url += '&' + Plus[1][0] + '=' + Plus[1][1] + '&' + Plus[4][0] + '='
    url_list = []

    for i in range(1,4):
        notice_url = url + str(i)
        url_list.append(notice_url)

    return url_list

def univ_notice3(url_list):
    board_list = [["게시글","날짜"]]
    for url in url_list:
        title_list = []
        date_list = []

        html = ur.urlopen(url).read()
        soup = bs(html, 'html.parser')

        title = soup.findAll('a')
        date = soup.findAll('td')

        for x in title:
            txt = x.text
            if(len(txt) > 6):
                title_list.append(txt)
            
        for y in date:
            day = y.text
            if(len(day) == 10):
                date_list.append(day)
        
        for i in range(len(title_list)):
            board_list.append([title_list[i],date_list[i]])

    WriteCsv("Post3.csv",board_list)

url_list = search_URL()
univ_notice3(url_list)