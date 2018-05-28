import os
from flask import Flask, redirect,render_template,request

app = Flask(__name__)


messages =[]
banned_words =["cats"]



@app.route("/") # at this route in the url return the below
def get_index(): # this is the function located at the above route/url that gets called when the page is returned.
    return render_template("index.html")



@app.route("/login")
def create_user():
    username = request.args.get("username")
    return redirect(username)
    
    
def can_see_message(message, username):
    for_everyone = not message["body"].startswith("@")
    for_this_user = message["body"].startswith("@" + username)
    user_is_sender = message["sender"] == username
    
    return for_everyone or for_this_user or user_is_sender   
    
    
    
    
@app.route("/<username>")
def get_userpage(username):
    
     filtered_messages = []
     for message in messages:
        if can_see_message(message, username):
            filtered_messages.append(message)
            
            
     return render_template("chat.html", username=username , messages=filtered_messages)
    
    
    
@app.route("/new", methods = ["POST","GET"])
def get_add_message():
    
    username = request.form["username"]
    text = request.form["message"]


    words = text.split()  #splits word
    words = [ "*" * len(word) if word.lower() in banned_words else word for word in words] ##uses a * for each letter of the word if its in banned words
    text = " ".join(map(str,words)) #rejoins the word back together
    
    
    message = { 
    "sender": username,
    "body": text,
    }
        
  
        
        
    messages.append(message)
    return redirect(username)




if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))