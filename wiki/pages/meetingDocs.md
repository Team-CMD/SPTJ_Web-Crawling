<h1 align='center'>Web_Crawling Team - Meeting Docs</h1>

## ▶ 3.7. Meeting
    Date : 2021. 03. 07.
    participants : CMD_Web-Crawling Team(3)
    🧨 어떤 주제(내용)을 크롤링할 것인지 🧨
         - 학교 공지사항 / (학교 관련 정보 크롤링) (1순위)
         - 백준 문제 크롤링 (2순위)
         - 공모전 관련 크롤링 (사이트 선별 해서 하나로 정리) 
         - 기간 (3순위)

        1. 크롤링 할 때 필요한 기능 공부기간 : 현재부터 ~ 15일 (14일 중간 회의) 

        <----- 1차 회의 내용 ----->

        1. 크롤링할 주제(내용) : 장학공지 / 학사공지 / 공지사항
        >>> 최종결과물은 웹페이지 형식으로

        2. 크롤링 관련 공부 및 자료 수집 : 21.03.07 ~ 21.03.15
        >>> 중간 회의 : 21.03.14 

## ▶ 3.14. Meeting
    Date : 2021. 03. 14.
    participants : CMD_Web-Crawling Team(3)
    Date : 2021. 03. 14.
    프로젝트 목표 : 주기적으로 크롤링이 가능한 웹크롤링(한번만 크롤링 하는 게 아님)
    프로젝트 인프라 : Python으로 Crawling code 작성 > 파일 생성 > 서버를 통한 웹페이지 형식으로 출력
    >>> Crawling 파트별 코딩 기간 : 2021.03.14 ~ 2021.03.28
    <----- 2차 회의 내용 ----->
    1. 파트분배 
        - 장학공지 : 최재훈
        - 학사공지 : 최형순
        - 공지사항 : 신현수

    2. 프로젝트 구성 
        - main.py
        - scholarship_notice.py (장학공지)
        - univ_notice.py (학사공지)
        - notice.py (공지사항)
        >>> 공지사항에 새로운 부분이 있는지 없는지 판별하기 위해 해당 페이지에 있는 목록을 출력(iframe)

     3. 프로젝트 할 때의 사항들

        1. HNU_(함수이름) : 큰 틀
        2. 변수 : 동사 + 명사( ex : getData , beforeData , afterData ... ) 
	        >> 변수의 역할을 알 수 있도록 변수명 설정
        3. 사용 모듈 : Beautifulsoup4 ( 필요 시 추가될 수도 있음 )
        4. 함수 전에 이 함수가 어떤 역할을 하는지 설명하는 주석 달기
            >> 더 필요할 시 github의 기능을 이용하여 요청하기( 확인해달라는 요청은 카톡이나 개인적 연락으로도 가능 )

      4. 다음 회의 일정 : 2021.03.28 3:00pm

## ▶ 3.28. Meeting
    Date : 2021. 03. 28.
    participants : CMD_Web-Crawling Team(3)
    Date : 2021. 03. 28.
    <----- 3차 회의 내용 ----->
    1. Crawling 할 범위 지정
        - Crawling 할 내용 : 각자 맡은 파트(내용)의 제목 및 날짜
        - 웹 페이지 범위 : 각자 맡은 파트 최신 내용에 맞게( ex : 3page 정도 )
        - 파일 출력 방식 : csv 파일
        
    2. 다음 주 회의 내용 : 1. 크롤링 한 내용을 각각 링크를 적용하는 방식 or 새로운 개시글이 올라올 시 알림하는 방식
    
    3. 다음 주 추가 계획 : Crawling 한 내용을 웹페이지에 출력을 할 때 어떠한 원리로 구현되는지 강의( 설명 )
   
    4. 다음 회의 일정 : 2021.04.04 3:00pm

## ▶ 4.04. Meeting
    Date : 2021. 04. 04.
    participants : CMD_Web-Crawling Team(3)
    Date : 2021. 04. 04.
    <----- 4차 회의 내용 ----->
    1. 출력 방식 : 새로운 개시글이 올라올 시 알림하는 방식
        
    2. Crawling 한 내용을 웹 형식으로 출력하기 위해 쓸 도구 : Flask
    
    3. Flask 활용하기 위한 공부 기간 (4/26 ~ 5/1)
    ※ 해당 기간은 중간고사 기간을 고려한 것입니다. ( Flask 공부는 예상으로 한 8일 정도 소요될 것 같습니다.)
       추가적 중간, 기말고사 및 과제 등을 고려하여 정해진 기간동안 여유롭게 진행하기로 하였음
    ※ issue를 주기적으로 확인 및 활용해보도록 하자는 내용도 추가되었음.
   
    4. 다음 회의 일정 : 2021.05.02 3:00pm

## ▶ 5.02. Meeting
    Date : 2021. 05. 02.
    participants : CMD_Web-Crawling Team(3)
    Date : 2021. 05. 02.
    <----- 5차 회의 내용 ----->
    1. 맡은 역할 변경 사항
     - 이전 파트분배 : 장학공지 : 최재훈, 학사공지 : 최형순, 공지사항 : 신현수
     
     - 변경된 파트(이 분배가 효율적이라는 의견을 수용하여 변경) : 
      - crawling 기능 구현 : 신현수, 최형순
      - 서버 구현 : 최재훈
 
    2. 전체적인 일정
     - 1. 5/2 ~ 5/16 (2주일) // flask 공부기간 (5/16에 중간회의 및 공부 내용 정리) 
     - 2. 5/17 ~  5/31 각자 맡은 기능 구현 기간 (5/31에 기능 수정/피드백)
     - 3. 5/31 ~6/6 // 기능 통합 기간
     - 4. 6/7 ~ 6/25 시험기간 
     - 5. 6/26 ~ 7/1 발표준비 및 발표
      
