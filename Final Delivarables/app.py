from flask import Flask, render_template, request
from mydb import connect
from flask_mysqldb import MySQL
from flask_mail import Mail,Message
import os
import ibm_db

app = Flask(__name__)

#database connection
def list_all():
   sql= "SELECT * from userregister"
   stmt = ibm_db.exec_immediate(conn, sql)
   dictionary = ibm_db.fetch_both(stmt)
   while dictionary != False:
     print ("The Name is : ",  dictionary["NAME"])
     print ("The email is : ", dictionary["EMAIL"])
     print ("The password is : ", dictionary["PASSWORD"])
     print ("The phone number is : ", dictionary["mobile number"])
     dictionary = ibm_db.fetch_both(stmt)

def insert_values(name,email,password,mobilenumber):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zhc67031;PWD=cMrI3QzWfo581pJ2;", "", "")
    sql = "INSERT INTO USERREGISTER VALUES('{}','{}','{}','{}')".format(name,email,password,mobilenumber)
    stmt = ibm_db.exec_immediate(conn,sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

#connect or not
try:
  conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zhc67031;PWD=cMrI3QzWfo581pJ2;", "", "")
  print("connection succesful")
except:
    print("not connected") 

#rendering home page
@app.route("/")
def homepage():
    return render_template("login.html")

#checking values in the login page
@app.route("/login",methods=['POST'])
def login():
    email=request.form['email']
    pwd=request.form['pwd']

    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
            return render_template('login.html',signupmsg=msg)
        if pwd != pwd:
            msg = 'Please enter correct confirm password'
            return render_template('login.html',signupmsg=msg)

#entering values are stored
result = ibm_db.exec_immediate(conn,f"SELECT * FROM userregister WHERE email LIKE '{email}'")
existing_user = ibm_db.fetch_row(result)

#get data in the registering page to enter
#store in the database
@app.route("/receivedata",methods=['POST'])
def result():
    name= request.form['name']
    email = request.form['email']
    password = request.form['password']
    phonenumber = request.form['phonenumber']
    connect.insert_values(name,email,password,phonenumber)
    return("Data received")  

    
#dont have an account sign up the page
@app.route("/sign up",methods=['POST'])
def signup():
    return render_template("Ticket.html")

#rendering ticket page for say their issue    
@app.route("/ticket",methods=['POST'])
def result(): 
      name=request.form['name']
      email = request.form['email']
      Productcategory = request.form['product category']
      ProblemDescription = request.form['Problem Decsription']
      return render_template("Ticket.html",message="Changes saved sucessfully!")

#insert data in the query
query = "SELECT * FROM customerprobem WHERE email=? AND passwrd=?"
        stmt = ibm_db.prepare(conn, query) # type:ignore
        ibm_db.bind_param(stmt,1,mail) # type:ignore
        ibm_db.bind_param(stmt,2,password) # type:ignore
        ibm_db.execute(stmt) # type:ignore
        user = ibm_db.fetch_assoc(stmt) # type:ignore
        print(user,password)

        if user:
            session["username"] = user['USERNAME']
            session['mail'] = mail
            return render_template('agent.html',username=session["username"],mail=session["mail"])
        else:
            msg = 'mail or password is not valid.'
            return render_template('home.html',signinmsg=msg)
        if request.method == "GET":
            return redirect(url_for('home'))


#agents info table
@app.route("/agent",methods=['POST'])
def result():
      name=request.form['name']
      email = request.form['email']
      password = request.form['password']
      technology = request.form['technology']
      experience = request.form['experience']
      return render_template("agent.html",message="Changes saved sucessfully!")
    
    if not name == session["username"] or not mail == session["mail"]:
            msg = "please don't change username and mail."
            return render_template('home.html',msg=msg)
    result = ibm_db.exec_immediate(conn,f"INSERT INTO agent (username,email,Technology,solution) VALUES('{name}','{mail}','{technology}','{solution}','{'0'}')")
        
        sendemail(mail,'complaint_creation')
        msg = 'Complaint registerd you check out complaints section.'
        return render_template('home.html',msg=msg)

#for generating email support
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] ='465'
app.config['MAIL_USERNAME']= 'abc@gmail.com.com'
app.config['MAIL_PASSWORD']= 'abcdef'
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#to get and send the mail for confirming my mail
@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        msg = Message("Customer Care", sender='CustomerCareRegistry@gmail.com',recipients=['email'])
        msg.body = "You are Successfully Registered in your account"  
        return "Send email."
    return render_template('Agent.html')


if __name__=="__main__":
    app.run(debug=True)