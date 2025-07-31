from cmu_graphics import *
import csv

def onAppStart(app):
    app.scene = "welcome"
    app.width = 1080
    app.height = 720
    app.highlightedLeft = False
    app.highlightedRight = False
    app.highlightedBack = False
    app.highlightedContinue = False
    app.fLines=[('C', 'mm'),('mm','gg'),('aa','dd'),('dd','ee'),('ee', 'X'),('X', 'Y' ),
            ('Y', 'Z' ),('Z', 'nn'),('nn', 'A'),
            #('oo', 'L'),
            #('L', 'pp'),
            ('ii', 'L'),('L', 'kk'),('dd', 'L'),('L', 'ee'),('V', 'Q'),('Q', 'U'),
            ('U', 'S'),('S', 'T'),('T', 'P'),('P', 'V')]
    app.bLines=[('c','i'),('i','j'),('j','h'),('h','WW'),('ZZ','MM'),('MM','TT'),
            ('TT','VV'),('VV','m'),('m','AA'),
            #('c','LL'),
            #('LL','QQ'),
            ('QQ','OO'),('OO','PP'),
            #('PP','KK'),
            #('KK','c'),
            ('i','k'),('k','j')]
    app.beneviento = loadBeneviento()
    app.example = loadExample()
    app.user = dict()
    app.allMeasures = ['neck', 'shoulder', 'front length', 'cross front',
    'figure length','figure breadth', 'back length', 'cross back', 'bust',
    'underbust', 'waist', 'high hip', 'low hip', 'side', 'armhole','front neck',
    'back neck', 'half figure breadth', 'half cross front','half cross back',
    'front bust', 'back bust', 'cup size','front waist', 'back waist',
    'front armhole', 'back armhole', 'waist height', 'high hip height',
    'shoulder dart', 'side dart', 'armhole dart', 'center front dart',
    'waist dart']
    app.takingInput = False
    app.currentTextBox = ''
    app.sizeList = ['00']
    for s in range(0, 24, 2): #womens sizes
        app.sizeList.append(str(s))
    for s in range(36, 52, 2): #mens sizes
        app.sizeList.append(str(s))
    app.currentSize = ''
    app.highlightCenter = False #this is for scene 'sizes'
    app.isUsingSize = False


def loadBeneviento():
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

def loadExample():
    example = dict()
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
    return example


def drawBackAndContinue(app, background): #kinda broken?
        #draw back button
        if app.highlightedBack:
            border1Color = "black"
        else:
            border1Color = app.background
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
        drawBackAndContinue(app, background)

    if app.scene == "sizes":
        #draw background
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
        drawBackAndContinue(app, background)
        #input place for size
        if app.highlightCenter:
            border = 'black'
        else:
            border = background
        drawRect(app.width//2, app.height//2, app.width//6, app.height//4,
        fill = 'white', border = border, align = 'center')
        #mouseover to highlight
        #on click, app.addingText = True?
        drawLabel(app.currentTextBox, app.width//2, app.height//2, size = 24,
        align = 'center')
        if app.takingInput and app.currentTextBox == '':
            drawLabel('input size here', app.width//2, app.height//2, size = 24,
            fill = 'black', opacity = 50, align = 'center')
        if app.currentSize != '':
            drawLabel(f'Size = {app.currentSize}', app.width//2, app.height//2+30,
            size = 24, fill = 'black', align = 'center')


    if app.scene == "drafter":
        #draw background
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
        drawBackAndContinue(app, background)

    if app.scene == "output":
        #draw background
        background = "lightCoral"
        drawRect(0,0,app.width, app.height, fill = background)
        #draw download button
        drawRect(app.width//2, app.height//2, app.width//3, app.height//5,
                    fill = "white", border = 'black', align = "center")
        drawLabel(":3", app.width//2, app.height//2, size = 24, align = 'center')
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
    if app.scene != "welcome":
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
    if app.scene == 'sizes':
        if ((app.width//2-app.width//12) < mouseX < (app.width//2+app.width//12) and
            (app.height//2-app.height//8) < mouseY < (app.height//2+app.height//8)):
            app.highlightCenter = True
        else:
            app.highlightCenter = False



def onMousePress(app, mouseX, mouseY):
    if app.scene == "welcome":
        #go to measurements
        if ((app.width//4-app.width/12) < mouseX < (app.width//4+app.width/12) and
           (app.height//2-app.width//20) < mouseY < (app.height//2+app.height//20)):
               app.scene = "measurements"
               app.isUsingSize = False
        #go to sizes
        if ((app.width//4*3-app.width/12) < mouseX < (app.width//4*3+app.width/12) and
           (app.height//2-app.width//20) < mouseY < (app.height//2+app.height//20)):
               app.scene = "sizes"
               app.isUsingSize = True
    if app.scene != "welcome":
        #go back
        if ((app.width//6-app.width/16) < mouseX < (app.width//6+app.width/16) and
           (app.height//7*6-app.width//24) < mouseY < (app.height//7*6+app.height//24)):
            if app.scene == 'measurements' or app.scene == 'sizes':
                app.scene = 'welcome'
            elif app.scene == 'drafter':
                if app.isUsingSize:
                    app.scene = 'sizes'
                else:
                    app.scene = 'measurements'
            elif app.scene == 'output':
                app.scene = 'drafter'
        #continue
        if ((app.width//6*5-app.width/16) < mouseX < (app.width//6*5+app.width/16) and
           (app.height//7*6-app.width//24) < mouseY < (app.height//7*6+app.height//24)):
            if app.scene != 'drafter':
                app.scene = "drafter"
            else:
                app.scene = 'output'
    if app.scene == 'sizes':
        if ((app.width//2-app.width//12) < mouseX < (app.width//2+app.width//12) and
            (app.height//2-app.height//8) < mouseY < (app.height//2+app.height//8)):
            app.takingInput = True
        else:
            app.takingInput = False


def onMouseRelease(app, mouseX, mouseY):
    app.highlightedBack = False
    app.currentTextBox = ''
    app.currentSize = ''

def onMouseDrag(app, mouseX, mouseY):
    if app.scene != "welcome":
        app.highlightedBack = False

def onKeyPress(app, key):
    if app.scene == 'sizes':
        if app.takingInput and key.isdigit():
            app.currentTextBox += key
        if key == 'enter':
            if app.currentTextBox in app.sizeList:
                app.currentSize = app.currentTextBox
                print(app.currentSize)
                app.takingInput = False
            else:
                app.currentTextBox = 'Invalid Size'






runApp()

