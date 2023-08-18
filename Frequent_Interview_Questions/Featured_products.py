from collections import Counter

def featuredProducts(arr):
    # Sorting the Array
    arr.sort()

    # Storing the items in a dictionary (hash Map)
    productCount = dict(Counter(arr))

    # Calcutating the max frequency
    max = 0
    for i in productCount:
        if max < productCount[i]:
            max = productCount[i]

    # Appending the items with max value in the new list
    featured = []
    for key ,value in productCount.items():
        if max == value :
            featured.append(key)
    
    # Printing the last name in the list
    return featured[-1]






arr = ['YellowShirt' , 'redShirt' ,'GreenShirt' , 'yellowShirt' , 'yellowShirt' , 'redShirt' , 'redShirt' ]
print("The featured product this week is : " , featuredProducts(arr))