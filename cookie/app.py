from flask import Flask, render_template, request, make_response

import base64

app = Flask(__name__)

flag = "2023BSC{_True_if_sanghyuk.weight==104_else_True}"

@app.route('/')
def index():
    cookie = request.cookies.get('id')

    if cookie:
        decoded_cookie = base64.b64decode(cookie).decode('utf-8')

        if decoded_cookie == "admin":
            return render_template('index.html', user="admin", flag=flag)
        else:
            return render_template('index.html', user="user")

    encoded_cookie = base64.b64encode('guest'.encode('utf-8')).decode('utf-8')
    response = make_response(render_template('index.html', user="user"))
    response.set_cookie('id', encoded_cookie)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
