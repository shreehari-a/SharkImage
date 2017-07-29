from flask import Flask, request, redirect, url_for, session, abort, render_template ,Response ,flash ,send_from_directory ,Blueprint
from datetime import datetime
import sqlite3 as sql
import bcrypt
import os

#import main app
from imageup import app

#shimages.com >> public
@app.route("/",methods=['POST','GET'])
def login():
    '''
    login page will be loaded and inputs are evaluated
    login fields,button - checks login validation - if login is valid render index.html
    for registration separate route is given
    
    '''

    if request.method == 'POST':      
        if 'login' in request.form:        
            #get username and password from form;user input
            username_in= request.form['username']
            password_in = request.form['password']
            
            #database connection 
            con = sql.connect("database.db")
            cur = con.cursor()

            #check the existance of user
            sql_command1 = "select password from users where username=(?)"           
            cur.execute(sql_command1,(username_in,))
            user_out = cur.fetchone()
                        
            
            # If Username_in not found, login is invalid
            if user_out is None:
                return render_template("index.html")
                        
            # Else then retrieve Password_out
            password_out = user_out[0]
                        
            #retrive the salt
            sq1 = "select salt from users where username=?"
            cur.execute(sq1,(username_in,))
            salt_out = cur.fetchone()
            salt_out = str(salt_out[0])
                        
            #hash password_in
            password_in = str(password_in)
            password_in = bcrypt.hashpw(password_in,salt_out)
                
            # Compare Password_in and Password_out
            if password_in == password_out:
                
                session['username_in'] = username_in
                username = session['username_in']
                print username
                con.commit
                con.close()
                return render_template('index.html', username=username)
            else:
                loginerror = "Invalid password"
                return render_template('index.html',loginerror=loginerror)
    else: 
        if 'username_in' in session:
            username_in = session['username_in']
            return render_template("index.html",username=session['username_in'])
        username_in = 'anonymous'  
        return render_template("index.html",username=username_in)
