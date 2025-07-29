### notes to self

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

### import libraries
#from cmu_graphics import *
from datetime import date
import csv


### load in constants
allMeasurements = ['neck', 'shoulder', 'front length', 'cross front','figure length','figure breadth', 'back length', 'cross back', 'bust', 'underbust', 'waist', 'high hip', 'low hip', 'side', 'armhole','front neck', 'back neck', 'half figure breadth', 'half cross front','half cross back', 'front bust', 'back bust', 'cup size','front waist', 'back waist', 'front armhole', 'back armhole']
requiredMeasurements = allMeasurements[:15]
allForms = ['00']
for s in range(0, 24, 2): #womens forms
    allForms.append(str(s))
for s in range(36, 52, 2): #mens forms
    allForms.append(str(s))


### hardcoded example

example_measurements = dict()
for measurement in allMeasurements:
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


### filling in default sizes

with open('C:/Users/Janet/Documents/GitHub/bodice_drafter/dressform_measurements.csv', newline='') as wrapper:
    reader = csv.reader(wrapper)
    df = []
    for row in reader:
        df.append(row)

beneviento = dict() #hehe
for col in range(1, len(df[0])):
    beneviento[df[0][col]] = dict()
    for rowName in allMeasurements:
        beneviento[df[0][col]][rowName] = None

for form in beneviento:
    formIndex = allForms.index(form)
    print(formIndex, form, df[0][formIndex+1])
    for measurement in form:
        beneviento[form][measurement] = None

### user stuff

class user:
    def __init__(self, name, fittings = []): #user, string, list of fittings
        self.name = name
        self.initialized = date.today()
        self.fittings = []
        self.fittings = self.sortFittings(self)
        self.measurements = self.fittings[0]

    def sortFittings(self):

        return sortedFittings

###

class fitting:
    def __init__(self, username = None): #fitting, string, dict
        allMeasurements = ['neck', 'shoulder', 'front length', 'cross front','figure length','figure breadth', 'back length', 'cross back', 'bust', 'underbust', 'waist', 'high hip', 'low hip', 'side', 'armhole','front neck', 'back neck', 'half figure breadth', 'half cross front','half cross back', 'front bust', 'back bust', 'cup size','front waist', 'back waist', 'front armhole', 'back armhole']
        self.measurements = dict()
        for m in allMeasurements:
            self.measurements[m] = None
        self.date = date.today()
        if username != None:
            user = None #look up username
            for m in allMeasurements:
                if user.measurements[m] != None:
                    self.measurements[m] = user.measurements[m]



### functions to calculate measurements


def calculateMeasurements(measures): #takes dictonry
    toCalculate = []
    for key in measures:
        if measures[key] == None:
            toCalculate.append(key)
    for key in toCalculate:
        if key in requiredMeasurements:
            measures = interpolateMeasurements(measures)



def interpolateMeasurements(measures, knownSize = None):
    toCalculate = []
    if knownSize != None:
        sizeMeasurements = allSizes[knownSize] #dict
        for size in sizeMeasurements:
            if toCalculate[size] != None:
                pass

calculateMeasurements(example_measurements)

###


