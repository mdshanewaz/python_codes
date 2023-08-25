
n = int(input("n = "))

number_list = list(range(1, n+1))

for i in number_list:
    if i >= 3:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    else:    
        print(i)


def reverse_words_order_and_swap_cases(sentence):
    
    print(sentence)

    words = sentence.split(' ')[::-1]

    swap_words = []

    for i in words:
        cont = i.swapcase()
        swap_words.append(cont)

    rev_sentence = ' '.join(swap_words)
    print(rev_sentence)

reverse_words_order_and_swap_cases("aWESOME is cODING")

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        area = self.a * self.b
        print("%.2f" % area)

class Circle:
    def __init__(self, a):
        self.a = a
    
    def area(delf):
        area = 3.1416 * a * a
        print("%.2f" % area)


        
