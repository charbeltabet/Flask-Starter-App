from flask import Flask, request, render_template, escape
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/forms', methods=["GET", "POST"])
def forms():
    if request.method == "GET":
        if 'data' in request.args: 
            data = escape(request.args['data'])
            return render_template('forms.html', GetData=data)
    
    if request.method == "POST":
        if 'data' in request.form:
            data = escape(request.form['data'])
            return render_template('forms.html', PostData=data)

    return render_template('forms.html')


if __name__ == "__main__":
    app.run(debug=True)
