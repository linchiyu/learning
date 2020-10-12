from __future__ import with_statement

class MyC():
	def __init__(self):
		#called when the object is created x = ObjectClass()
		print('init')

	def __enter__ (self):
		#called when used in 'with as' statement
		print('enter')

	def __exit__(self, exc_type, exc_val, exc_tb):
		#called after the end of the 'with as' statement
		print('exit')
		print(exc_type, exc_val, exc_tb)


with MyC() as a:
	print('b')

a = MyC()
a.__enter__()
a.__exit__(None,None,None)
