from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Simone Izzo',
        'title' : 'Blog Post',
        'content' : 'First post content',
        'date_posted' : 'December 17, 2022'
    },{
        'author': 'Michele Alessandrino',
        'title' : 'Blog Post',
        'content' : 'Second post content',
        'date_posted' : 'December 16, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)