#===============================================================
#Part A — Python Lists 
#===============================================================


#Question 1
a=[12,23,44,56,40,32,69,13]
print(a[0])
print(a[-1])

#Question 2 
a=["orange","red","green","blue","white"]
Result=len(a)
print(Result)

#question 3 
a=["orange","red","green","blue","white"]
a.append("Black")
print(a)

#Question 4 =
a=["orange","red","green","blue","white"]
a.insert(0,"Gray")
print(a)

#Question 5
a=["orange","red","green","blue","white"]
a.remove("white")
print(a)

#Question 6
a=[12,14,16,16]
item_a=a.pop()
print(item_a)
print(a)

#Question 7
c=[90,60,40,3]
print(3 in c)

#Question 8
a=[1,2,3,4,5,6,7]
Result=(a[0:3])
print(Result)

#Question 9
a=[11,14,13,19]
a[1]=12
print(a)

#Questin 10
list=[1,2,2,4,5,2,5]
Result=list.count(2)
print(Result)

#=================================================
#Part B — Python Tuples
#=================================================


#Question 1=	Create a tuple t = (10, 20, 30) and print the second element.

t=(10,20,30)
print(t[1])

#Question 2=	Find the length of tuple ('a', 'b', 'c').
t=('a','b','c')
print(len(t))

#Question 3=	Unpack the tuple (4, 5) into variables x and y

t=(4,5)
(x,y)=t
print(x)
print(y)

#Question 4=	Check if 'b' is in the tuple ('a', 'b', 'c').
t=('a','b','c')
print('b'in t)

#Question 5=	Create an empty tuple and print its type.
t=( )
print(t)
print("t:",type(t))

#Question6=	Concatenate (1, 2) and (3, 4) into a new tuple.
t1=(1,2)
t2=(3,4)
Result=(t1+t2)
print(Result)

#Question7=	Repeat (7,) three times.
t=(7,)
Result=t*3
print(Result)

#Question8=	Find the index of 2 in (1, 2, 3, 2).
t=(1,2,3,2)
print(t.index(2))

#Question9=	Count how many times 2 appears in (1, 2, 3, 2).
t=(1,2,3,2)
Result=t.count(2)
print(Result)

#Question10=	Create a single‑element tuple containing the value 5
t=(5,)
print(t)
print(type(t))

#=====================================================================================
#Part C — Python Sets (10 Beginner Questions)                                     ====
#=====================================================================================

#Question 1=	Create a set from [1, 2, 2, 3] and print it.
number=[1,2,2,3]
c=set(number)
print(c)

#Question 2=	Add element 4 to the set {1, 2, 3}.
a={1,2,3}
a.add(4)
print(a)

#Question 3=	Remove element 2 from the set {1, 2, 3}.
s={1,2,3,4}
s.remove(2)
print(s)

#Question 4=	Check if 5 is in the set {1, 3, 5}.
s={1,3,5,7}
print(5 in s)

#Question 5=	Find the length of set {10, 20, 30}.
s={10,20,30,40}
Result=len(s)
print(Result)

#Question 6=	Clear all elements from the set {1, 2, 3}.
a={1,2,3,4,5,6,7,8,9}
a.clear()
print(a)

#Question 7=












#Question 8=	Convert list ['a', 'a', 'b'] into a set to remove duplicates.
number=['a','b','a']
a=set(number)
print(a)

#Question 9=	Create two sets and print their union
set1={1,2,3,4,5,6,7,8,9,10}
set2={6,7,8,9,10,11,12,13,14}
result=set1.union(set2)
print(result)

#Question 10=	Create two sets and print their intersection.
set1={1,3,5,7,9,11,13,15}
set2={1,2,3,4,5,6,7,8,9,10}
result=set1.intersection(set2)
print(result)

#=================================================================================
#Part D — Python Dictionaries (10 Beginner Questions)
#=================================================================================

#question 1=	Create a dictionary {'name': 'Ali', 'age': 25} and print the name
a={'name': 'Ali', 'age': 25}
print(a["name"])

#Question 2=	Add key 'city': 'Lahore' to a dictionary.
a={'name': 'Ali', 'age': 25}
a["city"]="lahore"
print(a)

#Question 3 =	Change 'age' in {'name': 'Ali', 'age': 25} to 30.
a={'name': 'Ali', 'age': 25}
a["age"]=30
print(a)

#question 4=	Delete key 'age' from a dictionary.
a={'name': 'Ali', 'age': 25}
del a["age"]
print(a)

#Question 5=	Check if key 'salary' exists in a dictionary.
a={'name': 'Ali', 'age': 25}
print("salary" in a)

#Question 6=	Print all keys from {'a': 1, 'b': 2}.
a={'name': 'Ali', 'age': 25}
result=a.keys()
print(result)

#Question 7=	Print all values from a dictionary.
a={'name': 'Ali', 'age': 25}
result=a.values()
print(result)

#Question 8=	Iterate and print key‑value pairs from {'x': 10, 'y': 20}.
a={'name': 'Ali', 'age': 25}
for key,value in a.items():
    print(a)

#Question9=	Use get() to safely read key 'score' from an empty dictionary.
my_dic={}
print(my_dic.get("score"))

#Question 10=
keys={'a','b'}
values={1,2}
print(dict(zip(keys,values)))






#Alhamdulillah! (ٱلْحَمْدُ لِلَّٰهِ)