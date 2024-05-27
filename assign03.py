Str=input("Enter the Input:")
List=Str.split()
dic=dict()

for s in List:
    temp=dic.get(s)

    if temp==None:
        dic[s]=1
    else:
        dic[s]=temp+1
fre=[[] for i in range(0,len(List)+1)]

for key in dic:
    fre[dic[key]].append(key)

cnt=10
flag=False
res=[]

for i in range(len(fre)-1,-1,-1):
    temp=fre[i]
    if len(temp)==0:
        continue
    for data in temp:
        if cnt==0:
            flag=True
            break
        res.append(data)
        cnt-=1
    if flag:
         break
print(res)




from collections import Counter

# Get user input
user_input = input("Enter the Input:")

# Split the input into a list of words
word_list = user_input.split()

# Use Counter to count word frequencies
word_counter = Counter(word_list)

# Get the 10 most common words
most_common_words = word_counter.most_common(10)

# Extract just the words from the result
result = [word for word, count in most_common_words]

# Print the result
print(result)

