from flask import Flask, request, redirect, url_for, session, abort, render_template ,Response ,flash ,send_from_directory ,Blueprint
from datetime import datetime
import sqlite3 as sql
import bcrypt
import os


from imageup import app


@app.route("/register",methods=['GET','POST'])
def register():
    
    if request.method == 'POST':       
     
        #get the informations from form
        
        username_in = request.form['username']
        password_in = request.form['password']
        
        #block username=anonymous
        if username_in is 'anonymous':
            return render_template('login.html')
        #connect to database
        con = sql.connect("database.db")
        cur = con.cursor()
        
        #create user table
        sql_command1 = "create table if not exists users(username primary key,salt,password)"
        cur.execute(sql_command1)
        cur.execute("select * from users where username=(?)",(username_in,))
        user = cur.fetchone()
        
        #if user doesnt exist
        if user is None:
            
            #hash the password
            salt = bcrypt.gensalt()
            password_in = str(password_in)
            password = bcrypt.hashpw(password_in,salt)
                
            #store into database
            cur.execute("INSERT INTO users (username,salt,password) VALUES (?,?,?)", (username_in,salt,password))
            con.commit()
            return "registration succes"
        #if user already exist
        else:
            error = 'User already exists'
            return render_template("login.html",error=error)
        con.close()
