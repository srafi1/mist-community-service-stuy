from flask import Flask, render_template

@app.route('/')
def home():
    return 'hello world'

if '__main__' == __name__:
    app.debug = True
    app.run()
