def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


user_num = int(input("please enter an integer:"))

while True:
    result = collatz(user_num)
    if result == 1:
        break
    user_num = result