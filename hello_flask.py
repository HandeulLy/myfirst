# hello_flask.py
# web server를 작동시키는 기본 code

from flask import Flask

app = Flask(__name__) # __*** : python 내부적으로 관리하는 변수

# http://(AWS의 IP주소):5000
@app.route("/") # 특정 URL 요청이 들어올 때 어떤 작업을 처리하는지 정의
# / : 브라우저로부터의 요청이 들어온다는 것
def hello_world() :
    return "hello world"

# http://127.0.01.1:5000/abc
@app.route("/abc") # 특정 URL 요청이 들어올 때 어떤 작업을 처리하는지 정의
# / : 브라우저로부터의 요청이 들어온다는 것
def hello_abc() :
    return "hello abc"

if __name__ == '__main__' : # 스스로 실행시킨 것이라면 아래 코드 실행
    app.run('0.0.0.0')