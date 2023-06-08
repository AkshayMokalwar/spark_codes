# # ----------capitalize
# #Returns a copy of the string with its first character capitalized and the rest lowercased.
# a = "bee sting" 
# print(a.capitalize())

# # ----------center
# #Returns the string centered in a string of length width. Padding can be done using the specified fillchar (the default padding uses an ASCII space). The original string is returned if width is less than or equal to len(s)
# a = "bee" 
# b = a.center(50, "-")
# print(b)

## -------------count
# #Returns the number of non-overlapping occurrences of substring (sub) in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

##Non-overlapping occurrences means that Python won't double up on characters that have already been counted. For example, using a substring of xxx against xxxx returns 1.

# a = "Mushroooom soup" 
# print(a.count("O"))
# print(a.count("o"))
# print(a.count("oo"))
# print(a.count("ooo"))
# print(a.count("Homer"))
# print(a.count("o", 4, 7))
# print(a.count("o", 7))

# ------------------encode
"""Returns an encoded version of the string as a bytes object. The default encoding is utf-8. errors may be given to set a different error handling scheme. The possible value for errors are:

strict (encoding errors raise a UnicodeError)
ignore
replace
xmlcharrefreplace
backslashreplace
any other name registered via codecs.register_error()"""

# from base64 import b64encode

# a = "Banana"
# print(a)

# a = b64encode(a.encode())
# print(a)

# -----------------expandtabs
"""Returns a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every tabsize characters (the default is 8, giving tab positions at columns 0, 8, 16 and so on)."""

# a = "1\t2\t3"
# print(a)
# print(a.expandtabs())
# print(a.expandtabs(tabsize=12))
# print(a.expandtabs(tabsize=2))


# ----------------find
"""Returns the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Returns -1 if sub is not found.

The find() method should only be used if you need to know the position of the substring. If you don't need to know its position (i.e. you only need to know if the substring exists in the string), use the in operator. See string operators for an example of in."""

# a = "Fitness"
# print(a.find("F"))
# print(a.find("f"))
# print(a.find("n"))
# print(a.find("ness"))
# print(a.find("ess"))
# print(a.find("z"))
# print(a.find("Homer"))


# ------------format_map
"""Similar to format(**mapping), except that mapping is used directly and not copied to a dictionary. This is useful if for example mapping is a dict subclass."""


# # Example 1
# lunch = {"Food": "Pizza", "Drink": "Wine"}
# print("Lunch: {Food}, {Drink}".format_map(lunch))

# # Example 2
# class Default(dict):
#     def __missing__(self, key):
#       return key

# lunch = {"Food": "Pizza"}
# print("Lunch: {Food}, {Drink}".format_map(Default(lunch)))

# lunch = {"Drink": "Wine"}
# print("Lunch: {Food}, {Drink}".format_map(Default(lunch)))


# ------------index
"""Like find() (above), but raises a ValueError when the substring is not found (find() returns -1 when the substring isn't found)."""

# a = "Fitness"
# print(a.index("F"))
# print(a.index("n"))
# print(a.index("ness"))
# print(a.index("ess"))
# print(a.index("z"))   #Error


# ---------------isalnum
"""Returns True if all characters in the string are alphanumeric and there is at least one character. Returns False otherwise.

A character c is deemed to be alphanumeric if one of the following returns True:

c.isalpha()
c.isdecimal()
c.isdigit()
c.isnumeric()"""

# c = "Fitness"
# print(c.isalnum())

# c = "123"
# print(c.isalnum())

# c = "1.23"
# print(c.isalnum())

# c = "$*%!!!"
# print(c.isalnum())

# c = "0.34j"
# print(c.isalnum())

#------------isidentifier

"""Returns true if the string is a valid identifier according to the language definition, section Identifiers and keywords from the Python docs."""

# a = "123"
# print(a.isidentifier())

# a = "_user_123"
# print(a.isidentifier())

# a = "_user-123"
# print(a.isidentifier())

# a = "Homer"
# print(a.isidentifier())

# a = "for"
# print(a.isidentifier())

# ------islower()

"""Returns True if all cased characters in the string are lowercase and there is at least one cased character. Returns False otherwise."""

# a = " "
# print(a.islower())

# a = "123"
# print(a.islower())

# a = "_user_123"
# print(a.islower())

# a = "Homer"
# print(a.islower())

# a = "HOMER"
# print(a.islower())

# a = "homer"
# print(a.islower())

# a = "HOMER"
# a = a.casefold() #Force lowercase
# print(a.islower())
