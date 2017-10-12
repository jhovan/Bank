#Gallardo Valdez Jose Jhovan
#19/09/2016
#Bank queue simulation

from random import randint
import time

#class person that represents a customer
class Person:

	#construnctor method that receives an ID and creates a person whose transaction 
	#takes a random number of minutes between 1 and 15
	def __init__(self,id):
		self.id=id
		#number of minutes that the transation takes to complete
		self.time=randint(1,15)
		#it's 0 if the customer it's waiting in the line
		self.state=0
		self.paydesk=None

	#to string method
	def __str__(self):
		return "person" + str(self.id)

	#set a paydesk for the customers
	def set(self,paydesk):
		self.paydesk=paydesk
		self.state=1

	#decrements the time that the person needs to be in the bank
	def dec(self):
		self.time-=1

	#returns true when the person finishes his transaction
	def ready(self):
		return self.time<=0

#class paydeks that represents a paydesk in the bank
class paydesk:

	#constructor method that receives an id
	def __init__(self,id):
		self.id=id
		self.person=None

	#set a person to the paydesk
	def set(self,person):
		self.person=person

	#returns true if there is nobody in the paydeks
	def empty(self):
		if self.person==None:
			return True
		else:
			return False

	#empty the paydesk
	def setempty(self):
		self.person=None

	#to string method
	def __str__(self):
		return "paydesk" + str(self.id)

#class clock that represents the current time
class Clock:

	#constructor method that that receives a initial time
	def __init__(self, hours, minutes):
		self.hours=hours
		self.minutes=minutes

	#to string method
	def __str__(self):
		return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2)

	#increases the time by a certain number of minutes
	def inc(self,minutes):
		self.minutes+=minutes
		self.hours+=self.minutes/60
		self.minutes=self.minutes%60
		self.hours=self.hours%24

#initializes the clock at 12:00 
clock=Clock(12,0)

#initializes the list of customeres
customers=[]

#initializes the 3 paydesks
paydesk1=paydesk(1)
paydesk2=paydesk(2)
paydesk3=paydesk(3)

#counts every second that pass by
counter=0

#while there are customers or it's before 13:30 (91 minutes after 12:00) the program runs
while customers or counter in range(91):
	#prints the time
	print str(clock)+ "->"
	#every two minutes a new customer arrives
	if counter%2==0 and counter in range(91):
		customers.append(Person(counter/2 + 1))
	#list that stores the customers who finish their transaction
	delete=[]
	#determine the behavior of each customer in the bank
	for y in customers:
		#if the customer is at a paydesk then the transaction time decreases
		#if not, and there is an empty paydesk the customer go to the paydesk
		if y.state==1:
			y.dec()
			if y.ready():
				print str(y) + " leaves  " + str(y.paydesk)
				y.paydesk.setempty()
				delete.append(y)
			else:
				print str(y) + " in " + str(y.paydesk) 
		else:
			if paydesk1.empty():
				paydesk1.set(y)
				y.set(paydesk1)
				print str(y) + " go to paydesk " + str(paydesk1) + ", transaction:" + str(y.time) + " minutes"
			elif(paydesk2.empty()):
				paydesk2.set(y)
				y.set(paydesk2)
				print str(y) + " go to paydesk " + str(paydesk2) + ", transaction:" + str(y.time) + " minutes"
			elif(paydesk3.empty()):
				paydesk3.set(y)
				y.set(paydesk3)
				print str(y) + " go to paydesk " + str(paydesk3) + ", transaction:" + str(y.time) + " minutes"
			else:
				print str(y) + " waiting" + ", transaction:" + str(y.time) + " minutes"
	#removes the customers that left the bank from the customers list 
	for y in delete:
		customers.remove(y)
	#one minute pass by every second in real life
	counter+=1
	clock.inc(1)
	time.sleep(1) 