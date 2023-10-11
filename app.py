from flask import Flask, render_template, url_for, request, redirect
import sys

app = Flask(__name__)

#Home
@app.route('/')
def home():
    return render_template('home.html', page_name="About Me")

#Goals
@app.route('/goals')
def goals():
    return render_template('goals.html', page_name="My Goals")

#Projects
@app.route('/projects')
def projects():
    return render_template('projects.html', page_name="My Work")
@app.route('/projects/games')
def proj_games():
    return render_template('games.html', page_name="My Games")
@app.route('/projects/software')
def proj_software():
    return render_template('software.html', page_name="My Software")
@app.route('/projects/images')
def proj_images():
    return render_template('images.html', page_name="My Images")
@app.route('/projects/videos')
def proj_videos():
    return render_template('videos.html', page_name="My Videos")

#Reflection
@app.route('/reflection')
def reflection():
    return render_template("reflection.html", page_name="Reflection")

#Online
@app.route('/online')
def online():
    return render_template('online.html', page_name="Online Presence")

#Launch Website
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)