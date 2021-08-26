word1 =[]
word2 =[]
word3 =[]

Doc1 = "it is what it is"
Doc2 = "What? What is is is it"
Doc3 = "it is a banana. it!"

word1 = Doc1.split(" ")
word2 = Doc2.split(" ")
word3 = Doc3.split(" ")

word1.insert(0,"word1")
word2.insert(0,"word2")
word3.insert(0,"word3")


countword1=0

list=1
for i in word1:
    if word1[list] == i:
        countword1+=1
    if list==2:
        countword1=0
    print(word1[list], i,countword1)

