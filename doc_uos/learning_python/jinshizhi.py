while True:
    try:
        str =input()
        str1=int(str.split('.')[0])
        str2=int(str.split('.')[1])
        r = int(round(float(str)))
        if str2==5 and str1%2 == 0:
            r += 1
        print(r)
    except:
        break