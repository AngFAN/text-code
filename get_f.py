apple = input("How many apples do you got?\n")
try:
	apple = int(apple)
except:
	print ("\33[41m[error]\33[0m",apple,"NaN")
else:
	print(f"You got {apple} apples")

banana = input("How many bananas do you got?\n")
try:
	banana = int(banana)
except:
	print("\33[41m[error]\33[0m",banana,"NaN")
else:
	print(f"You got {banana} bananas")
