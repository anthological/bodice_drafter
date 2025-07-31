from datetime import date
import csv
from cmu_graphics import *
import math
import copy

##

def initiateEverything(app):
#front lines:
    app.fLines=[('C', 'mm'),
            ('mm','gg'),
            ('aa','dd'),
            ('dd','ee'),
            ('ee', 'X'),
            ('X', 'Y' ),
            ('Y', 'Z' ),
            ('Z', 'nn'),
            ('nn', 'A'),
            #('oo', 'L'),
            #('L', 'pp'),
            ('ii', 'L'),
            ('L', 'kk'),
            ('dd', 'L'),
            ('L', 'ee'),
            ('V', 'Q'),
            ('Q', 'U'),
            ('U', 'S'),
            ('S', 'T'),
            ('T', 'P'),
            ('P', 'V')]

    #back lines:
    app.bLines=[('c','i'),
            ('i','j'),
            ('j','h'),
            ('h','WW'),
            ('ZZ','MM'),
            ('MM','TT'),
            ('TT','VV'),
            ('VV','m'),
            ('m','AA'),
            #('c','LL'),
            #('LL','QQ'),
            ('QQ','OO'),
            ('OO','PP'),
            #('PP','KK'),
            #('KK','c'),
            ('i','k'),
            ('k','j')]

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

    example = dict()
    for measurement in allMeasurements: #fills out dictionary with keys
        example[measurement]  = None
    example['neck']           = 16
    example['shoulder']       = 4.5
    example['front length']   = 17
    example['cross front']    = 14.5
    example['figure length']  = 10.25
    example['figure breadth'] = 7.75
    example['back length']    = 18
    example['cross back']     = 14.5
    example['bust']           = 41
    example['underbust']      = 33.75
    example['waist']          = 37
    example['high hip']       = 44.5
    example['low hip']        = 44.5
    example['side']           = 10.5
    example['armhole']        = 16.25

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
    return beneviento
    #app.beneviento is a dictionary of forms
    #each form is a dictionary of measurements
### fill measurements

def guessSize(app, measures):
    if (measures['bust'] == None or
        measures['waist'] == None or
        measures['low hip'] == None):
            return None
    closestSize = ''
    closestSizeScore = 999
    for size in app.beneviento:
        if size != '':
            bustScore = (measures['bust'] - app.beneviento[size]['bust'])**2 / app.beneviento[size]['bust']
            waistScore = (measures['waist'] - app.beneviento[size]['waist'])**2 / app.beneviento[size]['waist']
            hipScore = (measures['low hip'] - app.beneviento[size]['low hip'])**2 / app.beneviento[size]['low hip']
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
    constructed = app.beneviento[size]
    for m in measures:
        if measures[m] != None:
            constructed[m] = measures[m]
    return constructed


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
    'centerFrontDart': CF_dart, #i feel like there's an easier way to do this
    'waistDart': waist_dart}    #but some of my variable names are weird
    return out

### generate guidelines

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

### helpers


def skipDart(latestPoint):
    if latestPoint == 'Y':
        return 0.25 #close enough
    elif latestPoint == 'gg':
        return 0.25
    elif latestPoint == 't':
        return 0.125

def getLeg(hyp, leg):
    return ((hyp)**2-(leg**2)**0.5)

#def pointAlongDiagLine(x1, y1, length, x2 = None, y2 = None, angle = None):
    #return

#def getArc(ellipse):
    #return centerX, centerY, width, height, startAngle, sweepAngle

#def walkAlongEllipse(ellipse, xy, length, direction):
    #return

#def getEllipse(x1, y1, x2, y2, x3, y3):
    #return centerX, centerY, width, height


### helper wrappers

#front draft
def getPointF(m): #land on line
    CF = m['shoulder']+m['shoulderDart']
    CD = m(['frontNeck']+0.125)/2
    outY = m['frontLength']+(m['frontNeck']+0.125)/2
    outX = getLeg(CF, CD) + m['frontNeck']
    return outX, outY

def getPointsGH(m, out): #walk along line
    CD = (m['frontNeck']+0.125)/2
    CF = m['shoulder']+m['shoulderDart']
    DF = ((CF)**2-(CD**2)**0.5)
    sinth = CD / CF
    costh = DF / CF
    CG = m['shoulder']
    CH = m['shoulderDart'] + CG
    dGy = CG*sinth
    dGx = CG*costh
    dHy = CH*sinth
    dHx = CH*costh
    Cx, Cy = out['C']
    Gx = Cx+dGx
    Gy = Cy-dGy
    Hx = Cx+dHx
    Hy = Cy-dHy
    return Gx, Gy, Hx, Hy


def getPointL(m, out): #land on line
    AL = m['figureLength']
    A0 = out['K'][0]
    outX = A0
    outY = out['A'][1] - getLeg(AL, A0)
    return outX, outY

def getPointaa(m, out): #land on line
    Xa = m['side'] + m['sideDart']
    X0 = out['W'][0] - out['X'][0]
    outX = out['W'][0]
    outY = out['X'][1] + getLeg(Xa, X0)
    return outX, outY

def getPointsddee(m, out): #point on line
    ddY = out['W'][1]+0.5
    eeY = out['W'][1]-0.5
    #along line Xaa
    aaX, aaY = out['aa']
    Xx, Xy = out['X']
    m = (aaY-Xy)/(aaX-Xx)
    ddX = (ddX-Xy)/m + Xx
    eeX = (eeX-Xy)/m + Xx
    return ddX, ddY, eeX, eeY

def getPointsjjkk(m, out): #armhole ellipse
    cenX = out['aa'][0]
    cenY = out['gg'][1]
    radA = out['aa'][0]-out['gg'][0] #width
    radB = out['gg'][1]-out['aa'][1] #height
    if radA > radB:
        pass
        # (jjX - cenX)**2 /radA + (jjY - cenY)**2 /radB  = 1
        # (kkX - cenX)**2 /radA + (kkY - cenY)**2 /radB  = 1
    else:
        pass
        # (jjX - cenY)**2 /radA + (jjY - cenX)**2 /radB  = 1
        # (kkX - cenY)**2 /radA + (kkY - cenX)**2 /radB  = 1
        # sqrt((jjX-kkX)**2 + (jjY-kkY)**2) = m['armholeDart']
    # sqrt((jjX-iiX)**2 + (jjY-iiY)**2) = m['armholeDart']/2
    # sqrt((kkX-iiX)**2 + (kkY-iiY)**2) = m['armholeDart']/2
    #where ii is the lesser intersection between
    #the ellipse above and line y-out['hh'][1] = x-out['hh'][0]
    jjY = 10.9375
    kkY = 11.3175
    jjX = 7.8125
    kkX = 8.375
    return jjX, jjY, kkX, kkY

def getPointmm(m, out):
    #the arc length of an ellipse is.. at least an hour and a half of reading
    #it's been so long since i did any calculus dude
    #https://www.wolframalpha.com/input?i=elliptic+integral+of+the+second+kind
    #i'm already approximating the armhole curve to an ellipse and a line
    #but i can't get the armhole length without getting the arc length
    #so i guess you're just gonna have to pinch out the shoulders
    #it's not like this was gonna produce something perfectly fitted anyways
    # :(
    return out['F'][0], out['F'][1]-0.75
##

def getPointsoopp(m, out):
    ooX, ooY, ppX, ppY = None, None, None, None
    #oo = intersection GL and Cmm
    #pp = intersection HL and Cmm
    return ooX, ooY, ppX, ppY

#back draft
def getPointd(m): #land on line
    outX, outY = None
    return outX, outY

def getPointsef(m): #walk along line
    outX, outY = None
    return outX, outY

def getPointz(m):
    outX, outY = None
    return outX, outY

def getPointCC(m):
    outX, outY = None
    return outX, outY

def getPointDD(m):
    outX, outY = None
    return outX, outY

def getPointHH(m):
    outX, outY = None
    return outX, outY

def getPointII(m):
    outX, outY = None
    return outX, outY

def getPointJJ(m):
    outX, outY = None
    return outX, outY

def getPointKK(m):
    outX, outY = None
    return outX, outY

def getPointLL(m):
    outX, outY = None
    return outX, outY


### generate points
'''
(0,0) is at the center waist for both front and back drafts
The front side seam is in the +x direction
The back side seam is in the -x direction
Everything is in inches
Input (m) is a full dictionary of measurements
'''

def generateFrontMoulagePoints(app, m):
    out = dict()
    #neck
    out['A'] = (0, m['frontLength'])
    out['B'] = (m['frontNeck'], m['frontLength'])
    out['C'] = (m['frontNeck'], m['frontLength']+(m['frontNeck']+0.125))
    out['D'] = (m['frontNeck'], m['frontLength']+(m['frontNeck']+0.125)/2)
    out['E'] = (m['frontNeck']+6, m['frontLength']+(m['frontNeck']+0.125)/2)
    #shoulder
    out['F'] = getPointF(m)
    out['G'] = getPointsGH(m, out)[0], getPointsGH(m, out)[1]
    out['H'] = getPointsGH(m, out)[2], getPointsGH(m, out)[3]
    #bust
    out['I'] = (0, m['frontLength']/2) #temp bust height
    out['J'] = (m['frontBust'], m['frontLength']/2)
    out['K'] = (m['halfFigureBreadth'], m['frontLength']/2)
    #high figure point
    out['L'] = getPointL(m, out)
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
    out['aa']= getPointaa(m, out)
    out['bb']= (0, out['aa'][1])
    out['cc']= None #waist shaping
    out['dd']= getPointsddee(m, out)[0], getPointsddee(m, out)[1]
    out['ee']= getPointsddee(m, out)[2], getPointsddee(m, out)[3]
    out['ff']= None #shoulder dart bowing
    out['gg']= (m['crossFront']+skipDart('gg'), m['frontLength']-3)
    out['hh']= (m['crossFront']+skipDart('gg'), out['aa'][1])
    #armhole curve
    out['ii']= (m['crossFront']+skipDart('gg')+1/2**0.5, out['aa'][1]+1/2**0.5)
    out['jj']= getPointsjjkk(m, out)[0], getPointsjjkk(m, out)[1]
    out['kk']= getPointsjjkk(m, out)[2], getPointsjjkk(m, out)[3]
    out['ll']= (out['B'][0]-1/2**0.5, out['B'][0]+1/2**0.5)
    #neckline curve
    out['mm']= getPointmm(m, out)
    out['nn']= (0, -m['lowHipDepth'])
    out['oo']= getPointoo(m, out)
    out['pp']= getPointpp(m, out)
    app.frontPoints = out
    return out


def generateBackMoulagePoints(app, m):
    out = dict()
    #neck
    out['a'] = (0, m['backLength'])
    out['b'] = (-m['backNeck'], m['backLength'])
    out['c'] = (-m['backNeck'], m['backLength']+1)
    #shoulder
    out['d'] = getPointd(m)
    out['e'] = getPointsef(m)[0], getPointsef(m)[1]
    out['f'] = getPointsef(m)[2], getPointsef(m)[3]
    #back contour
    out['g'] = None #these aren't used for a sloper
    out['h'] = None #but i'm still gonna keep track
    out['i'] = None #just in case
    out['j'] = (0, m['backLength']/4*3)
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
    out['w'] = (-m['crossBack'], m['backLength']/4*3)
    out['x'] = (0, m['backLength']/2)
    out['y'] = (-m['backBust'], m['backLength']/2)
    #side
    out['z'] = getPointz(m)
    out['AA']= (0, out['z'][1])
    out['BB']= None #waist shaping
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
    out['MM']= (0, -m['lowHipDepth'])
    app.backPoints = out
    return out

### draft sloper

def coordsToPixels(app):
    app.frontPixels = dict()
    app.backPixels = dict()
    frontHeight = app.frontPoints['C'][1] + abs(app.frontPoints['nn'][1])
    backHeight = app.backPoints['c'][1]+ abs(app.frontPoints['MM'][1])
    app.canvasHeight = max(frontHeight, backHeight) + 4 #2" border
    frontWidth = app.frontPoints['Z'][0]
    backWidth = app.backPoints['v'][0]
    app.canvasWidth = max(frontWidth, backWidth) + 6 #2" separator

    app.waistHeight = app.canvasHeight - 2 - max(abs(app.frontPoints['nn'][1], abs(app.frontPoints['MM'][1])))

    for point in app.frontPoints:
        x, y = app.frontPoints[point][0], app.frontPoints[point][1]



def draftLines(app):
    for line in app.fLines:
        x1, y1 = app.frontPixels[line[0]]
        x2, y2 = app.frontPixels[line[1]]
        drawLine(x1, y1, x2, y2, fill='black')

    for line in app.bLines:
        x1, y1 = app.backPixels[line[0]]
        x2, y2 = app.backPixels[line[1]]
        drawLine(x1, y1, x2, y2, fill='black')


def draftCurves(app):
    #front neck
    Ax, Ay = app.frontPoints['A']
    Cx, Cy = app.frontPoints['C']
    drawArc(Ax, Cy, (Cx-Ax), (Cy-Ay), 270, 90, fill = None, border = "black")
    #front armhole
    ggX, ggY = app.frontPoints['gg']
    aaX, aaY = app.frontPoints['aa']
    drawArc(aaX, ggY, (aaX-ggX), (ggY-aaY), 180, 90, fill = None, border = "black")
    #back neck
    aX, aY = app.backPoints['a']
    cX, cY = app.backPoints['c']
    drawArc(aX, cY, (cX-aX), (cY-aY), 180, 90, fill = None, border = "black")
    #back armhole
    wX, xY = app.backPoints['w']
    zX, zY = app.backPoints['z']
    drawArc(zX, wY, (wX-zX), (wY-zY), 270, 90, fill = None, border = "black")
    #also gotta draw over all the radii in white


### model/view/controller

def onAppStart(app):
    app.scene = "welcome" #'measurements','sizes','drafter','output'
    app.width = 800
    app.height = 400
    app.highlightedLeft = False
    app.highlightedRight = False
    app.highlightedBack = False
    app.highlightedContinue = False
    app.beneviento = initateEverything()
    app.frontPonts = []
    app.backPoints = []
    app.canvasX, app.canvasY = app.width//6, app.height //8
    app.canvasWidth, app.canvasHeight = app.width//4, app.height//3*2
    initiateEverything(app)

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

    elif app.scene == "measurements":
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

    elif app.scene == "sizes":
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

    elif app.scene == "drafter":
        #draw background
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
        #create canvas for draft
        drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, fill = 'white', border = 'black')

    elif app.scene == "output":
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


### run!

def main():
    runApp()

main()

### more features
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


