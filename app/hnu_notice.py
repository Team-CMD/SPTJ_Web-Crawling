import re , csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

def search_URL(url, N):
    html = ur.urlopen(url).read()
    soup = bs(html, "html.parser")

    search_url = soup.find_all('div',{"class":"borad_frame"})
    for x in search_url:
        url = x.find_all('iframe')[0].get('src')

    url += "&p_pageno="
    
    url_list = []
    for i in range(1,N+1):
        notice_url = url + str(i)
        url_list.append(notice_url)

    return url_list

def UNU_noice(url_list):
    row_list = []
    
    for url in url_list:
        source = requests.get(url)
        soup = bs(source.content, "html.parser")

        tr_data = soup.find(class_='tb_brdTmp').find_all('tr') #table class= 'tb_brdTmp' / tr에 있는 내용 가져오기

        del tr_data[0] #처음 부분 삭제(불필요한 부분 삭제)

        tr_data_len = len(tr_data)
        # column_list = [] #열

        for i in range(0, tr_data_len):
            column_list = [] #초기화
            if tr_data[i].get('class'): # 고정된 게시물 o
                fix = False
            else:                       # 고정된 게시물 x 
                fix = True
            td_data = tr_data[i].find_all('td')
            td_data_len = len(td_data)
            for j in range(0, td_data_len): #td 가져오기
                element = td_data[j].text.strip()
                column_list.append(element)
            del column_list[0:2] #열의 불필요한 부분 제거
            del column_list[2] ##열의 불필요한 부분 제거
            row_list.append([fix,column_list[1], column_list[2]]) #열에 있는 내용을 행에 넣기
            

    return row_list

if __name__ == "__main__":
    notice = "http://www.hannam.ac.kr/community/community_0104.html"  # -> 공지
    scholar = "http://janghak.hannam.ac.kr/sub4/menu_1.html"           # -> 장학
    univ = "http://www.hannam.ac.kr/guide/guide_0200.html"          # -> 학사

    notice_list = search_URL(notice,1)
    scholar_list = search_URL(scholar,4)
    univ_list = search_URL(univ,3)

    notice_result = UNU_noice(notice_list)
    scholar_result = UNU_noice(scholar_list)
    univ_result = UNU_noice(univ_list )

    # 결과값 확인하고 지우면 됩니다.
    print("\n--------------------공지사항--------------------\n")
    for i in range(len(notice_result)):
        print(i+1,notice_result[i])
    print("\n--------------------장학공지--------------------\n")
    for i in range(len(scholar_result)):
        print(i+1,scholar_result[i])
    print("\n--------------------학사공지--------------------\n")
    for i in range(len(univ_result)):
        print(i+1,univ_result[i])