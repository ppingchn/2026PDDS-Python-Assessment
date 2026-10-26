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
users_df = None  # Replace this with your solution

print("Users DataFrame:")
print(users_df)

# Expected Output:
# Users DataFrame:
#    id   name
# 0   1  Alice
# 1   2    Bob

# =============================================
# DataFrame Creation of Orders

# Your Code Here
orders_df = None  # Replace this with your solution

print("Orders DataFrame:")
print(orders_df)

# Expected Output:
# Orders DataFrame:
#    id  user_id  price
# 0   1        1   1000
# 1   2        2    500
# 2   3        1    200

# Section 2: DataFrame Merging
'''
Merge the users_df and orders_df DataFrames based on user_id and id.
1. Declare a variable "merged_df" to store the result of the merge operation.
2. Use the merge() function from pandas to merge the two DataFrames.
   Merge users_df (left) with orders_df (right) where users_df["id"] matches
   orders_df["user_id"].
'''

# Your Code Here
merged_df = None  # Replace this with your solution

print("Merged DataFrame:")
print(merged_df)

# Expected Output:
# Merged DataFrame:
#    id_x   name  id_y  user_id  price
# 0     1  Alice     1        1   1000
# 1     1  Alice     3        1    200
# 2     2    Bob     2        2    500

# Section 3: DataFrame Grouping & Sorting
'''
Group the merged_df DataFrame by "name" and calculate the total price and
order count for each user. Use the groupby() and agg() functions from pandas
and sort the result by "total_price" in descending order.

The output columns must be named exactly:
  - "total_price"  : sum of the price column
  - "order_count"  : number of orders per user

Declare a variable "grouped_sorted_df" to store the result, with "name" as
the index.
'''

# Your Code Here
grouped_sorted_df = None  # Replace this with your solution

print("Grouped and Sorted DataFrame:")
print(grouped_sorted_df)

# Expected Output:
# Grouped and Sorted DataFrame:
#           total_price  order_count
# name
# Alice            1200            2
# Bob               500            1

# Section 4: DataFrame Indexing
'''
Index the grouped_sorted_df DataFrame to get the row with the highest total_price.
Declare a variable "top_user" to store the Series for the user with the highest
total price from the grouped_sorted_df DataFrame.
The Series index should be the user's name (i.e., top_user.name == "Alice").
'''

# Your Code Here
top_user = None  # Replace this with your solution

print("Top User:")
print(top_user)

# Expected Output:
# Top User:
# total_price    1200
# order_count       2
# Name: Alice, dtype: int64
