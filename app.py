from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'If you can read this, then the site didn\'t crash :D'

if '__main__' == __name__:
    app.run(debug=True)
