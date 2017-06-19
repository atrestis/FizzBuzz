#!/usr/bin/env python
import time
class FizzBuzz:

	def myawesomescript(self):

		for x in range (0,100):
			if (x%3==0):
				if ((x%3==0) & (x%5==0)):
					print("FizzBuzz")
					time.sleep(1)
				else:
					print("Fizz")
					time.sleep(1)
			elif (x%5==0):
				if ((x%3==0) & (x%5==0)):
					print("FizzBuzz")
				else:
					print("Buzz")
					time.sleep(1)
			else:
				print(x)
				time.sleep(1)

if __name__ == '__main__':
	print("Running as a script...")
	time.sleep(0.5)
	fb = FizzBuzz()
	fb.myawesomescript()
