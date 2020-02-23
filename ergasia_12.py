#εργασια 12
import datetime
from datetime import date
#Συναρτηση για να δωθει σωστη ημεερομηνια.
def GetValidDate():
    isValid=False
    while not isValid:
        userIn = input("Δώστε ημερομηνία στη μορφή ΗΗ/ΜΜ/ΕΕΕΕ: ")
        try: 
            d = datetime.datetime.strptime(userIn, "%d/%m/%Y")
            isValid=True
        except:
            print ("Λάθος, προσπαθήστε ξανά!\n")
    return d

#πόσες ημέρες έχει ο μήνας;
def GetValidDays(etos,minas):
    if minas == 1 or minas == 3 or minas == 5 or minas == 7 or minas == 8 or minas == 10 or minas == 12:
        itIs = 31
    elif minas == 4 or minas == 6 or minas == 9 or minas == 11:    
        itIs = 30
    elif minas == 2:
        #Αν το ετος ειναι δισεκτο τοτε ο φεβρουαριος εχει 29 ημερες.
        if ((etos % 4 ==0) and (etos % 100 !=0)) or (etos % 400 == 0):
            itIs = 29
        else:    
            itIs = 28

    return itIs
#ARXH_PROGRAMMATOS
d=GetValidDate()
y1 = GetValidDays(d.year,d.month)

today = datetime.date.today()
d1 = today.strftime("%d")
d2 = today.strftime("%m")
d3 = today.strftime("%Y")
f_date = date(d.year,d.month,d.day)
l_date = date(int(d3),int(d2),int(d1))
delta = l_date - f_date
days = delta.days
hours = days*24
sec = hours*3.600
print ("\n")
print ("Απέχει απο την τρέχουσα ημερομηνία :",str(days) + " μέρες / " + str(hours) + " ώρες / " + str(sec) + " δευτερόλεπτα")
print ("\n")
print ("ο μήνας της ημερομηνίας που δώσατε έχει ",y1,"μέρες")
#TELOS_PROGRAMMATOS
