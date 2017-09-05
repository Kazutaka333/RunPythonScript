# const
extention = ".swift"


def extractName(jsonName):
    return jsonName.split(".")[0]

# file name
def createStateFileNameFrom(jsonName):
    return extractName(jsonName) + "State" + extention

def createReducerFileNameFrom(jsonName):
    return extractName(jsonName) + "StateReducer" + extention

def createActionFileNameFrom(jsonName):
    return extractName(jsonName) + "StateAction" + extention

# get all json files
jsonPath = "Stamp.json"

# for loop all the json files
fileName =
jsonFile = open()

# reducer

# state

# action

