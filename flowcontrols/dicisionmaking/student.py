m1=int(input("mark of s1:"))
m2=int(input("mark of s2:"))
m3=int(input("mark of s3:"))
total=m1+m2+m3
print("total is",total)
if(total>145):
    print("A+")
elif((total>=140)&(total<=145)):
    print("A")
elif((total>=135) & (total<=140)):
    print("B+")
elif((total>=130) & (total<=135)):
    print("B")
else:
    print("fail")


