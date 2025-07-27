from cmu_graphics import *
#from cmu_cpcs_utils import Tree
#import csv

### UNRUNNABLE
def onAppStart(app):
    app.scene = "welcome"
    app.width = 800
    app.height = 400
    app.highlightedLeft = False
    app.highlightedRight = False


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
        blockOfText = "laskjf slkdf sklj \n lskdjf lksdj f"
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
        drawLabel(blockOfText, 200,200)
    if app.scene == "sizes":
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
    if app.scene == "drafter":
        background = "mistyRose"
        drawRect(0,0,app.width, app.height, fill = background)
    if app.scene == "output":
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


runApp(app)

