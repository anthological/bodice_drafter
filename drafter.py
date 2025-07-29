### import libraries
from cmu_graphics import *
#import csv
from datetime import date

### read in dress form measurements




### load example measurements

all_measurements = ['neck', 'shoulder', 'front length', 'cross front', 'figure length',
                    'figure breadth', 'back length', 'cross back', 'bust', 'unerbust',
                    'waist', 'high hip', 'low hip', 'side', 'armhole', 'mall size',
                    'front neck', 'back neck', 'half figure breadth', 'half cross front',
                    'half cross back', 'front bust', 'back bust', 'cup size',
                    'front waist', 'back waist', 'front armhole', 'back armhole']

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
example_user_measurements['mall size']      = "2X"

###

class user:
    def __init__(self, name, fittings = []):
        self.name = name
        self.initialized = date.today()
        self.fittings = [] #more fittings will be taken later


#class fitting:
    #def addFitting(self):





###

def onAppStart(app):
    app.scene = "welcome"
    app.width = 800
    app.height = 400
    app.highlightedLeft = False
    app.highlightedRight = False
    app.highlightedBack = False
    app.highlightedContinue = False
