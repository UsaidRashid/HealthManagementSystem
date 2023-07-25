def getdate():
    import datetime
    return datetime.datetime.now()

print("ENTER 1 FOR OPENING CLIENT SONU's FILE")
print("ENTER 2 FOR OPENING CLIENT MONU's FILE")
print("ENTER 3 FOR OPENING CLIENT CHOMU's FILE")
n=int(input())

if n==1:
    print("PRESS 1 FOR DIET PLAN")
    print("PRESS 2 FOR EXERCISE PLAN")
    n1=int(input())
    if n1==1:
        f = open("SonuDiet.txt", "a+")
        print("PRESS 1 IF YOU WANT TO WRITE TO SONU's DIET")
        print("PRESS 2 IF YOU WANT TO LOOK TO SONU's DIET")
        m1=int(input())
        if m1==1:
            d=str(getdate())
            a=input("INPUT THE ITEM ")
            f.write("[")
            f.write(d)
            f.write("]    ")
            f.write(a)
            f.write("\n")
        elif m1==2:
            f.seek(0)
            print(f.readlines())
        f.close()
    elif n1==2:
        f=open("SonuExercise.txt","a+")
        print("PRESS 1 IF YOU WANT TO WRITE TO SONU's EXERCISE")
        print("PRESS 2 IF YOU WANT TO LOOK TO SONU's EXERCISE")
        m1 = int(input())
        if m1 == 1:
            d = str(getdate())
            a = input("INPUT THE EXERCISE NAME ")
            f.write("[")
            f.write(d)
            f.write("]    ")
            f.write(a)
            f.write("\n")
        elif m1 == 2:
            f.seek(0)
            print(f.readlines())
        f.close()

elif n==2:
    print("PRESS 1 FOR DIET PLAN")
    print("PRESS 2 FOR EXERCISE PLAN")
    n1=int(input())
    if n1==1:
        f = open("MonuDiet.txt", "a+")
        print("PRESS 1 IF YOU WANT TO WRITE TO MONU's DIET")
        print("PRESS 2 IF YOU WANT TO LOOK TO MONU's DIET")
        m1=int(input())
        if m1==1:
            d=str(getdate())
            a=input("INPUT THE ITEM ")
            f.write("[")
            f.write(d)
            f.write("]    ")
            f.write(a)
            f.write("\n")
        elif m1==2:
            f.seek(0)
            print(f.readlines())
        f.close()
    elif n1==2:
        f=open("MonuExercise.txt","a+")
        print("PRESS 1 IF YOU WANT TO WRITE TO MONU's EXERCISE")
        print("PRESS 2 IF YOU WANT TO LOOK TO MONU's EXERCISE")
        m1 = int(input())
        if m1 == 1:
            d = str(getdate())
            a = input("INPUT THE EXERCISE NAME ")
            f.write("[")
            f.write(d)
            f.write("]    ")
            f.write(a)
            f.write("\n")
        elif m1 == 2:
            f.seek(0)
            print(f.readlines())
        f.close()

elif n==3:
    print("PRESS 1 FOR DIET PLAN")
    print("PRESS 2 FOR EXERCISE PLAN")
    n1=int(input())
    if n1==1:
        f = open("ChomuDiet.txt", "a+")
        print("PRESS 1 IF YOU WANT TO WRITE TO CHOMU's DIET")
        print("PRESS 2 IF YOU WANT TO LOOK TO CHOMU's DIET")
        m1=int(input())
        if m1==1:
            d=str(getdate())
            a=input("INPUT THE ITEM ")
            f.write("[")
            f.write(d)
            f.write("]    ")
            f.write(a)
            f.write("\n")
        elif m1==2:
            f.seek(0)
            print(f.readlines())
        f.close()
    elif n1==2:
        f=open("ChomuExercise.txt","a+")
        print("PRESS 1 IF YOU WANT TO WRITE TO CHOMU's EXERCISE")
        print("PRESS 2 IF YOU WANT TO LOOK TO CHOMU's EXERCISE")
        m1 = int(input())
        if m1 == 1:
            d = str(getdate())
            a = input("INPUT THE EXERCISE NAME ")
            f.write("[")
            f.write(d)
            f.write("]    ")
            f.write(a)
            f.write("\n")
        elif m1 == 2:
            f.seek(0)
            print(f.readlines())
        f.close()
