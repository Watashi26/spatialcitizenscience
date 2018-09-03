from flask import Flask, render_template, url_for
import sys

app = Flask(__name__)


posts = [
    {"author": "Max",
     "maintitle" : "Webpage Titel",
     "date_posted" : "April 20, 2018",
     "comment" : "Das sind allgemeine Informatinen ueber die Seite."
     },
        {"author": "Bob",
     "maintitle" : "Titel",
     "date_posted" : "April 22, 2018",
     "comment" : " Nochmal, das sind allgemeine Informatinen ueber die Seite."
     }
    ]



@app.route('/') #mehere Namen sind gleichzietig moeglich
def mainpage():
    return render_template("main.html", posts=posts)

@app.route('/blog')
def blog():
    return render_template("blog.html", posts=posts, title="blog")

@app.route('/map')
def map():
    return render_template("map.html", posts=posts, title="map")

@app.route('/form')
def form():
    return render_template("form.html", posts=posts, title="form")

@app.route('/about')
def about():
    return render_template("about.html", posts=posts, title="About")


# routs können dann raus
@app.route('/login')
def login():
    return render_template("about.html", posts=posts, title="About")
@app.route('/register')
def register():
    return render_template("about.html", posts=posts, title="About")



if __name__ == "__main__":
    app.run(debug=True) # server neustart bei Veraenderungen wird vermieden
