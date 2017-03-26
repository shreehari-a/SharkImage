#shimages.com/static/images/<filename> 
import os
import flask

from imageup import app
#app = Blueprint('views',__name__,
#                static_folder='static',
#                template_folder='templates')


@app.route('/uploaded/<filename>')
@app.route('/<username>/uploaded/<filename>')
def image_details(filename,username='anonymous'):
    
    if username != 'anonymous' and  not flask.session:
        return flask.redirect(flask.url_for('login'))
 
    link = os.path.join(flask.request.url_root,"images",filename + '.jpg')
    filename = filename.split('.')
    img_id = filename[0]
    return flask.render_template('details.html', img_id=img_id , link=link, username=username)


@app.route('/send_one_image/<filename>')
def sendoneimage(filename):
    path = os.path.join(os.getcwd(),'imageup','images')
    return flask.send_from_directory(path,filename)
