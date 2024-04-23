s="abin"
t="nibe"
count=0
for i in s:
    for j in t:
        if i==j:
            count+=1
            break
if count == len(s):
    print("true")
else:
    print("false")

