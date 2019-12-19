from flask import Flask, escape, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
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
    return render_template('cube.html',html_num=def_num)
     

if __name__ == "__main__":
    app.run(debug=True)

