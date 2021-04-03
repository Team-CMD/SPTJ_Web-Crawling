import re #텍스트 수정(탭, 개행, 공백)
import requests
from bs4 import BeautifulSoup
import pandas as pd
source =requests.get("http://uniboard.hannam.ac.kr/servlet/controller.helpdesk.UniboardServlet?seq=MQ==")
soup = BeautifulSoup(source.content, "html.parser")

def UNU_noice():
    # source =requests.get("http://uniboard.hannam.ac.kr/servlet/controller.helpdesk.UniboardServlet?seq=MQ==")
    # soup = BeautifulSoup(source.content, "html.parser")

    tr_data = soup.find(class_='tb_brdTmp').find_all('tr') #table class= 'tb_brdTmp' / tr에 있는 내용 가져오기
    del tr_data[0] #처음 부분 삭제(불필요한 부분 삭제)

    tr_data_len = len(tr_data)

    row_list = [] #행
    column_list = [] #열
    # thead_list = ["게시글 번호","제목","날자","작성자","조회수"]
    thead_list = ["제목","날자"] 

    for i in range(0, tr_data_len):
        td_data = tr_data[i].find_all('td')
        
        td_data_len = len(td_data)
        for j in range(0, td_data_len): #td 가져오기
            element = td_data[j].text.strip()
            
            # element = re.sub('&nbsp; | &nbsp;|\n|\t|\r|  ' , '', td_data[j].text.strip()) #stripe() #빈공간 정리
            column_list.append(element)
            
            
            # print(j, ' - ', td_data[j])
        del column_list[0:2] #열의 불필요한 부분 제거
        del column_list[2] ##열의 불필요한 부분 제거
        row_list.append([column_list[1], column_list[2]]) #열에 있는 내용을 행에 넣기
        column_list = []
        
    result = pd.DataFrame(row_list,columns=thead_list)
    result.to_csv('Notice.csv', encoding= 'UTF-8-sig')

# def notice_page():
#     p = soup.find_all('input')
#     page = []
#     for i in p:
#         name = i.get('name')
#         value = i.get('value')
#         page.append([name, value])

#     url += '&' + page[1][0] + '=' + page[1][1] + '&' + page[4][0] + '='
#     url_list = []

#     for i in range(1,4):
#         notice_url = url + str(i)
#         url_list.append(notice_url)

#     return url_list


if __name__ == "__main__":
    UNU_noice()
