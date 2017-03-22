from flask import Flask, session, render_template
from functools import wraps

app = Flask(__name__,static_folder="images")


app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

def login_required(test):
    @wraps(test)
    def wrap( *args, **kwargs):
        if 'username_in' in session:
            return test(*args,**kwargs)
        else:
            return render_template('index.html')
    return wrap



from imageup.views.route import app
from imageup.views.gallery import app
from imageup.views.galleryone import app
from imageup.views.deleteimage import app
from imageup.views.register import app
from imageup.views.upload import app
from imageup.views.logout import app

from imageup.models import app

