def serve_tea():
    yield "Hot"
    yield "Cold"


hot_tea = serve_tea()


for tea in hot_tea:
    print(tea)

# Generator funcions


def get_users():
    yield {"id": 1, "name": "Gopal"}
    yield {"id": 2, "name": "Shivam"}
    yield {"id": 3, "name": "Rahul"}


user = get_users()

print(next(user))


for u in user:
    print(u)
