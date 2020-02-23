#εργασια 5
#ARXH_PROGRAMMATOS
mystr=''
words=[]
with open('test.txt', 'r',encoding="utf8") as f:
    for line in f:
        words = line.split( )
        for i in range(len(words)):
            if words[i].strip()!='.' and words[i].strip()!=',':
                if '.' in words[i] or ',' in words[i]:
                    st=words[i]
                    if ',' in words[i]:
                        st=st.split(',')
                    else:
                        st=st.split('.')

                    for g in range(len(st)):
                        if len(st[g])>3:
                            newmystr=''
                            mystr=st[g]
                            for k in range(1,len(mystr)):
                                newmystr +=mystr[k]
                            newmystr = newmystr + 'ay' + mystr[0] 
                            print(newmystr)
                else:                    
                    if len(words[i])>3:
                        newmystr=''
                        mystr=words[i]
                        for k in range(1,len(mystr)):
                            newmystr +=mystr[k]
                        newmystr = newmystr + 'ay' + mystr[0] 
                        print(newmystr)
#TELOS_PROGRAMMATOS

 
