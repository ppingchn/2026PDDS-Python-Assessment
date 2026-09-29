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
# Users DataFrame:
#    id   name
# 0   1  Alice
# 1   2    Bob

# =============================================
# DataFrame Creation of Orders

# Your Code Here

print("Orders DataFrame:")
print(orders_df)

# Expected Output:
# Orders DataFrame:
#    id  user_id  price
# 0   1        1   1000
# 1   2        2    500
# 2   3        1    200

# Section 2: DataFrame Marging
'''
Merge the users_df and orders_df DataFrames based on user_id and id
1. Declare a variable "merged_df" to store the result of the merge operation
2. Use the merge() function from pandas to merge the two DataFrames on the specified columns
'''

# Your Code Here

print("Merged DataFrame:")
print(merged_df)

# Expected Output:
# Merged DataFrame:
#    id   name  user_id  price
# 0   1  Alice        1   1000
# 1   3  Alice        1    200
# 2   2    Bob        2    500

# Section 3: DataFrame Grouping & Sorting
'''
Group the merged_df DataFrame by "name" and calculate the total price and order count for each user
by using the groupby() and agg() functions from pandas and sort the result by "total_price" in descending order
'''

# Your Code Here

print("Grouped and Sorted DataFrame:")
print(grouped_sorted_df)

# Expected Output:
# Grouped and Sorted DataFrame:
#     name  total_price  order_count
# 0  Alice         1200            2
# 1    Bob          500            1

# Section 4: DataFrame Indexing
'''
Index the grouped_sorted_df DataFrame to get the row with the highest total_price
Pring out the top user who has the highest total price from the grouped_sorted_df DataFrame
'''

# Your Code Here

print("Top User:")
print(top_user)

# Expected Output:
# Top User:
# total_price    1200
# order_count       2
# name: Alice, dtype: int64