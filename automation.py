import os

while True:
	X = os.popen("python3 process.py").read()
	#X = X.split('\n')
	print(X)