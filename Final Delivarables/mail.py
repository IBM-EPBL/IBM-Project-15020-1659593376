from flask import Flask, render_template, request
from flask_mail import Mail,Message
import os

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] ='465'
app.config['MAIL_USERNAME']= 'abc@gmail.com.com'
app.config['MAIL_PASSWORD']= 'abcdef'
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        msg = Message("Customer Care", sender='CustomerCareRegistry@gmail.com',recipients=['email'])
        msg.body = "You are Successfully Registered in your account"  
        return "Send email."
    return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True)

