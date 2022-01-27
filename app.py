from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def ask_questions():
    words = silly_story.prompts
    print(words)
    return render_template("questions.html", prompts=words)

@app.get("/story")
def add_story():
    completed_story = silly_story.generate(request.args)
    return render_template("story.html", completed_story=completed_story)
