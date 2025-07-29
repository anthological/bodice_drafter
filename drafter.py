### import libraries
#from cmu_graphics import *
from datetime import date

### read in dressform measurements from csv



### establish measurements

all_measurements = ['sizing type','neck', 'shoulder', 'front length', 'cross front','figure length','figure breadth', 'back length', 'cross back', 'bust', 'underbust', 'waist', 'high hip', 'low hip', 'side', 'armhole','front neck', 'back neck', 'half figure breadth', 'half cross front','half cross back', 'front bust', 'back bust', 'cup size','front waist', 'back waist', 'front armhole', 'back armhole']

example_user_measurements = dict()

example_user_measurements['neck']           = 17.5
example_user_measurements['shoulder']       = 4.25
example_user_measurements['front length']   = 15.75
example_user_measurements['cross front']    = 15.25
example_user_measurements['figure length']  = 10.75
example_user_measurements['figure breadth'] = 10
example_user_measurements['back length']    = 17
example_user_measurements['cross back']     = 16
example_user_measurements['bust']           = 49
example_user_measurements['underbust']      = 44.25
example_user_measurements['waist']          = 42
example_user_measurements['high hip']       = 51.25
example_user_measurements['low hip']        = 50.75
example_user_measurements['side']           = 8.5
example_user_measurements['armhole']        = 18.5

###

class user:
    def __init__(self, name, fittings = []):
        self.name = name
        self.initialized = date.today()
        self.fittings = [] #more fittings will be taken later


'''

okay. so we want, for the framework:
a bunch of users.
    within each user, we have a name, a date, US or metric, and a list of fittings.
        list of fittings is sorted by most recent.
            within each fitting, a date, and a dictionary of measurements.
                some of these measurements are taken from the user,
                some are calculated from measurements taken,
                some are guessed from clothing size,
                some are guessed without the clothing size.


with a complete list of measurements, you can output a bunch of points, which can be used
to draw lines.

then we draw the straight lines
then we draw the curves
then we draw the labels

then we display this as a preview

to output:
    if user is US user and using inches,
        scale to 2550x3300
    else:
        scale to 2480x3508
'''

###

def onAppStart(app):
    app.scene = "welcome"
    app.width = 800
    app.height = 400
    app.highlightedLeft = False
    app.highlightedRight = False
    app.highlightedBack = False
    app.highlightedContinue = False
