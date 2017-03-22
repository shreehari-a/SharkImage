#shimages.com/static/images/<filename> 
from flask import Flask, request, redirect, url_for, session, abort, render_template ,Response ,flash ,send_from_directory, Blueprint
import os


from imageup import app
#app = Blueprint('views',__name__,
#                static_folder='static',
#                template_folder='templates')


@app.route('/uploaded/<filename>')
@app.route('/<username>/uploaded/<filename>')
def image_details(filename,username='anonymous'):
    
    link = os.path.join(request.url_root,"images",filename)
    filename = filename.split('.')
    img_id = filename[0]
    return render_template('details.html', img_id=img_id , link=link, username=username)
