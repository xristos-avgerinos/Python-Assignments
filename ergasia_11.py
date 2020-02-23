#εργασια 11
#ARXH_PROGRAMMATOS
import math
words=[]
neww=[]
mynums=[]
with open('test_nums.txt', 'r',encoding="utf8") as f:
    for line in f:
        words = line.split(',')
        for i in range(len(words)):
            neww= words[i].split()
            for k in range(len(neww)):
                mynums.append(int(neww[k]))
a=[]
for i in range(6):
    a.append(input('Δώστε ' + str(i+1) + ' αριθμό:'))
    
found2 = 0
l=[]
for i in range(6-3):
    for j in range(i+1,6-2):
        for k in range(j+1,6-1):
            for r in range(k+1,6):
                
                c=0
                q=0
                found=1
                x=0
                while x<len(mynums):
                    
                    if int(a[i])==mynums[4*q+0] or int(a[i])==mynums[4*q+1] or int(a[i])==mynums[4*q+2] or int(a[i])==mynums[4*q+3]:
                        c+=1
                    if int(a[j])==mynums[4*q+0] or int(a[j])==mynums[4*q+1] or int(a[j])==mynums[4*q+2] or int(a[j])==mynums[4*q+3]:
                        c+=1
                    if int(a[k])==mynums[4*q+0] or int(a[k])==mynums[4*q+1] or int(a[k])==mynums[4*q+2] or int(a[k])==mynums[4*q+3]:
                        c+=1
                    if int(a[r])==mynums[4*q+0] or int(a[r])==mynums[4*q+1] or int(a[r])==mynums[4*q+2] or int(a[r])==mynums[4*q+3]:
                        c+=1

                    if c==4:
                        found=0
                        c=0
                    else:
                        c=0
                        
                    q+=1
                    x+=4
                    
                if found==1:
                    l.append(int(a[i]))
                    l.append(int(a[j]))
                    l.append(int(a[k]))
                    l.append(int(a[r]))  
                    found2 = 1     
                    

if found2==0:
    print('Δεν βρέθηκε διαθέσιμη τετράδα!')
else:
    print('Βρέθηκε η  διαθέσιμη τετράδα:',str(l[0]) + ' ' + str(l[1]) + ' ' +  str(l[2])  + ' ' +  str(l[3]))
#TELOS_PROGRAMMATOS
