# Prints positional arguments


def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)

# # Prints named arguments


# def f(*args, **kwargs):
#     print("Named:", kwargs)


# f(galleons=100, sickles=50, knuts=25)