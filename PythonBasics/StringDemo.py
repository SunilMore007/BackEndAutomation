str = "SunilMore.Kavalapur"
str1 = "Amar More"
str2 = "SunilMore"

print(str[1])  # u
print(str[0:5])  # Sunil
print(str + str1)  # concatination
print(str2 in str)  # Substring Check # True

newString = str.split(".")
print(newString)  # ['SunilMore', 'Kavalapur']
print(newString[0])  # SunilMore

str3 = " Good "         # to trim the whitespaces
print(str3.strip())        #Good
print(str3.lstrip())       #Good #leftTrim
print(str3.rstrip())       # Good  #RightTrim
