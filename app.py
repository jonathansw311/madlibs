from flask import Flask, request, render_template
from stories import *


app = Flask(__name__)

@app.route('/')
def home_page():
    keys = story.prompts
    return render_template("home.html", keys=keys)




@app.route('/story')
def display():
    ans = request.args
    disp = story.generate(ans)
    return  render_template("story.html", disp=disp)
    
@app.route('/drop')
def drop():
    storyList = list(storyWords.keys())
    return render_template("dropDown.html", storyList=storyList)

@app.route('/homeTwo')
def homeTwo():
    sstory=(request.args.get("StoryList"))
    keys=storyWords.get(sstory)
    print(sstory)
    print('sstory above')
    return  render_template("homeTwo.html", keys=keys, sstory=sstory)

@app.route('/storyTwo')
def story_Two():
    ans = request.args
    
    selectedstory=request.args.get('selected_Story')
    if selectedstory=='story':
       disp = story.generate(ans)
    if selectedstory=='storyTwo':
       disp = storyTwo.generate(ans)
 
    
    return  render_template("story.html", disp=disp)