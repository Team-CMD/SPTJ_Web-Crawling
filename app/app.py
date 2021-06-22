from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import redirect
from hnu_notice import search_URL, HNU_notice
import time

Now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
app = Flask("WEB_CRAWLING")

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/hnu_notice")
def hnu_notice():
    notice_url = "http://www.hannam.ac.kr/community/community_0104.html"  # -> 공지
    notice_list = search_URL(notice_url, 1)
    notice_res = HNU_notice(notice_list)
    return render_template("hnu_notice.html", time = Now, Target_URL = notice_url, result = notice_res)

@app.route("/schalarship_notice")
def schalarship_notice():
    scholar_url = "http://janghak.hannam.ac.kr/sub4/menu_1.html"           # -> 장학
    scholar_list = search_URL(scholar_url, 4)
    scholar_res = HNU_notice(scholar_list)
    return render_template("schalarship_notice.html", time = Now, Target_URL = scholar_list, result = scholar_res)

@app.route("/univ_notice")
def univ_notice():
    univ_url = "http://www.hannam.ac.kr/guide/guide_0200.html"          # -> 학사
    univ_list = search_URL(univ_url, 3)
    univ_res = HNU_notice(univ_list)
    return render_template("univ_notice.html", time = Now, Target_URL = univ_url, result = univ_res)

if __name__=="__main__":
    app.run(host="0.0.0.0")