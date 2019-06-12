'''
Access the items in the list through different ways:
1. List Comprehension
2. For Loop
3. len()
4. enumerate()

'''


fruits = ['banana','orange','berry','apple','coconut','Lemon','WaterMelon']

# Capitalize the items, using list comprehension
fruits = [i.title() for i in fruits]
print(fruits)

# Lowercase, using for loop
for i in fruits:
    print(i.lower())

# Lowercase, using len()
for i in len(fruits):
    print(fruits[i].lower())

# Uppercase the item, using enumerate
for index,item in enumerate(fruits):
    # print(index,item.upper())
    print(item.upper())
