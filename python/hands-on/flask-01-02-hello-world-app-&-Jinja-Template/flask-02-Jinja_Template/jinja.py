from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number = 20, number2 = 40)

@app.route('/sebahat')
def number():
    variable1 , variable2 = 23 , 45
    return render_template('body.html', num1=variable1, num2= variable2, multiplication=variable1+variable2)
    
@app.route ("/ikinci")
def second():
    return render_template("yeni.html")

if __name__=='__main__':
    app.run(debug = True)