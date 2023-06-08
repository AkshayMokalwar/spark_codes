word="Norwegian Blue"

# print(word[0:9])    # the string is from 0  upto the 9 but not including the 9
# print(word[:9])
# print(word[10:14])
# print(word[10:])
# print(word[:])

# ---------slicing with Negative 

# print( word[-4:-2:])

# print( word[-4:12:])

# ----------Steps in slicing

# print(word[0:6:2])
# print(word[0:6:3])

# numbers="9;254,152'654 544:547;578"
# seperators=numbers[1::4]
# print()

# value = "".join(char if char not in seperators else " " for char in numbers).split()
# print([int(val) for val in value])


# -----------------Reverse Slicing
# in negative steps , the start value should always greater than end value 
letters= "abcdefghijklmnopqrstuvwxyz"
# print(letters[25::-1])
# print(letters[::-1])#it is the reverse of the string


# # solution
# print(letters[16:13:-1])
# print(letters[4::-1])
# print(letters[:-9:-1])

# idioms
# first letter of string using slicing

print(letters[:1])

print(letters[0])# gives error when string is empty 

# last letter of string using slicing 
print(letters[-1:])



# difference between slicing and indexing is index gives error for empty string