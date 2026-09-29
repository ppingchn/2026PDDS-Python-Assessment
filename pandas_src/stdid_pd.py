import pandas as pd

users = [
    { "id": 1, "name": "Alice"},
    { "id": 2, "name": "Bob"}
]

orders = [
    { "id": 1, "user_id": 1, "price": 1000},
    { "id": 2, "user_id": 2, "price": 500 },
    { "id": 3, "user_id": 1, "price": 200 }
]

# Section 1: DataFrame Creation
'''
Create a DataFrame from the users and orders lists
1. Create a DataFrame for users where variable name is "users_df"
2. Create a DataFrame for orders where variable name is "orders_df"
'''

# DataFrame Creation of Users

# Your Code Here

print("Users DataFrame:")
print(users_df)

# Expected Output:
#    id   name
# 0   1  Alice
# 1   2    Bob

# =============================================
# DataFrame Creation of Orders

# Your Code Here

print("Orders DataFrame:")
print(orders_df)

# Expected Output:
#    id  user_id  price
# 0   1        1   1000
# 1   2        2    500
# 2   3        1    200

