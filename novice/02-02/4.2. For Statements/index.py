# words = ["anggur", "apel", "jeruk"]
# for i in words:
#     print(i)

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for a in users:
#     print(a)

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#     print(users)

users = {'Hans': 'active', 'Éléonore': 'inactive', 'Nida': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(users)
        print(active_users)

a = {}
a["c"] = "d"
a["e"] = "f"
print(a)

