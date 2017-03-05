def getEvents():
    events = []
    f = open('data/events.csv', 'rU')
    s = f.read()
    events = toDict(s)
    return fixData(events, ['link', 'location', 'name', 'details'])
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
