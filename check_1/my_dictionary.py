my_dictionary = {
    "item_name": "milk",
    "price": "1.49"
}

my_dictionary["type"] = "whole"
print(my_dictionary)

print(my_dictionary["type"])

#Loop both keys and values
for x, y in my_dictionary.items():
    print(x, y)