from flask import Flask,request, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_us')
def about():
    return render_template ("About_us.html")

@app.route('/gallery')
def gallery():
    return render_template ("gallery.html")

@app.route('/contact_us')
def contactus():
    return render_template ("Contact_us.html")

app.run(debug=True)
