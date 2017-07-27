from flask import Flask, render_template, request

app = Flask(__name__)

def getEvents():
    events = []
    f = open('data/events.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'location', 'name', 'details'])
def getArts():
    arts = []
    f = open('data/arts.csv', 'rU')
    s = f.read()
    arts = toDict(s)
    return fixData(arts, ['link', 'duration', 'deadline', 'name', 'details'])
def getAwards():
    events = []
    f = open('data/awards.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'name', 'deadline', 'scholarship $ range', 'grade requirement'])
def getHealth():
    events = []
    f = open('data/health.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'name'])
def getLaw():
    events = []
    f = open('data/law.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'duration of program', 'deadline', 'name', 'details', 'age/grade requirements'])
def getLeadership():
    events = []
    f = open('data/leadership.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'deadline', 'name', 'details', 'duration', 'age/grade requirements'])
def getParks():
    events = []
    f = open('data/parks.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'deadline', 'age/grade requrements', 'location', 'name', 'details'])
def getService():
    events = []
    f = open('data/service.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'name', 'service'])
def getStem():
    events = []
    f = open('data/stem.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'deadline', 'duration', 'age/grade requirements', 'location', 'name', 'details'])
def toDict(s):
    opps = s.split('\n\n')
    for i in range(len(opps)):
        e = opps[i].split('\n')
        opps[i] = {}
        for d in e:
            d = d.split(': ')
            if len(d) > 1:
                opps[i][d[0].lower()] = d[1]
    return opps
def fixData(d, l):
    for i in range(len(d)):
        keys = d[i].keys()
        for p in l:
            if not p in keys:
                d[i][p] = ''
    return d
arts = getArts()
awards = getAwards()
events = getEvents()
health = getHealth()
law = getLaw()
leadership = getLeadership()
parks = getParks()
services = getService()
stem = getStem()

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', page='home')

@app.route('/opportunities')
def opportunities(arts=arts,awards=awards,events=events,health=health,law=law,leadership=leadership,parks=parks,services=services,stem=stem):
    return render_template('opportunities.html', page='opportunities',arts=arts,awards=awards,events=events,health=health,law=law,leadership=leadership,parks=parks,services=services,stem=stem)
        
@app.route('/studyhelp')
def studyhelp():
    return render_template('studyhelp.html', page='studyhelp')

@app.route('/testprep')
def testprep():
    return render_template('testprep.html', page='testprep')

@app.route('/collegeprep')
def collegeprep():
    return render_template('collegeprep.html', page='collegeprep')
    
@app.route('/feedback')
def contact():
    return render_template('contact.html', page='feedback')

@app.route('/feed', methods=['GET', 'POST'])
def feedback():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    message = request.form.get('message', '')
    if name == '' or email == '' or message == '':
        return render_template('feedback.html',name=name,email=email,message=message)
    try:
        f = open('feedback.txt', 'rU')
        s = f.read()
        f.close()
        f = open('feedback.txt', 'w')
        f.write(s)
        f.write(processComment(name, email, message))
        print(s)
        f.close()
    except:
        print('error saving feedback')
    return render_template('thankyou.html')

def processComment(a,b,c):
    c = c.replace('"', "'")
    c = '"' + c + '"'
    return a + ',' + b + ',' + c + '\n'

@app.route('/getfeedback')
def getfeedback():
    f = open('feedback.txt', 'rU')
    s = f.read()
    s = s.replace('\n', '<br>')
    return s
    
if '__main__' == __name__:
    app.run(debug=True)

@app.route('/NAME_OF_ROUTE')
def NAME_OF_ROUTE():
    return render_template('NAME_OF_FILE')
