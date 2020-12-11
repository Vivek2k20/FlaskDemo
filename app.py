from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
    if(request.method=='GET'):
        a=""
        return render_template('index.html',a=a)
    else :
        a=request.form['content']
        return render_template('index.html',a=a)

if  __name__=="__main__":
    app.run(debug=True)