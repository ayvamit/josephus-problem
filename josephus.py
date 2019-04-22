n = int(input())
pos= int(input())
l=list()
for i in range(n):
    l.append(i)
i=0
if pos<n:
    while i<n:
        print("start")
        print(l,pos)
        if pos<len(l)-1:
            pos=pos+1
            l.pop(pos) 
        elif pos==len(l):
            pos=1
            l.pop(pos)
            pos=1
        elif pos<=len(l)-1:
            pos=0
            l.pop(pos)
            pos=0
       
        if len(l)==1:
            break
        print("end")
        print (i,l,pos)    
        i=i+1
print ("Result: ")   
print(l)  
