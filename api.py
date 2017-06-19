import json
import store
import requests


def buildUrl(path):
    settings = store.getSettings()
    url = "http://{0}:{1}/{2}{3}".format(settings["url"], settings["port"], settings["prefix"], path)
    return url


# Default requests
def PostRequest(path, payload):
    url = buildUrl(path)
    # print "Sending post request to webserver"
    # print url

    # print "payload"
    # print payload

    # print 'testing requests'
    # print "payload"
    # print payload
    try:
        r = requests.post(url, data=payload, timeout=5)
        return r
    except requests.exceptions.ConnectionError as e:
        print e


# State requests
def authenticate():
    path = "/authenticate"
    settings = store.getSettings()
    data = {
        "username": settings["username"],
        "password": settings["password"]
    }
    return PostRequest(path, data)


def sendPackage(package):
    path = "/addmeasurement"
    return PostRequest(path, package)
