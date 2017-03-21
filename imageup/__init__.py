from flask import Flask

app = Flask(__name__)


app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

from imageup.views.route import app
from imageup.views.gallery import app
from imageup.views.galleryone import app
from imageup.views.deleteimage import app
from imageup.views.register import app
from imageup.views.upload import app
from imageup.views.logout import app

from imageup.models import app

