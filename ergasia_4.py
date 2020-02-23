#εργασια 4
def isItPrime(x):    
    found=0
    i=2
    while i<=x//2 and found==0:
        if x%i==0:
            found=1
        i+=1   
    return found
#ARXH_PROGRAMMATOS
mystr=''
x = str(input("Δώστε μία αλφαριθμητική τιμή "))
for i in range(len(x)):
    mystr = mystr +  str(ord(x[i]))

isIt = isItPrime(int(mystr))
if isIt==0:
    print("Πρώτος")
else:
    print("Δέν είναι πρώτος")
#TELOS_PROGRAMATOS

