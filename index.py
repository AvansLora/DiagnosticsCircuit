from state import State, StateManager
import time, json
import api
import Adafruit_DHT
import os
import store

defaultMeasureValue = -50

class Idle(State):
    def __init__(self):
        State.__init__(self, "idle")

    def run(self, manager):
        if not manager.getSkipNext():
            time.sleep(60*60/2)
        manager.setNextState("measure")


class Measure(State):
    def __init__(self):
        State.__init__(self, "measure")
        self.cpuTemp = defaultMeasureValue
        self.temp = defaultMeasureValue
        self.hum = defaultMeasureValue

    def init(self):
        self.cpuTemp = defaultMeasureValue
        self.temp = defaultMeasureValue
        self.hum = defaultMeasureValue
        return

    def run(self, manager):
        # @TODO add validation for the values
        self.hum, self.temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        self.getcputemp()

        package = {
            "token": store.getToken(),
            "cputemp": round(float(self.cpuTemp),2),
            "casetemp": round(self.temp,2),
            "humidity": round(self.hum,2)
        }

        r = api.sendPackage(package)

        if r is not None and (r.status_code == 401 or r.status_code == 403):
            manager.setNextState("auth")

        manager.setNextState("idle")
        return

    def getcputemp(self):
        res = os.popen('vcgencmd measure_temp').readline()
        self.cpuTemp = res.replace("temp=", "").replace("'C\n", "")
        return



class Auth(State):
    def __init__(self):
        State.__init__(self, "auth")

    def run(self, manager):
        r = api.authenticate()
        if r is not None and r.status_code == 200:
            data = json.loads(r.text)
            token = data["token"]
            store.setToken(token)

        manager.setNextState("idle")
        return False


sm = StateManager()
start = Idle()

sm.addState(start)
sm.addState(Measure())
sm.addState(Auth())

sm.start(start)
