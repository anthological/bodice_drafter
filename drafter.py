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
    print(form)
    formIndex = allForms.index(form)
    dfCol = [formIndex+1]



### user stuff

class user:
    def __init__(self, name, fittings = []): #user, string, list of fittings
        self.name = name
        self.initialized = date.today()
        self.fittings = []
        self.fittings = self.sortFittings(self)
        self.measurements = self.fittings[0]

    def sortFittings(self): #list of fittings
        sortedFittings = copy.deepcopy(self.fittings)
        #do i need to make fitting IDs?
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


def calculateMeasurements(measures): #measures is a dictionary
    toCalculate = []
    for key in measures:
        if measures[key] == None:
            toCalculate.append(key)
    for key in toCalculate:
        if key in requiredMeasurements:
            measures[key] = interpolateMeasurement(measures, key) #returns None



def interpolateMeasurements(measures, key, knownSize = None):
    toCalculate = []
    if knownSize != None:
        sizeMeasurements = allSizes[knownSize]
        for size in sizeMeasurements:
            if toCalculate[size] != None:
                pass

calculateMeasurements(example_measurements)

### just get on with it

def calculateMeasurementsHelper(measures, height = 66)
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
    measures = measures['armhole']
    #calculate the rest
    front_neck = neck/6 + 0.25
    back_neck = neck/6 + 0.375
    figure_breadth = figure_breadth/2
    cross_front = cross_front/2
    cross_back = cross_back/2
    front_bust = bust/4 + 0.25
    back_bust = bust/4 - 0.25
    cup_size = rounded(bust - underbust - 4.5)
    front_waist = waist/4 + 0.25
    back_waist = waist/4 - 0.25
    front_armhole = armhole/2 - 0.25
    back_armhole = armhole/2 + 0.25
    if front_length > back_length:
        front_armhole += 0.5
        back_armhole -= 0.5
    if height <= 64:
        waist_height = 8
        HH_height = 4
    elif height >= 70:
        waist_height = 9
        HH_height = 4
    else:
        waist_height = 8.5
        HH_height = 4
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
    out = dict()
    #for measure in allMeasures:
    #    out[measure] =
    return out


###









