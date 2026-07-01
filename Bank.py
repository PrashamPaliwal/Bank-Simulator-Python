def bank (b,n,a,p,c,bp):
    if bp==123:
        f=open(f"{b}.txt",'a')
        f.write(f'\n{a},{p}')
        f.close()
        aca=f'{a}.txt'
        err=1
        while err==1:
            y=int(input('enter year in (****) format = ',))
            m=int(input('enter month in (**) format = ',)) 
            d=int(input('enter day in (**) format = ',))
            if y>=1000 and m>0 and d>0 and m<=12 and d<=31 and y<=9999:
                if m==2 and y%4==0 and d<=29:
                    if y%100==0:
                        if y%400==0:
                            da=f'{y}-{m}-{d}'
                            err=0
                        elif d<=28:
                            da=f'{y}-{m}-{d}'
                            err=0
                elif m==2 and y%4!=0 and d<=28:
                    da=f'{y}-{m}-{d}'
                    err=0
                elif m!=2 :
                    da=f'{y}-{m}-{d}'
                    err=0
            elif err==1:
                print('no date selected due to wrong input try again')
        g=open(f'{b}/{aca}','a')
        g.write(f'\n{n} = name\n{da} = DOB\n{c} = balance')
        g.close()
        print('account created successfully')
    else :
        print('bank pin wrong account can be created by bank employe only')
def check_balance (b,a,p):
    z=0
    f=open(f'{b}.txt','r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data=i.strip(',\n').split(',')
        if data[0]==a and data[1]==p:
            aca=f'{a}.txt'
            g=open(f'{b}/{aca}','r')
            print(g.read())
            g.close()
            z=1
    if z==0:
        print('account number or password wrong')
def deposite (b,a,p,c):
    z=0
    aca=f'{a}.txt'
    f=open(f"{b}.txt",'r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data=i.strip(",\n").split(',')
        if data[0]==a and data[1]==p:
            g=open(f"{b}/{aca}",'r')
            fd=g.readlines()
            g.close()
            g=open(f"{b}/{aca}",'w')
            r=''
            for j in fd:
                if j.endswith('balance'):
                    y=0
                    for x in j:
                        if x.isdigit():
                            y+=1
                        elif x=='.':
                            y+=1
                        else :
                            break
                    for q in range (0,y):
                        r+=j[q]
                    r=float(r)
                    c+=r
                    j=f'{c} = balance'
                    print(j)
                    g.write(j)
                else:
                    g.write(j)
            g.close()
            z=1
    if z==0:
        print('account number or password wrong')
def withdraw (b,a,p,c):
    z=0
    aca=f'{a}.txt'
    f=open(f'{b}.txt','r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data = i.strip(',\n').split(',')
        if data[0]==a and data[1]==p:
            r=''
            g=open(f'{b}/{aca}','r')
            fd=g.readlines()
            g.close()
            g=open(f'{b}/{aca}','w')
            for j in fd:
                if j.endswith('balance'):
                    y=0
                    for x in j:
                        if x.isdigit():
                            y+=1
                        elif x=='.':
                            y+=1
                        else :
                            break
                    for q in range (0,y):
                        r+=j[q]
                    r=float(r)
                    if r>=c:
                        r-=c
                        j=f'{r} = balance'
                        print(j)
                    else :
                        print('not enough balance')
                    g.write(j)
                else:
                    g.write(j)
            g.close()
            z=1
    if z==0:
        print('account number or password wrong')
def transfer (b1,b2,a1,a2,p1,c):
    z1=0
    z2=0
    a2=str(a2)
    aca1=f'{a1}.txt'
    aca2=f'{a2}.txt'
    f1=open(f'{b1}.txt','r')
    sd=f1.readlines()
    f1.close()
    f2=open(f'{b2}.txt','r')
    rd=f2.readlines()
    f2.close()
    for i in sd :
        data1 = i.strip(',\n').split(',')
        if data1[0]==a1 and data1[1]==p1:
            z1=1
            break
    if z1==0:
        print('your account number or pin is wrong ')
        return False
    for j in rd:
        if j.startswith(a2):
            z2=1
            break
    if z2==0:
        print('recievers account number not found')
        return False
    g1=open(f'{b1}/{aca1}','r')
    g2=open(f'{b2}/{aca2}','r')
    d1 = g1.readlines()
    d2 = g2.readlines()
    g1.close()
    g2.close()
    g1=open(f'{b1}/{aca1}','w')
    g2=open(f'{b2}/{aca2}','w')
    for u1 in d1:
        if u1.endswith('balance'):
            y=0
            c1=''
            for x1 in u1:
                if x1.isdigit():
                    y+=1
                elif x1=='.':
                    y+=1
                else:
                    break
            for t in range (0,y):
                c1+=u1[t]
            c1=float(c1)
            if c1>c:
                c1-=c
                g1.write(f'{c1} = balance')
                print (f'payment success full of rupess {c}')
            else:
                g1.write(u1)
                print('payment failed not enough balance')
                return False
        else:
            g1.write(u1)
    for u2 in d2:
        if u2.endswith('balance'):
            y=0
            c2=''
            for x2 in u2:
                if x2.isdigit():
                    y+=1
                elif x2=='.':
                    y+=1
                else:
                    break
            for t in range (0,y):
                c2+=u2[t]
            c2=float(c2)
            c2+=c
            g2.write(f'{c2} = balance')
        else :
            g2.write(u2)
    g1.close()
    g2.close()
def update_pin (b,a,p1,p2):
    z=0
    f=open(f'{b}.txt','r')
    ud=f.readlines()
    f.close()
    f=open(f'{b}.txt','w')
    for i in ud :
        data = i.strip(',\n').split(',')
        if data[0]==a and data[1]==p1:
            f.write(f'{a},{p2}\n')
            z=1
        else:
            f.write(i)
    f.close()
    if z==0:
        print('account number or pin is incorrect')
    else:
        print('pin updated successfully')
def update (b,a,p,wd,nd):
    z=0   
    aca=f'{a}.txt'
    f=open(f"{b}.txt",'r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data = i.strip(',\n').split(',')
        if data[0]==a and data[1]==p:
            g=open(f'{b}/{aca}','r')
            dud=g.readlines()
            g.close()
            g=open(f'{b}/{aca}','w')
            for j in dud:
                if j.strip('\n').endswith(wd):
                    g.write(f'{nd} = {wd}\n')
                    z=1
                    print(f'{wd} changed successfully')
                else:
                    g.write(j)
            g.close()
    if z==0:
        print('incorrect account number or pin')
def main ():
    x=0
    bn=0
    y=0
    bn=int(input('type 1 for hdfc bank, type 2 axis bank, type 3 for sbi, type 4 to end interraction = ',))
    if bn==1:
        b='HDFC'
    elif bn==2:
        b='AXIS'
    elif bn==3:
        b='SBI'
    else:
        print('invalid input')
        return False
    while x!=3:
        print('type 1 to create account\ntype 2 to login\ntype 3 to exit')
        x=int(input())
        if x==1:
            bank(b,str(input('enter your name = ',)),int(input('enter acc number = ',)),int(input('enter your pin = ',)),float(input('enter balance = ',)),int(input('enter bank pin = ',)))
        elif x==2:
            a,p=int(input('enter your account number = ',)),int(input('enter pin = ',))
            a,p=str(a),str(p)
            Av=0
            f=open(f"{b}.txt",'r')
            ud=f.readlines()
            f.close()
            for i in ud:
                data=i.strip(',\n').split(',')
                if data[0]==a and data[1]==p:
                    Av=1
            if Av==1:
                while y!=8:
                    print('type 1 to check balance in your account\ntype 2 to deposite money in your account\ntype 3 to withdraw ammount from your account\ntype 4 to tranfer money from one accoungt to another\ntype 5 to update pin\ntype 6 to update name\ntype 7 to logout')
                    y=int(input())
                    if y==1:
                        check_balance(b,a,p)
                    elif y==2:
                        deposite(b,a,p,float(input('enter ammount to deposite = ',)))
                    elif y==3:
                        withdraw(b,a,p,float(input('enter ammount to withdraw = ',)))
                    elif y==4:
                        bn=int(input('type 1 for hdfc bank, type 2 axis bank, type 3 for sbi = ',))
                        if bn==1:
                            b2='HDFC'
                            transfer(b,b2,a,int(input('enter account number of reciever = ',)),p,float(input('amount to transfer = ',)))
                        elif bn==2:
                            b2='AXIS'
                            transfer(b,b2,a,int(input('enter account number of reciever = ',)),p,float(input('amount to transfer = ',)))
                        elif bn==3:
                            b2='SBI'
                            transfer(b,b2,a,int(input('enter account number of reciever = ',)),p,float(input('amount to transfer = ',)))
                        else:
                            print('wrong input try again')
                    elif y==5:
                        update_pin(b,a,p,int(input('enter your new pin = ',)))
                    elif y==6:
                        update(b,a,p,'name',str(input('enter your new name = ',)))
                    elif y==7:
                        print('thankyou')
                    else :
                        print('wrong input try again')
            else :
                print('incorrect acc number or pin')
        elif x==3:
            print()
        else:
            print('incorrect input')
def bank (b,n,a,p,c,bp):
    if bp==123:
        f=open(f"{b}.txt",'a')
        f.write(f'\n{a},{p}')
        f.close()
        aca=f'{a}.txt'
        err=1
        while err==1:
            y=int(input('enter year in (****) format = ',))
            m=int(input('enter month in (**) format = ',)) 
            d=int(input('enter day in (**) format = ',))
            if y>=1000 and m>0 and d>0 and m<=12 and d<=31 and y<=9999:
                if m==2 and y%4==0 and d<=29:
                    if y%100==0:
                        if y%400==0:
                            da=f'{y}-{m}-{d}'
                            err=0
                        elif d<=28:
                            da=f'{y}-{m}-{d}'
                            err=0
                elif m==2 and y%4!=0 and d<=28:
                    da=f'{y}-{m}-{d}'
                    err=0
                elif m!=2 :
                    da=f'{y}-{m}-{d}'
                    err=0
            elif err==1:
                print('no date selected due to wrong input try again')
        g=open(f'{b}/{aca}','a')
        g.write(f'\n{n} = name\n{da} = DOB\n{c} = balance')
        g.close()
        print('account created successfully')
    else :
        print('bank pin wrong account can be created by bank employe only')
def check_balance (b,a,p):
    z=0
    f=open(f'{b}.txt','r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data=i.strip(',\n').split(',')
        if data[0]==a and data[1]==p:
            aca=f'{a}.txt'
            g=open(f'{b}/{aca}','r')
            print(g.read())
            g.close()
            z=1
    if z==0:
        print('account number or password wrong')
def deposite (b,a,p,c):
    z=0
    aca=f'{a}.txt'
    f=open(f"{b}.txt",'r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data=i.strip(",\n").split(',')
        if data[0]==a and data[1]==p:
            g=open(f"{b}/{aca}",'r')
            fd=g.readlines()
            g.close()
            g=open(f"{b}/{aca}",'w')
            r=''
            for j in fd:
                if j.endswith('balance'):
                    y=0
                    for x in j:
                        if x.isdigit():
                            y+=1
                        elif x=='.':
                            y+=1
                        else :
                            break
                    for q in range (0,y):
                        r+=j[q]
                    r=float(r)
                    c+=r
                    j=f'{c} = balance'
                    print(j)
                    g.write(j)
                else:
                    g.write(j)
            g.close()
            z=1
    if z==0:
        print('account number or password wrong')
def withdraw (b,a,p,c):
    z=0
    aca=f'{a}.txt'
    f=open(f'{b}.txt','r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data = i.strip(',\n').split(',')
        if data[0]==a and data[1]==p:
            r=''
            g=open(f'{b}/{aca}','r')
            fd=g.readlines()
            g.close()
            g=open(f'{b}/{aca}','w')
            for j in fd:
                if j.endswith('balance'):
                    y=0
                    for x in j:
                        if x.isdigit():
                            y+=1
                        elif x=='.':
                            y+=1
                        else :
                            break
                    for q in range (0,y):
                        r+=j[q]
                    r=float(r)
                    if r>=c:
                        r-=c
                        j=f'{r} = balance'
                        print(j)
                    else :
                        print('not enough balance')
                    g.write(j)
                else:
                    g.write(j)
            g.close()
            z=1
    if z==0:
        print('account number or password wrong')
def transfer (b1,b2,a1,a2,p1,c):
    z1=0
    z2=0
    a2=str(a2)
    aca1=f'{a1}.txt'
    aca2=f'{a2}.txt'
    f1=open(f'{b1}.txt','r')
    sd=f1.readlines()
    f1.close()
    f2=open(f'{b2}.txt','r')
    rd=f2.readlines()
    f2.close()
    for i in sd :
        data1 = i.strip(',\n').split(',')
        if data1[0]==a1 and data1[1]==p1:
            z1=1
            break
    if z1==0:
        print('your account number or pin is wrong ')
        return False
    for j in rd:
        if j.startswith(a2):
            z2=1
            break
    if z2==0:
        print('recievers account number not found')
        return False
    g1=open(f'{b1}/{aca1}','r')
    g2=open(f'{b2}/{aca2}','r')
    d1 = g1.readlines()
    d2 = g2.readlines()
    g1.close()
    g2.close()
    g1=open(f'{b1}/{aca1}','w')
    g2=open(f'{b2}/{aca2}','w')
    for u1 in d1:
        if u1.endswith('balance'):
            y=0
            c1=''
            for x1 in u1:
                if x1.isdigit():
                    y+=1
                elif x1=='.':
                    y+=1
                else:
                    break
            for t in range (0,y):
                c1+=u1[t]
            c1=float(c1)
            if c1>c:
                c1-=c
                g1.write(f'{c1} = balance')
                print (f'payment success full of rupess {c}')
            else:
                g1.write(u1)
                print('payment failed not enough balance')
                return False
        else:
            g1.write(u1)
    for u2 in d2:
        if u2.endswith('balance'):
            y=0
            c2=''
            for x2 in u2:
                if x2.isdigit():
                    y+=1
                elif x2=='.':
                    y+=1
                else:
                    break
            for t in range (0,y):
                c2+=u2[t]
            c2=float(c2)
            c2+=c
            g2.write(f'{c2} = balance')
        else :
            g2.write(u2)
    g1.close()
    g2.close()
def update_pin (b,a,p1,p2):
    z=0
    f=open(f'{b}.txt','r')
    ud=f.readlines()
    f.close()
    f=open(f'{b}.txt','w')
    for i in ud :
        data = i.strip(',\n').split(',')
        if data[0]==a and data[1]==p1:
            f.write(f'{a},{p2}\n')
            z=1
        else:
            f.write(i)
    f.close()
    if z==0:
        print('account number or pin is incorrect')
    else:
        print('pin updated successfully')
def update (b,a,p,wd,nd):
    z=0   
    aca=f'{a}.txt'
    f=open(f"{b}.txt",'r')
    ud=f.readlines()
    f.close()
    for i in ud:
        data = i.strip(',\n').split(',')
        if data[0]==a and data[1]==p:
            g=open(f'{b}/{aca}','r')
            dud=g.readlines()
            g.close()
            g=open(f'{b}/{aca}','w')
            for j in dud:
                if j.strip('\n').endswith(wd):
                    g.write(f'{nd} = {wd}\n')
                    z=1
                    print(f'{wd} changed successfully')
                else:
                    g.write(j)
            g.close()
    if z==0:
        print('incorrect account number or pin')
def main ():
    x=0
    bn=0
    y=0
    bn=int(input('type 1 for hdfc bank, type 2 axis bank, type 3 for sbi, type 4 to end interraction = ',))
    if bn==1:
        b='HDFC'
    elif bn==2:
        b='AXIS'
    elif bn==3:
        b='SBI'
    else:
        print('invalid input')
        return False
    while x!=3:
        print('type 1 to create account\ntype 2 to login\ntype 3 to exit')
        x=int(input())
        if x==1:
            bank(b,str(input('enter your name = ',)),int(input('enter acc number = ',)),int(input('enter your pin = ',)),float(input('enter balance = ',)),int(input('enter bank pin = ',)))
        elif x==2:
            a,p=int(input('enter your account number = ',)),int(input('enter pin = ',))
            a,p=str(a),str(p)
            Av=0
            f=open(f"{b}.txt",'r')
            ud=f.readlines()
            f.close()
            for i in ud:
                data=i.strip(',\n').split(',')
                if data[0]==a and data[1]==p:
                    Av=1
            if Av==1:
                while y!=8:
                    print('type 1 to check balance in your account\ntype 2 to deposite money in your account\ntype 3 to withdraw ammount from your account\ntype 4 to tranfer money from one accoungt to another\ntype 5 to update pin\ntype 6 to update name\ntype 7 to logout')
                    y=int(input())
                    if y==1:
                        check_balance(b,a,p)
                    elif y==2:
                        deposite(b,a,p,float(input('enter ammount to deposite = ',)))
                    elif y==3:
                        withdraw(b,a,p,float(input('enter ammount to withdraw = ',)))
                    elif y==4:
                        bn=int(input('type 1 for hdfc bank, type 2 axis bank, type 3 for sbi = ',))
                        if bn==1:
                            b2='HDFC'
                            transfer(b,b2,a,int(input('enter account number of reciever = ',)),p,float(input('amount to transfer = ',)))
                        elif bn==2:
                            b2='AXIS'
                            transfer(b,b2,a,int(input('enter account number of reciever = ',)),p,float(input('amount to transfer = ',)))
                        elif bn==3:
                            b2='SBI'
                            transfer(b,b2,a,int(input('enter account number of reciever = ',)),p,float(input('amount to transfer = ',)))
                        else:
                            print('wrong input try again')
                    elif y==5:
                        update_pin(b,a,p,int(input('enter your new pin = ',)))
                    elif y==6:
                        update(b,a,p,'name',str(input('enter your new name = ',)))
                    elif y==7:
                        print('thankyou')
                    else :
                        print('wrong input try again')
            else :
                print('incorrect acc number or pin')
        elif x==3:
            print()
        else:
            print('incorrect input')
main()