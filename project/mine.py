from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/1')
def blog_1():
    return render_template('blog.html')


@app.route('/blog/2')
def blog_2():
    return render_template('blog2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')


  

app.run(debug=True)
