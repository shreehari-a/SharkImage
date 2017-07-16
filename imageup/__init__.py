import flask 
from functools import wraps

app = flask.Flask(__name__)


app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx',
    
)

app.config["CACHE_TYPE"] = "null"
app.config['STATIC_FOLDER'] = 'images'


from imageup.views.route import app
from imageup.views.gallery import app
from imageup.views.galleryone import app
from imageup.views.deleteimage import app
from imageup.views.register import app
from imageup.views.upload import app
from imageup.views.logout import app







