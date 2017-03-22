import flask

from imageup import app


@app.route('/logout')
def logout():
    flask.session.pop('username_in',None)
    logoutmsg = 'You are successfully logged out'
    username_in = 'anonymous'
    return flask.render_template('index.html',username_in=username_in)
