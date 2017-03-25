#shimages.com/<username>/uploaded- public url uploaded images
import flask 
from datetime import datetime
import sqlite3 as sql
import os


from imageup import app
from imageup import login_required

@app.route("/<username>/uploaded",methods=['GET','POST'])
@login_required
def explore(username='anonymous'):
    print "haha-this is protected"
    '''
    Display the images uploaded

    '''
    #database connection
    con = sql.connect("database.db")
    cur = con.cursor()
    
    #if explore input from user fetch all the images which are for user=anonymous
    if flask.request.args.get('explore'):
        sql_command1="select imageId from imageDetails where username='anonymous'"
        cur.execute(sql_command1)
        imagelist=cur.fetchall()
    
    else:
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


@app.route("/uploaded",methods=['GET','POST'])
def gallery(username='anonymous'):
    '''
    Display the images uploaded

    '''
    #database connection
    con = sql.connect("database.db")
    cur = con.cursor()
    
    #if explore input from user fetch all the images which are for user=anonymous
    if flask.request.args.get('explore'):
        sql_command1="select imageId from imageDetails where username='anonymous'"
        cur.execute(sql_command1)
        imagelist=cur.fetchall()
    
    else:
        #search database for the images of user-<username>
        sql_command1="select imageId from imageDetails where username=?"
        cur.execute(sql_command1,(username,))
        imagelist=cur.fetchall()
    
    
    #arrange name into list
    image_list=[]
    for imageid in imagelist:
        image_list.append(str(imageid[0])+".thumbnail")
    
    return flask.render_template('gallery.html',image_list=image_list,username=username)
 
