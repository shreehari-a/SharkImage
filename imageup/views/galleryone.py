#sharkimages.com/static/images/<filename> 
import os
import flask
import sqlite3 as sql
from imageup import app


@app.route('/uploaded/<filename>')
@app.route('/<username>/uploaded/<filename>')
def image_details(filename,username='anonymous'):
    print
    print "hello"
    print

    print username
    print filename
    #secure url

    if username != 'anonymous' and  not flask.session:
        return flask.redirect(flask.url_for('login'))
    
    conn = sql.connect('database.db')
    c = conn.cursor()
    command1 = "select key from imageDetails where imageId=?"
    c.execute(command1,(filename,))
    key = c.fetchone()
    if key !=None:
        key = key[0]
    elif username != 'anonymous':
        key = 'private'
    else:
        key = 'public'
    #link for sharing
    link = os.path.join(flask.request.url_root,"images",filename + '.jpg')
    filename = filename.split('.')
    img_id = filename[0]

    if flask.session:
        username = flask.session['username_in']

    return flask.render_template('details.html', img_id=img_id , link=link, username=username, key=key)

@app.route('/send_one_image/<filename>')
def sendoneimage(filename):
    path = os.path.join(os.getcwd(),'imageup','images')
    return flask.send_from_directory(path,filename)

@app.route('/makepublic/<username>/<image_id>')
def makepublic(username,image_id):
    print username
    print image_id
    conn = sql.connect('database.db')
    c = conn.cursor()
    command = "update imageDetails set key='public' where imageId=?"
    c.execute(command,(image_id,))
    conn.commit()
    return flask.redirect(flask.url_for('explore',username=username))
