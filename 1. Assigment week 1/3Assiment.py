


#Question 1=	Create a list comprehension that returns the squares of only the even numbers from 0–20.
lists=[a**2 for a in range(21)if a%2==0]
print(lists)

#Question 2=	Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
nums = [3, 1, 4, 1, 5, 9]
result=sorted(nums)
print(result)

#Question 3=	Remove duplicates from a list while preserving the original order

nums = [3, 1, 4, 1, 5, 9]
result=list(dict.fromkeys(nums))
print(result)

#Question 4=
