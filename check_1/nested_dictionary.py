my_grocery_list = {
    "item1" : {
        "name" : "milk",
        "price" : 1.49
    },
    "item2" : {
        "name" : "coffee",
        "price" : 6.99
    },
    "item3" : {
        "name" : "eggs",
        "price" : 5.49
    },
    "item4" : {
        "name" : "butter",
        "price" : 3.99
    },
    "item5" : {
        "name" : "sugar",
        "price" : 2.49
    },
    "item6" : {
        "name" : "flour",
        "price" : 2.99
    },
}

print(my_grocery_list["item6"])

i = 1
while i < 6:
    print(my_grocery_list["item" + "{i}"])
    i += 1