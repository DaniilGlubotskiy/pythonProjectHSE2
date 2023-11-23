ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_geo_marks = set()

for user_marks in ids.values():
    unique_geo_marks.update(set(user_marks))

print(f"Результат: {unique_geo_marks}")
