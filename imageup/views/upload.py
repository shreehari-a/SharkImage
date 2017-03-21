import flask
from werkzeug.utils import secure_filename 
from datetime import datetime

import sqlite3 as sql
from PIL import Image
import bcrypt
import socket
import os


#import main app
from imageup import app


#shimage.com/upload >> private
@app.route("/upload",methods=['GET','POST'])
@app.route("/upload/<username>",methods=['GET','POST'])
#@login_required
def handle_upload(username='anonymous'):
    '''
    This is the upload data handler
    for guest username is set to anonymous
    upload details are stored into database
    images are stored into /static/images/<filename>.extension
    
    '''
    if flask.request.method == 'POST':             
        
        
        #get the file from the form
        file = flask.request.files['fileToUpload']
        filename = secure_filename(file.filename)
                
        #open database
        con = sql.connect("database.db")
        c = con.cursor()
        c.execute("select * from users")
        m=c.fetchone()
        print
        print str(m)
        print

        #create img table,insert active user too!
        sql_command1 = "create table if not exists imageDetails(\
                imageId integer primary key autoincrement,\
                originalFilename,\
                extension,\
                uploadDate,\
                uploadTime,\
                hostIp,\
                username references users(username))"
        c.execute(sql_command1)
                           
        #get extension
        extension_list = filename.split('.')
        extension = extension_list[1]
                
        #get host id
        host_ip = socket.gethostbyname(socket.gethostname())
                
        #get uploadDate
        upload_date = datetime.now().date()
        upload_date = str(upload_date)
                
        #get uploadTime
        upload_time = datetime.now().time()
        upload_time = str(upload_time)
                
        #insert fields into table
        
        sql_command3 = "insert into imageDetails(originalFilename,extension,uploadDate,uploadTime,hostIp,username)\
                values(?,?,?,?,?,?)"                           
        c.execute(sql_command3,(filename,extension,upload_date,upload_time,host_ip,username,))
        
        #generate a new filename
        sql_command4 = "select imageId from imageDetails where originalFilename=? and uploadTime=? and hostIp=?"
        c.execute(sql_command4,(filename,upload_time,host_ip,))
        new_filename = c.fetchone()
        new_filename = str(new_filename[0])+'.jpg'
        
        #database commit
        con.commit()
        con.close()
        
        #save image with new filename into directory
        file.save(os.path.join(os.getcwd(),'imageup','static', 'images', new_filename))
        print new_filename        
         
        #save thumbnail into /images/thumbnails
        size =256,192
        im = Image.open('imageup/static/images/'+new_filename)
        im.thumbnail(size,Image.ANTIALIAS)
        outfile = os.path.join(os.getcwd(),'imageup','static', 'images','thumbnails',os.path.splitext(new_filename)[0]+".thumbnail")
        im.save(outfile,"JPEG") 
       
              
        if username is 'anonymous':
            return flask.redirect(flask.url_for('image_details',filename=new_filename))
        return flask.redirect(flask.url_for('image_details',filename=new_filename,username=username))

    else:
        return "unauthorised url"


