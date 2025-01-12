from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def run():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def marks():
    Physics=int(request.form['Physics'])
    Maths= int(request.form['Maths'])
    Chemistry = int(request.form['Chemistry'])
    Computer_Science = int(request.form['Computer_Science'])
    English = int(request.form['English'])
    result = Physics + Maths + Chemistry + Computer_Science + English
    Percentage = result/5
    return render_template('home.html',Percentage=Percentage)

if __name__=='__main__':
    app.run(debug=True)
