from functools import wraps


def requie_admin(func):
    wraps(func)

    def wrapper(user_role):
        if user_role == "admin":
            return func(user_role)
        else:
            return "You are not authorized to perform this action"

    return wrapper


users = [
    {"id": 1, "name": "Gopal Adhikari", "role": "admin"},
    {"id": 2, "name": "Shivam Sah", "role": "user"},
    {"id": 3, "name": "Rahul Tag", "role": "user"},
]


@requie_admin
def access_dashboard(user_role):
    return f"Accessing dashboard as {user_role}"


for user in users:
    print(access_dashboard(user["role"]))
