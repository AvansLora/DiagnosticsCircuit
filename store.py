import json

store = {
    "token": ""
}

with open('settings.json') as data_file:
    store["settings"] = json.load(data_file)


def init():
    store["hardwareId"] = getSerial()
    return


def getSettings():
    settings = store["settings"]
    return settings


def getHardwareId():
    hardwareId = store["hardwareId"]
    return hardwareId


def setToken(token):
    store["token"] = token
    return


def getToken():
    token = store["token"]
    return token


def getSerial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial
