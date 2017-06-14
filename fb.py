#!/usr/bin/env python
class FizzBuzz:

	def myawesomescript(self):

		for x in range (0,100):
			if (x%3==0):
				if ((x%3==0) & (x%5==0)):
					print("FizzBuzz")
				else:
					print("Fizz")
			elif (x%5==0):
				if ((x%3==0) & (x%5==0)):
					print("FizzBuzz")
				else:
					print("Buzz")
			else:
				print(x)

if __name__ == '__main__':
	print("Running as a script...")
	fb = FizzBuzz()
	fb.myawesomescript()