str1 = 'abc'
str2 = 'aktcopb'
str3 = ""

count = 0
for char1 in str1:
    for char2 in str2:
        if char1 == char2:
            str3 += char2
            count += 1
            break

if count == len(str1) and str1 == str3:
    print("true")
else:
    print("false")
