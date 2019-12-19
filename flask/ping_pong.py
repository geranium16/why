from flask import Flask, render_template,request
# flask안에 Flask , reunder 있는것임
app=Flask(__name__)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    data = request.args.get('query')
    return render_template('pong.html',data=data)
# GET
# 암호화되지 않은 form의 데이터를 서버로 전송합니다.
# 가장 흔하게 사용되는 메소드입니다.
# get방식: 주소창에 모든 내용이 드러나는것
# request.args.get이 없으면 받지못한다.
@app.route('/naver')
def naver():
    return render_template('naver.html')
# request.arge.get이 없는 이유 : pong은 우리의 페이지다. 따라서 우리가 해결해야 하지만
# google은 구글 페이지이다. 구글이 처리한다.
@app.route('/google')
def google():
    
    return render_template('google.html')

# 원래 플라스크를 실행시키는 app.py이여서 FLASK_APP=ping_pong.py flask run이지만
# 디버그모드를 사용하기 위해 사용 아래를 사용하면 새로고침많으로 동기화
if __name__ ==("__main__"):
    app.run(debug=True)
#  주소의 시작은 /ping /pong 이 부분이다. 앞에 숫자는 그냥 내가 찾아가는 경로를 나타낸것뿐이다.
