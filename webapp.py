import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1',methods=['GET','POST'])
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["Ultimate-Life-Form"]=request.form['Ultimate-Life-Form']
    return render_template('page3.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    session["Location"]=request.form['Location']
    return render_template('page4.html')

@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    session["standName"]=request.form['standName']
    return render_template('page5.html')

@app.route('/page6' ,methods=['GET', 'POST'])
def renderPage6():
    session["DanceName"]=request.form['DanceName']
    return render_template('page6.html')

@app.route('/page7',methods=['GET','POST'])
def renderPage7():
    session["ChildName"]=request.form['ChildName']
    return render_template('page7.html')

@app.route('/page8',methods=['GET','POST'])
def renderPage8():
    session["President"]=request.form['President']
    return render_template('page8.html')

@app.route('/page9',methods=['GET','POST'])
def renderPage9():
    session["WoUstand"]=request.form['WoUstand']
    session["WoUstandUser"]=request.form['WoUstandUser']
    return render_template('page9.html')

@app.route('/page10',methods=['GET','POST'])
def renderPage10():
    session["Title"]=request.form['Title']
    return render_template('page10.html')


if __name__=="__main__":
    app.run(debug=True)
