# Variable Setup
users = [
    { "id": 1, "name": "Alice"},
    { "id": 2, "name": "Bob"}
]

orders = [
    { "id": 1, "user_id": 1, "price": 1000},
    { "id": 2, "user_id": 2, "price": 500 },
    { "id": 3, "user_id": 1, "price": 200 }
]

# Section 1: List joining
'''
Join the users and orders lists based on user_id and id
By declear variable user_orders to store the result of the join operation
'''

user_orders = []
for order in orders:
    for user in users:
        if order["user_id"] == user["id"]:
            user_orders.append({
                "id": order["id"],
                "name": user["name"],
                "user_id": order["user_id"],
                "price": order["price"]
            })

print("Section 1: List joining")
print(user_orders)

# Expected Output:
# [{'id': 1, 'name': 'Alice', 'user_id': 1, 'price': 1000}, {'id': 2, 'name': 'Bob', 'user_id': 2, 'price': 500}, {'id': 3, 'name': 'Alice', 'user_id': 1, 'price': 200}]

# Section 2: List Grouping
'''
Group the orders list by user_id and calculate the total price for each user
1. Declare a dictonary variable "grouped"
2. Set "name" as the key
3. Set the initial value as a dictionary (when key doesn't exist)
4. Increment the "total_price" and "order_count" of the order for each user

Dict structure:
{
    "name": {
        "total_price": 0,
        "order_count": 0
    }
}
'''

grouped = {}
for order in user_orders:
    name = order["name"]
    if name not in grouped:
        grouped[name] = {"total_price": 0, "order_count": 0}
    grouped[name]["total_price"] += order["price"]
    grouped[name]["order_count"] += 1

print("Section 2: List Grouping")
print(grouped)

# Expected Output:
# {'Alice': {'total_price': 1200, 'order_count': 2}, 'Bob': {'total_price': 500, 'order_count': 1}}

# Section 3: List Sorting
'''
Sort the grouped dictionary by "total_price" in descending order
1. Declare a variable "sorted_grouped" to store the result of the sorting operation
2. Use the sorted() function to sort by "total_price" in descending order
'''

sorted_grouped = sorted(grouped.items(), key=lambda x: x[1]["total_price"], reverse=True)

print("Section 3: List Sorting")
print(sorted_grouped)

# Expected Output:
# [('Alice', {'total_price': 1200, 'order_count': 2}), ('Bob', {'total_price': 500, 'order_count': 1})]

# Section 4: List Indexing
'''
Print the name of the user with the highest total price from the sorted_grouped list
1. Declare a variable "top_user" to store the name of the user with the highest total price
2. Use indexing to access the first element of the sorted_grouped list and print all the details of the user with the highest total price
'''

highest_total_price_user = {
    "name": sorted_grouped[0][0],
    "total_price": sorted_grouped[0][1]["total_price"],
    "order_count": sorted_grouped[0][1]["order_count"]
}

print("Section 4: List Indexing")
print(highest_total_price_user)

# Expected Output:
# {'name': 'Alice', 'total_price': 1200, 'order_count': 2}