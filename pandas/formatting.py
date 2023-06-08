# -------------format

"""Performs a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument."""

# Example 1
print("{} and {}".format("Tea", "Coffee"))

# Example 2
print("{1} and {0}".format("Tea", "Coffee"))

# Example 3
print("{lunch} and {dinner}".format(lunch="Peas", dinner="Beans"))

# Example 4
print("{0}, {1}, {2}".format(*"123"))

# Example 5
lunch = {"food": "Pizza", "drink": "Wine"}
print("Lunch: {food}, {drink}".format(**lunch))


print("Pi is approximately {0:12}".format(22/7))

print("Pi is approximately {0:12f}".format(22/7))

print("Pi is approximately {0:12.50f}".format(22/7))

print("Pi is approximately {0:<52.50f}".format(22/7))

print("Pi is approximately {0:<62.50f}".format(22/7))

print("Pi is approximately {0:<72.54f}".format(22/7))

for i in range(1,13):
    print("No. {:<2} squared is {:<3} and cube is {:<4}".format(i,i**2,i**3))