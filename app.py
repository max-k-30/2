# x = 3
# y = float(3)
# print(x,y)
# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)
# print (values[0])
# print (values[6])
# x = "this is a thing"
# y = x.split()
# z = y[0]
# print(y)
# print(z)
# def count():
#     x = input("gimme some words ")
#     y = x.split()
#     print(len(y)) 
# count()
# day_of_the_week = input("What day is it? ")
# if day_of_the_week == "Friday":
#     print("correct!")
# else:
#     print("incorrect")
# x = "test"
# print(f"hello {x}")
# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')
# def odd_or_even():
#     x = int(input("pick any integer "))
#     if x%2 == 0:
#         print("even")
#     else:
#         print("odd")
# odd_or_even()
def bill_calculation():
    x = input("How was your meal? ")
    y = input("what was the total without tax? ") 
    if x == "bad":
        print(y)
    elif x == "okay":
        print(y *= 1.15)
    elif x == "good":
        print(y *= 1.2)
    elif x == "great":
        print(y *= 1.25)
bill_calculation()