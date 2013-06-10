# -*- coding:utf8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
        title = 'Home',
        user = {
            'nickname' : u'자루'
        },
        posts = [
            {
                'author' : {
                    'nickname' : u'오리',
                },
                'body' : u'꽥꽥',
            },
            {
                'author' : {
                    'nickname' : u'나비',
                },
                'body' : u'냐옹',
            },
        ]
    )

if __name__ == '__main__':
    app.run(debug=True)
