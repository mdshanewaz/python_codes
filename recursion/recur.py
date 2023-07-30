# def my_count():
#     for i in range(1, 11):
#         print(i)

# my_count()


def my_count_2(n):
    if n > 5:
        return
    print(n)
    my_count_2(n+1)
    print(n)

my_count_2(1)