users = [
    {"name": "jhon" , "active": True},
    {"name": "Sam" , "active": False},
    {"name": "Alice" , "active": True},
    {"name": "Jarad" , "active": False},
]

active_users = [
         user["name"] for user in  users if user["active"]
]

print(active_users)