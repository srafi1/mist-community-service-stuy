from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', page='home')

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities.html', page='opportunities')

@app.route('/studyhelp')
def studyhelp():
    return render_template('studyhelp.html', page='studyhelp')

@app.route('/testprep')
def testprep():
    return render_template('testprep.html', page='testprep')

@app.route('/studytips')
def studytips():
    return render_template('studytips.html', page='studytips')
    
@app.route('/contact')
def contact():
    return render_template('contact.html', page='contact')

if '__main__' == __name__:
    app.run(debug=True)
