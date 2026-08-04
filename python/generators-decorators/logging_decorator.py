from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished calling {func.__name__}")
        return result

    return wrapper


@log_activity
def brew_tea(type):
    print(f"Brewing {type} tea")


brew_tea("green")
