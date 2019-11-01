def helloworld(x):
	print(x)
helloworld("Hello World")

def name(y):
	print("\nMy name is", y, ".")
	def age():
		print("I am 20+ years of age. Young, right? \U0001f600")
	age()
name("Stan")

sum = 0
lst = [12, 4, 56, 17, 8, 99]
for num in lst:
	sum = sum + num
	mean = sum / len(lst)
print("\nThe maximum number in this list:  [12, 4, 56, 17, 8, 99] is", max(lst), ".")
print("The mean: [12, 4, 56, 17, 8, 99] is", mean)

print("\nA for Apple\nB for Boy\nC for Cow\n...\nZ for Zebra")
