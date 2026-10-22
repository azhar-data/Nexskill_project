
#Beginner Level (Strings Fundamentals)


#first Question 	Length of a String
bookInfo="Computer is a good book"
print(bookInfo)
print(type(bookInfo))

#2nd question     Uppercase & Lowercase
print(bookInfo.upper())
print(bookInfo.lower())

#3rd 	Count a Character
Computer="future technology "
print(Computer.count("o"))

#4th 	First & Last Character
a="TEchnology"
print(a[0])
print(a[-1])

#5th Question 	Check Substring Presence
a="computer Technology"
sub="Technology"
Result=sub in a
print(Result)

#6th Question 	Slice a String
c="Nexskill is a good place for learning Ai"
print(c[0:9])

#7th Question 	Reverse a String
d="Garden town Lahore"
print(d[::-1])

#8th Question 	Replace Substring
E="sajwal is a good person"
result=E.replace("good","intellgent")
print(result)

#9th Question 	Split and Join
text="this is the over sentence for python"
result=text.split()
print(result)
result="".join(text)
print(result)

#10th Question Strip Whitespace
f="   This is my book in this field      "
result=f.strip()
print(result)



#=======================================================================================
#Intermediate Level (More Involved String Tasks)
#==================================================================

# 1st Question  	Count Vowels & Consonants   
text="how are you and what os your name"
vowel_count=0
conastant_count=0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel_count+=1
    else:
        conastant_count+=1

print(F"vowel:{vowel_count},Constant:{conastant_count}")

#Question 2=
