from bottle import route, run
from bottle import get, post, request # or route
from bottle import *

USERS = {}


@route('/')
def hello():
    # user render
    hello_page = ""
    for user in USERS.keys():
        hello_page += (f"<li><a href='/{...}'>{user}</a></li>")
    hello_page = f"<ul>{hello_page}</ul>"
    # greetings render
    hello_page = f"<h2>WELLCOME TO HOMEPAGE</h2><br>{hello_page}"
    return hello_page


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    def check_login(username, password):
        print(username)
        print(password)
        return True

    if check_login(username, password):
        USERS.update({username: password})
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def main():
    run(host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()