from datetime import date
import csv
from cmu_graphics import *

### RUN ON KERNEL RESTART
from datetime import date
import csv
from cmu_graphics import *

allMeasurements = ['neck', 'shoulder', 'front length', 'cross front',
'figure length','figure breadth', 'back length', 'cross back', 'bust',
'underbust', 'waist', 'high hip', 'low hip', 'side', 'armhole','front neck',
'back neck', 'half figure breadth', 'half cross front','half cross back',
'front bust', 'back bust', 'cup size','front waist', 'back waist',
'front armhole', 'back armhole', 'waist height', 'high hip height',
'shoulder dart', 'side dart', 'armhole dart', 'center front dart',
'waist dart']
requiredMeasurements = allMeasurements[:15]

allForms = ['00']
for s in range(0, 24, 2): #womens sizes
    allForms.append(str(s))
for s in range(36, 52, 2): #mens sizes
    allForms.append(str(s))

example_measurements = dict()
for measurement in allMeasurements: #fills out dictionary with keys
    example_measurements[measurement]  = None
example_measurements['neck']           = 16
example_measurements['shoulder']       = 4.5
example_measurements['front length']   = 17
example_measurements['cross front']    = 14.5
example_measurements['figure length']  = 10.25
example_measurements['figure breadth'] = 7.75
example_measurements['back length']    = 18
example_measurements['cross back']     = 14.5
example_measurements['bust']           = 41
example_measurements['underbust']      = 33.75
example_measurements['waist']          = 37
example_measurements['high hip']       = 44.5
example_measurements['low hip']        = 44.5
example_measurements['side']           = 10.5
example_measurements['armhole']        = 16.25

with open('C:/Users/Janet/Documents/GitHub/bodice_drafter/smoother_measurements.csv', newline='') as wrapper:
    reader = csv.reader(wrapper)
    df = []
    for row in reader:
        df.append(row)

beneviento = dict()
for col in range(1, len(df[0])):
    beneviento[df[0][col]] = dict()
for form in beneviento:
    dfCol = df[0].index(form) #df's column index of that form's measurements
    for row in df:
        if row[0] != 'size': #skipping the name
            beneviento[form][row[0]] = row[dfCol]
            if beneviento[form][row[0]] == "":
                beneviento[form][row[0]] = None
            else:
                beneviento[form][row[0]] = float(row[dfCol])


### begin actual stuff

def initiateEverything():
    allMeasurements = ['neck', 'shoulder', 'front length', 'cross front',
    'figure length','figure breadth', 'back length', 'cross back', 'bust',
    'underbust', 'waist', 'high hip', 'low hip', 'side', 'armhole','front neck',
    'back neck', 'half figure breadth', 'half cross front','half cross back',
    'front bust', 'back bust', 'cup size','front waist', 'back waist',
    'front armhole', 'back armhole', 'waist height', 'high hip height',
    'shoulder dart', 'side dart', 'armhole dart', 'center front dart',
    'waist dart']
    requiredMeasurements = allMeasurements[:15]
    #the required measurements are the ones taken, the rest are calculated

    allForms = ['00']
    for s in range(0, 24, 2): #womens sizes
        allForms.append(str(s))
    for s in range(36, 52, 2): #mens sizes
        allForms.append(str(s))

    example_measurements = dict()
    for measurement in allMeasurements: #fills out dictionary with keys
        example_measurements[measurement]  = None
    example_measurements['neck']           = 16
    example_measurements['shoulder']       = 4.5
    example_measurements['front length']   = 17
    example_measurements['cross front']    = 14.5
    example_measurements['figure length']  = 10.25
    example_measurements['figure breadth'] = 7.75
    example_measurements['back length']    = 18
    example_measurements['cross back']     = 14.5
    example_measurements['bust']           = 41
    example_measurements['underbust']      = 33.75
    example_measurements['waist']          = 37
    example_measurements['high hip']       = 44.5
    example_measurements['low hip']        = 44.5
    example_measurements['side']           = 10.5
    example_measurements['armhole']        = 16.25

    #used csv library example from documentation (see readme)
    with open('C:/Users/Janet/Documents/GitHub/bodice_drafter/smoother_measurements.csv', newline='') as wrapper:
        reader = csv.reader(wrapper)
        df = []
        for row in reader:
            df.append(row)

    beneviento = dict()
    for col in range(1, len(df[0])):
        beneviento[df[0][col]] = dict()
    for form in beneviento:
        dfCol = df[0].index(form) #df's column index of that form's measurements
        for row in df:
            if row[0] != 'size': #skipping the name
                beneviento[form][row[0]] = row[dfCol]
                if beneviento[form][row[0]] == "":
                    beneviento[form][row[0]] = None
                else:
                    beneviento[form][row[0]] = float(row[dfCol])
    #beneviento is a dictionary of forms
    #each form is a dictionary of measurements
    return beneviento, allMeasurements, example_measurements

### user stuff
#we'll come back to this if we have time

class user:
    def __init__(self, name, fittings = []): #user, string, list of fittings
        self.name = name
        self.initialized = date.today()
        self.fittings = fittings
        self.fittings = self.sortFittings(self)
        self.measurements = self.fittings[0] #most recent fitting

    def sortFittings(self): #list of fittings
        sortedFittings = copy.deepcopy(self.fittings)
        #gotta figure out how to sort datetimes.date
        return sortedFittings

class fitting:
    def __init__(self, username = None): #fitting, string, dict
        self.measurements = dict()
        for m in allMeasurements:
            self.measurements[m] = None
        self.date = date.today()
        if username != None:
            for m in allMeasurements:
                if user.measurements[m] != None:
                    self.measurements[m] = user.measurements[m]


### fill out measurements


def guessSize(measures):
    if (measures['bust'] == None or
        measures['waist'] == None or
        measures['low hip'] == None):
            return None
    closestSize = ''
    closestSizeScore = 999
    for size in beneviento:
        if size != '':
            bustScore = (measures['bust'] - beneviento[size]['bust'])**2 / beneviento[size]['bust']
            waistScore = (measures['waist'] - beneviento[size]['waist'])**2 / beneviento[size]['waist']
            hipScore = (measures['low hip'] - beneviento[size]['low hip'])**2 / beneviento[size]['low hip']
            currScore = bustScore + 2*waistScore + hipScore
            if currScore < closestSizeScore:
                closestSize = size
    return closestSize


def interpolateMeasurements(measures, size = ''):
    if size == '':
        size = guessSize(measures)
        if size == None:
            print("please supply bust, waist, and hip")
            return None
    constructed = beneviento[size]
    for m in measures:
        if measures[m] != None:
            constructed[m] = measures[m]



def calculateMeasurements(measures, height = 66):
    #import known ones
    neck = measures['neck']
    shoulder = measures['shoulder']
    front_length = measures['front length']
    cross_front = measures['cross front']
    figure_length = measures['figure length']
    figure_breadth = measures['figure breadth']
    back_length = measures['back length']
    cross_back = measures['cross back']
    bust = measures['bust']
    underbust = measures['underbust']
    waist = measures['waist']
    high_hip = measures['high hip']
    low_hip = measures['low hip']
    side = measures['side']
    armhole = measures['armhole']
    #calculate the rest
    front_neck = neck/6 + 0.25
    back_neck = neck/6 + 0.375
    half_figure_breadth = figure_breadth/2
    half_cross_front = cross_front/2
    half_cross_back = cross_back/2
    front_bust = bust/4 + 0.25
    back_bust = bust/4 - 0.25
    cup_size = (bust - underbust - 4.5)//1
    front_waist = waist/4 + 0.25
    back_waist = waist/4 - 0.25
    front_armhole = armhole/2 - 0.25
    back_armhole = armhole/2 + 0.25
    front_high_hip = high_hip/4 + 0.25
    back_high_hip = high_hip/4 - 0.25
    front_low_hip = low_hip/4 + 0.25
    back_low_hip = low_hip/4 - 0.25
    #adjustments
    if front_length > back_length:
        front_armhole += 0.5
        back_armhole -= 0.5
    #height
    if height <= 64:
        LH_depth = 8
        HH_depth = 4
    elif height >= 70:
        LH_depth = 9
        HH_depth = 4
    else:
        LH_depth = 8.5
        HH_depth = 4
    #cup darts
    if cup_size == 1:
        shoulder_dart = 0.375
        side_dart = 0.75
        armhole_dart = 0.375
        CF_dart = 0.375
    elif cup_size == 2:
        shoulder_dart = 0.5
        side_dart = 1
        armhole_dart = 0.5
        CF_dart = 0.5
    elif cup_size == 3:
        shoulder_dart = 0.625
        side_dart = 1.25
        armhole_dart = 0.625
        CF_dart = 0.625
    else:
        shoulder_dart = 0.75
        side_dart = 1.5
        armhole_dart = 0.75
        CF_dart = 0.75
    #waist dart
    if low_hip - waist >= 14:
        waist_dart = 1.25
    elif low_hip - waist >= 10:
        waist_dart = 1
    elif low_hip - waist >= 8:
        waist_dart = 0.75
    elif low_hip - waist >= 2:
        waist_dart = 0.375
    else:
        waist_dart = 0
    #formatting
    out = {
    'neck': neck,
    'shoulder': shoulder,
    'frontLength': front_length,
    'crossFront': cross_front,
    'figureLength': figure_length,
    'figureBreadth': figure_breadth,
    'backLength': back_length,
    'crossBack': cross_back,
    'bust': bust,
    'underbust': underbust,
    'waist': waist,
    'highHip': high_hip,
    'lowHip': low_hip,
    'side': side,
    'armhole': armhole,
    'frontNeck': front_neck,
    'backNeck': back_neck,
    'halfFigureBreadth': half_figure_breadth,
    'halfCrossFront': half_cross_front,
    'halfCrossBack': half_cross_back,
    'frontBust': front_bust,
    'backBust': back_bust,
    'cupSize': cup_size,
    'frontWaist': front_waist,
    'backWaist': back_waist,
    'frontArmhole': front_armhole,
    'backArmhole': back_armhole,
    'frontHighHip': front_high_hip,
    'backHighHip': back_high_hip,
    'frontLowHip': front_low_hip,
    'backLowHip': back_low_hip,
    'lowHipDepth': LH_depth,
    'highHipDepth': HH_depth,
    'shoulderDart': shoulder_dart,
    'sideDart': side_dart,
    'armholeDart': armhole_dart,
    'centerFrontDart': CF_dart,
    'waistDart': waist_dart}
    return out

exampleMeasures = calculateMeasurements(example_measurements)

### generate guides
'''
(0,0) is at the center waist for both front and back drafts
The front side seam is in the +x direction
The back side seam is in the -x direction
Everything is in inches
Input m is a full dictionary of measurements
'''

def generateFrontGuidePoints(m): #m = measurements dictionary
    out = [(0,0),(m['frontLowHip'],0)] #waist line
    out.append([(0,-m['highHipDepth']),(m['frontLowHip'],-m['highHipDepth'])]) #high hip line
    out.append([(0,-m['lowHipDepth']),(m['frontLowHip'],-m['lowHipDepth'])]) #low hip line
    out.append([(0,m['frontLength']),(4,m['frontLength'])]) #neckline
    out.append([(0,m['frontLength']-3),(8,m['frontLength']-3)]) #cross-front line
    out.append([(0,m['frontLength']/2),(m['frontBust'],m['frontLength']/2)]) #bust line
    return out

def generateBackGuidePoints(m): #m = measurements dictionary
    out = [(0,0),(m['backLowHip'],0)] #waist line
    out.append([(0, -m['highHipDepth']),(m['backLowHip'], -m['highHipDepth'])]) #high hip line
    out.append([(0, -m['lowHipDepth']),(m['backLowHip'], -m['lowHipDepth'])]) #low hip line
    out.append([(0, m['backLength']),(9,m['backLength'])]) #neck/shoulder line
    out.append([(0, m['backLength']/4*3),(9, m['backLength']/4*3)]) #cross-back line
    out.append([(0, m['backLength']/2),(m['backBust'], m['backLength']/2)]) #bust line
    return out

### geometry


def skipDart(latestPoint):
    if latestPoint == 'Y':
        return 0.25 #come back to this math Later
    elif latestPoint == 'gg':
        return 0.25
    elif latestPoint == 't':
        return 0.125

def landOnGuideline(x1, y1, x2, y2, length):#   (x1,y1)     len
    #assuming that you're in a situation like>  (x2,y2)________gth.
    return

def pointAlongDiagLine(x1, y1, length, x2 = None, y2 = None, angle = None):
    return

def getArc(ellipse):
    return centerX, centerY, width, height, startAngle, sweepAngle

def walkAlongEllipse(ellipse, xy, length, direction):
    return

def getEllipse(x1, y1, x2, y2, x3, y3):
    return centerX, centerY, width, height


### helpers / helper-organizers

#front draft
def getpointF(m):
    return outX, outY

def getpointG(m):
    return outX, outY

def getpointH(m):
    return outX, outY

def getpointL(m):
    return outX, outY

def getpointaa(m):
    return outX, outY

def getpointcc(m):
    return outX, outY

def getpointdd(m):
    return outX, outY

def getpointee(m):
    return outX, outY

def getpointjj(m):
    return outX, outY

def getpointkk(m):
    return outX, outY

def getpointmm(m):
    return outX, outY

#back draft
def getpointd(m):
    return outX, outY

def getpointe(m):
    return outX, outY

def getpointf(m):
    return outX, outY

def getpointz(m):
    return outX, outY

def getpointCC(m):
    return outX, outY

def getpointDD(m):
    return outX, outY

def getpointHH(m):
    return outX, outY

def getpointII(m):
    return outX, outY

def getpointJJ(m):
    return outX, outY

def getpointKK(m):
    return outX, outY

def getpointLL(m):
    return outX, outY




### generate front moulage
'''
(0,0) is at the center waist for both front and back drafts
The front side seam is in the +x direction
The back side seam is in the -x direction
Everything is in inches
Input m is a full dictionary of measurements
'''

def generateFrontMoulagePoints(m):
    out = dict()
    #neck
    out['A'] = (0, m['frontLength'])
    out['B'] = (m['frontNeck'], m['frontLength'])
    out['C'] = (m['frontNeck'], m['frontLength']+(m['frontNeck']+0.125))
    out['D'] = (m['frontNeck'], m['frontLength']+(m['frontNeck']+0.125)/2)
    out['E'] = (m['frontNeck']+6, m['frontLength']+(m['frontNeck']+0.125)/2)
    #shoulder
    out['F'] = getPointF(m)
    out['G'] = getPointG(m)
    out['H'] = getPointH(m)
    #bust
    out['I'] = (0, m['frontLength']/2) #temp bust height
    out['J'] = (m['frontBust'], m['frontLength']/2)
    out['K'] = (m['halfFigureBreadth'], m['frontLength']/2)
    #high figure point
    out['L'] = getPointL(m)
    HFx, HFy = out['L'][0], out['L'][1]
    out['M'] = (0, HFy)
    #waist dart
    out['N'] = (m['halfFigureBreadth'], 0)
    out['O'] = (m['halfFigureBreadth'], -m['lowHipDepth'])
    out['P'] = (m['halfFigureBreadth']-(m['waistDart']/2), 0)
    out['Q'] = (m['halfFigureBreadth']+(m['waistDart']/2), 0)
    out['R'] = (m['halfFigureBreadth']-0.5, 0)
    out['S'] = (m['halfFigureBreadth'], -m['lowHipDepth']+3)
    #waist shaping
    out['T'] = (m['halfFigureBreadth']-(m['waistDart']/2), -0.5)
    out['U'] = (m['halfFigureBreadth']+(m['waistDart']/2), -0.5)
    #bust 2
    out['V'] = (HFx, HFy-0.75)
    out['W'] = (m['frontBust'], HFy)
    #waist
    out['X'] = (m['frontWaist']+m['waistDart'], 0)
    out['Y'] = (m['frontHighHip'] + skipDart('Y'), -m['highHipDepth'])
    out['Z'] = (m['frontLowHip'], -m['lowHipDepth'])
    #side
    out['aa']= getPointaa(m) #x should equal m['frontBust']
    #final bust
    out['bb']= (0, out['aa'][1])
    #waist shaping
    out['cc']= getPointcc(m) #up 3 inches from X along side, then in 0.125
    out['dd']= getPointdd(m) #along side, up 0.5 from w
    out['ee']= getPointee(m) #along side, dn 0.5 from w
    #you can bump out the waist dart, go down VN/4 then out 0.25
    out['ff']= None #shoulder dart shaping, unused
    out['gg']= (m['crossFront']+skipDart('gg'), m['frontLength']-3)
    out['hh']= (m['crossFront']+skipDart('gg'), out['aa'][1])
    #armhole curve
    out['ii']= (m['crossFront']+skipDart('gg')+1/2**0.5, out['aa'][1]+1/2**0.5)
    ellipseA = getEllipse(out['gg'], out['ii'], out['aa'])
    out['jj']= getPointjj(m, ellipseA)
    out['kk']= getPointkk(m, ellipseA)
    out['ll']= (out['B'][0]-1/2**0.5, out['B'][0]+1/2**0.5)
    #neckline curve
    ellipseN = getEllipse(out['A'], out['xx'], out['C'])
    out['mm']= getPointmm(m, ellipseN)
    return out, ellipseA, ellipseN


def generateBackMoulagePoints(m):
    out = dict()
    #neck
    out['a'] = (0, m['backLength'])
    out['b'] = (-m['backNeck'], m['backLength'])
    out['c'] = (-m['backNeck'], m['backLength']+1)
    #shoulder
    out['d'] = getPointd(m)
    out['e'] = getPointe(m)
    out['f'] = getPointf(m)
    #back contour
    out['g'] = None #these aren't used for a sloper
    out['h'] = None #but i'm still gonna keep track
    out['i'] = None #just in case
    out['j'] = (0, m['backLength']/4*3))
    #waist shaping
    out['k'] = (-m['backWaist']/2, 0)
    out['l'] = (-m['backWaist']/2-m['waistDart'], 0)
    out['m'] = (-m['backWaist']-m['waistDart'],0)
    out['n'] = (-m['backWaist']/2-m['waistDart']/2, -m['lowHipDepth'])
    out['o'] = (-m['backWaist']/2-m['waistDart']/2, -m['lowHipDepth']+3)
    out['p'] = (-m['backWaist']/2, -0.5)
    out['q'] = (-m['backWaist']/2-m['waistDart'], -0.5)
    out['r'] = (0, -0.5)
    out['s'] = None #more back contour
    out['t'] = (-m['backHighHip']+skipDart('t'), -m['highHipDepth'])
    out['u'] = (0, -m['lowHipDepth'])
    out['v'] = (-m['backLowHip'], -m['lowHipDepth'])
    #cross back
    out['w'] = (-m['crossBack'], m['backLength']/4*3))
    out['x'] = (0, m['backLength']/2)
    out['y'] = (-m['backBust'], m['backLength']/2)
    #side
    out['z'] = getPointz(m)
    out['AA']= (0, out['z'][1])
    out['BB']= None #waist shaping, like front 'cc'
    out['CC']= getPointCC(m)#along line KE, y = out['z'][1]-1
    out['DD']= getPointDD(m) #along line KE, y = out['e'][1]-3.5
    #armhole
    out['EE']= (-m['crossBack'], out['z'][1])
    out['FF']= (-m['crossBack']-1/2**0.5, out['z'][1]+1/2**0.5)
    ellipseA = getEllipse(out['w'], out['FF'], out['z'])
    #neck
    out['GG']= (-m['backNeck']+0.5/2**0.5, m['backLength']+0.5/2**0.5)
    ellipseN = getEllipse(out['w'], out['FF'], out['z'])
    out['HH']= getPointHH(m, ellipseA) #tracing ellipseA
    #redo shoulder
    out['II']= getPointII(m)
    out['JJ']= getPointJJ(m)
    out['KK']= getPointKK(m) #redo point DD
    out['LL']= getPointLL(m) #same length as II
    return out


### CMU_GRAPHICS

def onAppStart(app):
    app.scene = "welcome" #'measurements','sizes','drafter','output'
    app.width = 800
    app.height = 400
    app.highlightedLeft = False
    app.highlightedRight = False
    app.highlightedBack = False
    app.highlightedContinue = False

def redrawAll(app):
    if app.scene == "welcome":
        #draw background
        background = "lightPink"
        drawRect(0,0,app.width, app.height, fill = background)
        drawLabel("Welcome!", app.width//2,app.height//6, size = 20)
        drawLabel("Please select an input type:", app.width//2,
                    (app.height//6)*1.6)
        #draw measurements button
        if app.highlightedLeft:
            border1Color = "black"
        else:
            border1Color = background
        border1Width = 2
#remember to adjust rectangle width to always be wider than the text
        drawRect(app.width//4, app.height//2, app.width//6, app.height//10,
                    fill = "white", border = border1Color,
                    borderWidth = border1Width, align = "center")
        drawLabel("Measurements", app.width//4, app.height//2, size = 16,
                    align = "center")
        #draw sizes button
        if app.highlightedRight:
            border2Color = "black"
        else:
            border2Color = background
        border2Width = 2
        drawRect(app.width//4*3, app.height//2, app.width//6, app.height//10,
                    fill = "white", border = border2Color,
                    borderWidth = border2Width, align = "center")
        drawLabel("Clothing Size", app.width//4*3, app.height//2, size = 16,
                    align = "center")
    if app.scene == "measurements":
        #draw background
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
        #draw instructions
        TextLine1 = 'Please see attached guide on how to take measurements.'
        TextLine2 = "If you can't take all of these measurements yourself,"
        TextLine3 = 'feel free to leave some blank. You can also estimate your'
        TextLine4 = 'measurements with just your bust/chest, waist, and hip.'
        TextLine5 = 'These are taken at the widest and narrowest points.'
        drawLabel(TextLine1, app.width//6, app.height//4 + 00, align = "left-top")
        drawLabel(TextLine2, app.width//6, app.height//4 + 12, align = "left-top")
        drawLabel(TextLine3, app.width//6, app.height//4 + 24, align = "left-top")
        drawLabel(TextLine4, app.width//6, app.height//4 + 36, align = "left-top")
        drawLabel(TextLine5, app.width//6, app.height//4 + 48, align = "left-top")
        #draw back button
        if app.highlightedBack:
            border1Color = "black"
        else:
            border1Color = background
        border1Width = 2
        drawRect(app.width//6, app.height//7*6, app.width//8, app.height//12,
                    fill = "white", border = border1Color,
                    borderWidth = border1Width, align = "center")
        drawLabel("Go Back", app.width//6, app.height//7*6, align = "center")
        #draw continue button
        if app.highlightedContinue:
            border2Color = "black"
        else:
            border2Color = background
        border2Width = 2
        drawRect(app.width//6*5, app.height//7*6, app.width//8, app.height//12,
                    fill = "white", border = border2Color,
                    borderWidth = border2Width, align = "center")
        drawLabel("Continue", app.width//6*5, app.height//7*6, align = "center")
    if app.scene == "sizes":
        #draw background
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
        #draw back button
        if app.highlightedBack:
            border1Color = "black"
        else:
            border1Color = background
        border1Width = 2
        drawRect(app.width//6, app.height//7*6, app.width//8, app.height//12,
                    fill = "white", border = border1Color,
                    borderWidth = border1Width, align = "center")
        drawLabel("Go Back", app.width//6, app.height//7*6, align = "center")
        #draw continue button
        if app.highlightedContinue:
            border2Color = "black"
        else:
            border2Color = background
        border2Width = 2
        drawRect(app.width//6*5, app.height//7*6, app.width//8, app.height//12,
                    fill = "white", border = border2Color,
                    borderWidth = border2Width, align = "center")
        drawLabel("Continue", app.width//6*5, app.height//7*6, align = "center")
    if app.scene == "drafter":
        #draw background
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
    if app.scene == "output":
        #draw background
        background = "maroon"
        drawRect(0,0,app.width, app.height, fill = background)


def onMouseMove(app, mouseX, mouseY):
    if app.scene == "welcome":
        #highlight measurements button
        if ((app.width//4-app.width/12) < mouseX < (app.width//4+app.width/12) and
           (app.height//2-app.width//20) < mouseY < (app.height//2+app.height//20)):
               app.highlightedLeft = True
        else:
            app.highlightedLeft = False
        #hightlight sizes button
        if ((app.width//4*3-app.width/12) < mouseX < (app.width//4*3+app.width/12) and
           (app.height//2-app.width//20) < mouseY < (app.height//2+app.height//20)):
               app.highlightedRight = True
        else:
            app.highlightedRight = False
    if app.scene == "measurements" or app.scene == "sizes":
        app.highlightedLeft = False
        app.highlightedRight = False
        app.highlightedBack = False
        app.highlightedContinue = False
        #highlight back button
        if ((app.width//6-app.width/16) < mouseX < (app.width//6+app.width/16) and
           (app.height//7*6-app.width//24) < mouseY < (app.height//7*6+app.height//24)):
               app.highlightedBack = True
        else:
            app.highlightedBack = False
        #highlight continue button
        if ((app.width//6*5-app.width/16) < mouseX < (app.width//6*5+app.width/16) and
           (app.height//7*6-app.width//24) < mouseY < (app.height//7*6+app.height//24)):
               app.highlightedContinue = True
        else:
            app.highlightedContinue = False


def onMousePress(app, mouseX, mouseY):
    if app.scene == "welcome":
        #go to measurements scene
        if ((app.width//4-app.width/12) < mouseX < (app.width//4+app.width/12) and
           (app.height//2-app.width//20) < mouseY < (app.height//2+app.height//20)):
               app.scene = "measurements"
        #go to sizes scene
        if ((app.width//4*3-app.width/12) < mouseX < (app.width//4*3+app.width/12) and
           (app.height//2-app.width//20) < mouseY < (app.height//2+app.height//20)):
               app.scene = "sizes"
    if app.scene == "measurements" or app.scene == "sizes":
        #go back to welcome
        if ((app.width//6-app.width/16) < mouseX < (app.width//6+app.width/16) and
           (app.height//7*6-app.width//24) < mouseY < (app.height//7*6+app.height//24)):
               app.scene = "welcome"
        #go to drafter
        if ((app.width//6*5-app.width/16) < mouseX < (app.width//6*5+app.width/16) and
           (app.height//7*6-app.width//24) < mouseY < (app.height//7*6+app.height//24)):
               app.scene = "drafter"

def onMouseRelease(app, mouseX, mouseY):
    if app.scene == "measurements" or app.scene == "sizes":
        app.highlightedBack = False




###


def main():
    initiateEverything()
    runApp()

main()