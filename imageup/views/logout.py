import flask

from imageup import app


@app.route('/logout')
def logout():
    flask.session.clear()
    return flask.redirect(flask.url_for('login'))
