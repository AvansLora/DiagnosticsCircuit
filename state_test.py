from state import State, StateManager
from random import randint
import time

class Idle(State):
	def __init__(self):
		State.__init__(self, "idle")

	def init(self):
		self.number = randint(0,15)
		time.sleep(1);

	def run(self, manager):
		print manager.getGoodRun()
		print self.toString()
		print self.number
		if (self.number <= 5):
			manager.setNextState("s1")
		elif (self.number > 5 and self.number <= 10):
			manager.setNextState("s2")
		elif (self.number > 10 and self.number <= 15):
			manager.setNextState("s3")

class MarginState(State):
	def __init__(self, name, margin):
		State.__init__(self, name)
		self.margin = margin

	def run(self, manager):
		self.toString()
		manager.setNextState("idle")
		
	def toString(self):
		return super(MarginState, self).toString()+" ["+self.margin+"]"

class s1(MarginState):
	def __init__(self):
		MarginState.__init__(self, "s1", "0-5")

class s2(MarginState):
	def __init__(self):
		MarginState.__init__(self, "s2", "5-10")

class s3(MarginState):
	def __init__(self):
		MarginState.__init__(self, "s3", "10-15")

sm = StateManager()
idle = Idle()

sm.addState(idle);
sm.addState(s1());
sm.addState(s2());
sm.addState(s3());

sm.start(idle);


