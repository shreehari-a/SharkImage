import flask
import sqlite3 as sql
import os

#import main app
from imageup import app


@app.route('/<username>/image_deleted/<image_id>')
def delete_image(image_id,username):
    con=sql.connect("database.db")
    c=con.cursor()
    sql_command="delete from imageDetails where imageId=%s"% (image_id,)
    c.execute(sql_command)
    con.commit()
    con.close()
    os.remove(os.path.join(os.getcwd(),'imageup','images',image_id+'.jpg'))
    os.remove(os.path.join(os.getcwd(),'imageup','images','thumbnails',image_id+'.thumbnail'))
    return  flask.redirect(flask.url_for('gallery',username=username))


