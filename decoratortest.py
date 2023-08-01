def zero_division_error(func):
    def inner(a, b):
        if b == 0:
            return "Zero division not applicable"
        return func(a, b)
    return inner

@zero_division_error
def division(a, b):
    return a/b



print(division(10, 2))
print(division(10, 4))
print(division(10, 0))