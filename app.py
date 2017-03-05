from flask import Flask, render_template, request

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

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    rating = request.form.get('rating', 0)
    comment = request.form.get('comment', 0)
    if rating == 0 or comment == 0:
        return render_template('feedback.html')
    try:
        f = open('feedback.txt', 'rU')
        s = f.read()
        f.close()
        f = open('feedback.txt', 'w')
        f.write(s)
        s = rating + ',' + comment + '\n'
        f.write(s)
        print(s)
        f.close()
    except:
        print('error saving feedback')
    return render_template('thankyou.html')
    
if '__main__' == __name__:
    app.run(debug=True)
