# # Q5 print last n line
# fp=open('text.txt','r')
# n=int(input("enter the line number:"))
# data=[]
# for line in fp:
#     data.append(line)
#
# l=len(data)
# i=l-n
# for i in range(i,l):
#     print(data[i],end="")
#
#
# # #Q5 2 print most frequent words
#
# fp=open('text.txt','r')
# dic={}
# for line in fp:
#     words=line.split()
#     for w in words:
#         temp=dic.get(w)
#         if temp is None:
#             dic[w]=1
#         else:
#             dic[w]=temp+1
# t=sorted(dic.values())
# for i in dic:
#     if dic[i]== t[len(t)-1]:
#         print(i,": ",dic[i])


fp = open("text.txt",'a')
fp.write("This is file")
fp.close()

