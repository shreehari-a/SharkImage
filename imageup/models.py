from flask_login import UserMixin

from imageup import app

def login_required(test):
    @wraps(test)
    def wrap( *args, **kwargs):
        if 'username_in' in session:
            return test(*args,**kwargs)
        else:
            return render_template('index.html')
    return wrap


