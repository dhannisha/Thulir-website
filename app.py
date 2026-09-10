from flask import Flask,request, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def about():
    return render_template ("aboutus.html")

@app.route('/gallery')
def gallery():
    return render_template ("gallery.html")

@app.route('/contactus')
def contactus():
    return render_template ("contactus.html")

app.run(debug=True)
