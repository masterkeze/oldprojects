def findmajor(list1):
    s=0#sum
    list2 = []
    for i in range(len(list1)):
        s+=list1[i]
    temps=s
    news=s
    for i in range(len(list1)):
        if list1[i]*(int(len(list1)/2)+1) >news:
            temps -= list1[i]
        else:
            list2.append(list1[i])
    while (temps != news):
        news = temps
        temps = s
        for i in range(len(list1)):
            if list1[i]*(int(len(list1)/2)+1) >news:
                temps -= list1[i]
            else:
                list2.append(list2[i])
    print(temps,news)
    print(list2)
