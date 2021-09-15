from apscheduler.schedulers.background import BackgroundScheduler
import time
from multiprocessing import Queue

class Person():
	def __init__(self):
		self.number = 3

def testf(a):
	print('hello')
	a.number = 8

y=Person()
print(y.number)
x= Queue()
scheduler = BackgroundScheduler()
job = scheduler.add_job(testf, 'interval',args=[y], seconds=1)
i = 0
scheduler.start()

while True:
	i = i+1
	time.sleep(3)
	if i >= 1:
		break

print(y.number)
job.remove()
