import process
try:
	total = str(process.total)
	print(f"You got {total} fruits!")
	print("You got {} fruits!".format(total))
	print("You got " + str(total) + " fruits!")
except Exception as e:
	print("\33[41m[error]\33[0mFail in getting total")
