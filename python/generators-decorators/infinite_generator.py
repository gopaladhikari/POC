def infinite_users():
    count = 0

    while True:
        yield {"id": count, "name": f"User {count}"}
        count += 1


user = infinite_users()


for _ in range(5):
    print(next(user))
