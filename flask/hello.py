from flask import Flask, escape, request, render_template
import random


app = Flask(__name__)

@app.route('/fstring')

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    # ,를 구분하기 위한 문법
    #  env FLASK_APP=hello.py flask run 가 없이 python hello.py만 해도 서버 켜지게함

@app.route('/hi') 
def hi():  # hi라는 곳에 들어가면
    name = "박대현"
    return render_template('hi.html',html_name=name)
    # hi.html을 렌더링해줘 , name이라는 별수를 넘겨주겟다.
# string: 사용할 이름명
@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name=name
    return render_template('greeting.html',html_name = def_name)

@app.route('/cube/<int:num>')
def cube(num):
    
    def_num=num**3
    return render_template('cube.html',def_num=def_num)

# 디너라는 곳으로 들어가면
#  디너를 작동해줘
@app.route('/dinner')
def dinner():
    menu=['삼각김밥','컵라면','스테이크','마라탕','훠궈']
    dinner=random.choice(menu)
    menu_img={'삼각김밥' :'https://ppss.kr/wp-content/uploads/2017/12/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-23.jpg',
                '컵라면':'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile25.uf.tistory.com%2Fimage%2F99A7CB355A4B982A0381DD',
                '스테이크':'http://recipe1.ezmember.co.kr/cache/recipe/2017/07/09/6741acc7f6bf0f7d04245851fb365c311.jpg',
                '마라탕':'https://img.ssfshop.com/cmd/LB_500x660/src/https://img.ssfshop.com/goods/ORBR/19/06/25/GPAQ19062509070_0_ORGINL.jpg',
                '훠궈':'http://mblogthumb1.phinf.naver.net/MjAxNzAxMThfMTQ4/MDAxNDg0NzEzMDg2ODEx.AlECVwpBlPPVVkPeopGuGIqhK3fc3m3vxK5-flVg-64g.kSxlkBitozZJ37A4EEWBxQGJc68l3q0otN5xlVrc3REg.JPEG.xodkqhgja1/%ED%9B%A0%EA%B6%881.jpg?type=w2'}
    img_url=menu_img[dinner]
    return render_template('dinner.html',dinner=dinner,img_url=img_url)

@app.route('/movies')
def movies():
    movies=['조카','거울왕콕','털미네이터','어벤척추']
    return render_template('movies.html',movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
