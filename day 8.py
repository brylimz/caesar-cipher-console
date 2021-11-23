# def greet():
#     print("Hello Angela")
#     print("How do you do Angela?")
#     print("Isn't the weather nice today?")
#
#
# greet()
# # function that allows for input
#
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
#
# greet_with_name("Angela")

# function with more than 1 input
# def greet_with(location, name):
#     print(F"Hello {name}, What is it like in {location}")
#
#
# greet_with("Angela", "London")
# # function with arguments
# greet_with(location="london", name="angela")

# area calc
# import math
#
#
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(F"You'll need {num_of_cans} cans of paint")
#
#
# test_h = int(input("height of wall :"))
# test_w = int(input("Width of wall :"))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("its a prime number.")
        else:
            print("its not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
