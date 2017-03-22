#shimages.com/<username>/uploaded- public url uploaded images
import flask 
from datetime import datetime
import sqlite3 as sql
import os


from imageup import app


@app.route("/uploaded")
@app.route("/<username>/uploaded")
#@login_required
def gallery(username='anonymous'):
    '''
    Display the images uploaded

    '''
    #database connection
    con = sql.connect("database.db")
    cur = con.cursor()
    
    #search database for the images of user-<username>
    sql_command1="select imageId from imageDetails where username=?"
    cur.execute(sql_command1,(username,))
    imagelist=cur.fetchall()
    
    #arrange name into list
    image_list=[]
    for imageid in imagelist:
        image_list.append(str(imageid[0])+".thumbnail")
    
    return flask.render_template('gallery.html',image_list=image_list,username=username)

@app.route('/send_images/<filename>')
def sendimages(filename):
    filename = filename + '.thumbnail'
    path  = os.path.join(os.getcwd(),'imageup','images','thumbnails')
    return flask.send_from_directory(path,filename)
   
