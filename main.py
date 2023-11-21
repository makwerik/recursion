
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    print(factorial(7))