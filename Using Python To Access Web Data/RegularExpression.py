import re
fhand=open('regex_sum_887499.txt')

sum=0
for lines in fhand:
    y=re.findall('[0-9]+',lines)
    if(len(y)>=1):
        for i in range(len(y)):
            sum+=int(y[i])
print(sum)