#Need to download and install Flask (python -m pip install flask)
#https://flask.palletsprojects.com/en/2.1.x/installation/

#to run, use $env:FLASK_APP = "main" in powershell
#in CMD, use set FLASK_APP=main
#in bash, use export FLASK_APP=main

#after that, use flask run
#and open http://127.0.0.1:5000/ in your browser
from flask import Flask

app = Flask(__name__)
@app.route('/')
def main():
    return '<p>This is our app! Hello world!</p>'

#print("Enter first word:")
#word1 = input()
#while (" " in word1) :
#    print("ERROR: Must be one word")
#    print("Enter first word:")
#    word1 = input()
#print("Enter second word:")
#word2 = input()
#while (" " in word2) :
#    print("ERROR: Must be one word")
#    print("Enter second word:")
#    word2 = input()
#print("Your two words are " + word1 +" and " + word2)