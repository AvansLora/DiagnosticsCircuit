class StateManager(object):
    def __init__(self):
        self.states = []
        self.currentState = None
        self.goodRun = True

    def addState(self, state):
        self.states.extend([state])

    def setNextState(self, nextState):
        # print "setting next state"
        # print nextState
        if nextState:
            self.currentState = nextState

    def start(self, startState):
        if (startState):
            self.setNextState(startState.getName())
            while True:
                if self.currentState:
                    nextState = self.getNextState()
                    # print "next state"
                    # print nextState
                    if nextState:
                        # print "state"
                        # print nextState.toString()
                        # print "init"
                        nextState.init()
                        # print "run"
                        wasdoodrun = nextState.run(self)
                        if wasdoodrun is None:
                            self.goodRun = True
                        else:
                            self.goodRun = wasdoodrun
                    else:
                        self.setNextState(startState.getName())
                else:
                    self.setNextState(startState.getName())

    def getNextState(self):
        for x in self.states:
            # print "state: "+x.toString()
            # print "currentstate: "+self.currentState
            name = x.getName()
            # print "name: "+name
            if name == self.currentState:
                # print "found state"
                # print x
                return x
        return None
    def getGoodRun(self):
        return self.goodRun;

    def toString(self):
        print "Statemanager"
        print len(self.states);
        for x in self.states: print x


class State(object):
    def __init__(self, state):
        self.name = state

    def init(self):
        return "init: " + self.toString()

    def run(self, manager):
        return "run:  " + self.toString()

    def getName(self):
        return self.name

    def toString(self):
        return self.name
