print("#############################################################")
print("Time Explorer Web App")
print("datetime python library")
print("#############################################################")

from flask import Flask
from datetime import datetime
from flask import render_template
#import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/now/")
def now():
    return render_template(
         "now.html", 
        date = datetime.now() )

@app.route("/personal/")
@app.route("/personal/<name>")
def personal(name = None):
    
    if name == "sammy":
        return render_template(
            "personal.html", 
            name = "Your Lord" ,
            date = datetime.now() )
    elif name == "raw":
        return printoutnow()
    else:      
        return render_template(
            "personal.html", 
            name = name,
            date = datetime.now() )

@app.route("/api/")
def api():
    return render_template("api.html")

def printoutnow():
    now = datetime.now()
    print(now)
    somethingnew = now.__str__()
    return somethingnew

@app.route("/explorer/")
def exploredates():
    return render_template("explorer.html")



print("http://127.0.0.1:5000/")
print("http://127.0.0.1:5000/about")
print("http://127.0.0.1:5000/contact")
print("http://127.0.0.1:5000/now")
print("http://127.0.0.1:5000/explorer")
print("http://127.0.0.1:5000/api") #now
print("http://127.0.0.1:5000/personal")
print("http://127.0.0.1:5000/personal/sammy") #your lord
print("http://127.0.0.1:5000/personal/raw") #simple printback 
print("http://127.0.0.1:5000/personal/alice") #alice hello

def main():
    print("#############################################################")
    app.run()

if __name__ == "__main__":
    main()
