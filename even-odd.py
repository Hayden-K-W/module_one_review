def even_or_odd(number=3):
    if (number % 2) == 0:
        print("even")
        result = "Even"
    else:
        print("Odd")
        result = "Odd"
    return result

result = even_or_odd()
print(result)