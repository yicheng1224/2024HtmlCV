from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)
@app.route('/')
def inital():
    return render_template("homepage.html")

@app.route('/submit',methods=["POST"])
def post_info():
    email = request.form.get('email')
    identity = request.form.get('identity')
    response = request.form.get('response')
    satisfaction = request.form.get('satisfaction')
    
    return render_template('respones.html', email=email, identity=identity, response=response, satisfaction=satisfaction)

if __name__ == '__main__':
    app.run()


