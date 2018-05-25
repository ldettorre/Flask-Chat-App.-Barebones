import os
from flask import Flask, redirect,render_template,request

app = Flask(__name__)


@app.route("/") # at this route in the url return the below
def get_index(): # this is the function located at the above route/url that gets called when the page is returned.
    return render_template("index.html")

messages =[]
banned_words =["fuck"]



# @app.route('rooms/add')
# def add_room():
#     roomname = request.form['roomname']
#     rooms[roomname] = []
#     return redirect(....)


@app.route("/login")
def create_user():
    username = request.args.get("username")
    return redirect(username)
    
    
    
@app.route("/<username>")
def get_userpage(username):
    return render_template("chat.html",username=username, all_messages=messages)
    
    
    
@app.route("/<username>/new", methods = ["POST"])
def get_add_message(username):
    text = request.form["message"]




    words = text.split()
    for i in range(len(words)):
        for j in range(len(banned_words)):
            if words[i] == banned_words[j]:
                words[i] = "*"*len(words[i])
    text = " ".join(map(str,words))
    message = { 
    "sender": username,
    "body": text
    }
        
  
        
        
    messages.append(message)
    return redirect(username)




if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))