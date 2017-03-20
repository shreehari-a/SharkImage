import flask

from imageup import app

@app.route('/logout')
def logout():
    flask.session.pop('username_in',None)
    logoutmsg = 'You are successfully logged out'
    return flask.render_template('login.html',logoutmsg=logoutmsg)
