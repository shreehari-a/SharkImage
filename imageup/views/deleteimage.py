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
    os.remove(os.path.join(os.getcwd(),'static','images',image_id+'.jpg'))
    os.remove(os.path.join(os.getcwd(),'static','images','thumbnails',image_id+'.thumbnail'))
    return flask.Response('''deleted <a href="/%s/uploaded">go back to gallery</a>''')%(username,)
