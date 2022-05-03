s = "IX"
roman={"IV":4,"IX":9,"I":1,"V":5,"X":10}
sum=0
j=0
for i in range(len(s)):
    i=j
    if i>=len(s):
        break
    elif i == len(s)-1:
        sum+=roman[s[i]]
        break
    elif s[i:i+2] in roman:
        sum += roman[s[i:i+2]]
        j+=2
    else:
        sum+= roman[s[i]]
        j+=1
print(sum)