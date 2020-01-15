# Document at least 3 use cases of the * and ** operators

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(
            name_1="Sayo",
            name_2="Joshua",
            name_3="Faith",
            name_4="Gbolahun",
            name_5="Alimot",
            name_6="Kingsley"
        )

def print_positions(*args):
    for index, value in enumerate(args):
        print("The position of {} is {}".format(value, index))


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# def lucas(n):
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     else:
#         return lucas(n - 1) + lucas(n - 2)


def order_checker(*args):
    for value in range(len(args)):
        if args[value] > args[value + 1]:
            return "Not ordered"
        return "Ordered"

print(order_checker(2, 1, 2, 3, 4, 5))

