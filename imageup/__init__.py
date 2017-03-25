import flask 
from functools import wraps

app = flask.Flask(__name__)


app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx',
    
)

app.config["CACHE_TYPE"] = "null"

def login_required(test):
    @wraps(test)
    def wrap( *args, **kwargs):
        if 'username_in' or 'username'  in session:
            return test(*args,**kwargs)
            print username_in
        else:
            flask.flash("you are not logged in")
            return flask.redirect(flask.url_for('login'))
    return wrap


from imageup.views.route import app
from imageup.views.gallery import app
from imageup.views.galleryone import app
from imageup.views.deleteimage import app
from imageup.views.register import app
from imageup.views.upload import app
from imageup.views.logout import app

from imageup.models import app



