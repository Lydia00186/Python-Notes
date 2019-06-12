'''
Dealing with the str usage,including:
Capitalize, Lowercase, Sort, Slice and so forth

'''

fruits = ['banana','orange','berry','apple','coconut','Lemon','WaterMelon']

# sorted() will sort the items inside alphabetically but will not change the
# original list
sorted(fruits)
print(fruits)

# change the order permantently

fruits.sort()
print(fruits)

# reverse -- sort the items in reverse alphabetical order
fruits_reverse = sorted(fruits, reverse=True)
print(fruits_reverse)

# order the item according to the length
fruits_len = sorted(fruits,key=len)
print(fruits_len)


