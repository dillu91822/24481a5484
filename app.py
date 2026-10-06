from flask import Flask

app= Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to flaskapp = routing"

@app.route('/greet/<uname>')
def greet(uname):
    return f"good morning,{uname}!"

@app.route('/delete/<int: roll')
def delete_user(roll):
    return redirect(url_for('greet'))
@app.route('/calculator',methods=['GET','POST'])
def si():
    if request.method=='POST':
        p=float(request.form['p'])
        T=float(request.form['t'])
        R=float(request.form['r'])
        result = (P*T*R)/100
        total = p+result
        return render_template('index.html',result=result,total=total,p=P,t=T,r=R)
    return render_template('index.html')
if __name__ =='__main__':
    app.run(debug=True,port=3500)
