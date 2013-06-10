microblog
=========

플라스크 스터티용 문서입니다.  

<http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>

## 테스트 환경

* mac os x 10.8.3
* python-2.7.2

## 프로젝트 가상 환경

    $ mkvirtualenv microblog 
    $ pip install flask
    $ pip install flask-mail
    $ pip install flask-openid
    $ pip install flask-sqlalchemy
    $ pip install flask-whooshalchemy
    $ pip install flask-wtf
    $ pip install flask-babel
    $ pip install flup
    $ pip install sqlalchemy-migrate

## 프로젝트 디렉토리

    $ mkdir ~/FlaskProjects
    $ cd ~/FlaskProjects
    $ cd microblog


## Hello, World! 출력

    $ vim views.py
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)    

<http://localhost:5000> 접속

## 템플릿 HTML 츌력

### 템플릿

    $ mkdir templates
    $ vim templates/index.html
    <html>
      <head>
        <title>{{title}} - microblog</title>
      </head>
      <body>
          <h1>Hello, {{user.nickname}}!</h1>
      </body>
    </html>

### 뷰

    # -*- coding:utf8 -*-
    from flask import Flask
    from flask import render_template

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html',
            title = 'Home',
            user = {
                'nickname' : 'Jaru'
            }
        )

    if __name__ == '__main__':
        app.run(debug=True)    


## 템플릿 조건문 출력

    <html>
        <head> 
            {% if title %}
            <title>{{title}} - microblog</title>                                                                 
            {% else %}
            <title>Welcome to microblog</title>                                                                  
            {% endif %}                                                                                          
        </head>
        <body>
            <h1>Hello, {{user.nickname}}!</h1>
            {% for post in posts %}
            <p>{{post.author.nickname}}:<b>{{post.body}}</b></p>
            {% endfor %}
        </body>
    </html>
