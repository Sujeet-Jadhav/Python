fp=open('text.txt','r')
dic={}
data=[]
for line in fp:
    data.append(line)
while True:
    flag=False
    choice=int(input("1:count frequency of words\n2:print content of line number\n3:Remove new line charcter\n4:copy one file to another\n5:get file size and number of line\n6:exit\n Enter the choice==> "))
    match choice:
        case 1:
            if len(dic)!=0:
                print(dic)
            else:
                for line in data:
                        words=line.split()
                        for w in words:
                            temp=dic.get(w)
                            if temp is None:
                                dic[w]=1
                            else:
                                dic[w]=temp +1
                print(dic)
        case 2:
            n=int(input("Enter the NUmber Line: "))
            if n <=0 or n > len(data):
                print("invalid line number")
            else:
                print(data[n-1])
        case 3:
            s=""
            for i in data:
                print(i)
                t= i[:len(i)-1:]
                s=s+t
            print(s)
        case 4:
            fname=input("Enter the file name:")
            f=open(fname,'w')
            for line in data:
                f.write(line)
            print("file content of ra.txt are copied into ",fname,"...")
        case 5:
            name=input("Enter the file name: ")
            #st=os.stat(name)
            i=open(name, 'r')
            cnt=0
            size=0
            for j in i:
                cnt +=1
                size+=len(j)+1
            size-=1
            print("size of given",name,"is:",size,"bytes")
            print("total number of lines:",cnt)

        case 6:
            flag=True
        case _:
            print("Invalid Choice")
    if flag:
        break

