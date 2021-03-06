#sharkimages.com/<username>/uploaded- public url uploaded images
import flask 
from datetime import datetime
import sqlite3 as sql
import os
from functools import wraps

from imageup import app


@app.route("/uploaded",methods=['GET','POST'])
@app.route("/<username>/uploaded",methods=['GET','POST'])
def explore(username='anonymous'):
    print username 
    #secure url
    if username != 'anonymous' and  not flask.session:
        return flask.redirect(flask.url_for('login'))
   
    #database connection
    con = sql.connect("database.db")
    cur = con.cursor()
    
    #if explore input from user fetch all the images which are for user=anonymous
    if username == 'anonymous':
        sql_command1="select imageId from imageDetails where key='public'"
        cur.execute(sql_command1)
        imagelist=cur.fetchall()
    
    else:
        #search database for the images of user-<username>
        sql_command1="select imageId from imageDetails where username=? and key='private'"
        cur.execute(sql_command1,(username,))
        imagelist=cur.fetchall()
    
    username = 'anonymous'
    if flask.session:
        username = flask.session['username_in']
    
    #arrange name into list
    image_list=[]
    for imageid in imagelist:
        image_list.append(str(imageid[0])+".thumbnail")
    
    return flask.render_template('gallery.html',image_list=image_list,username = username)

@app.route('/send_images/<filename>')
def sendimages(filename):
    filename = filename + '.thumbnail'
    path  = os.path.join(os.getcwd(),'imageup','static','images','thumbnails')
    return flask.send_from_directory(path,filename)



