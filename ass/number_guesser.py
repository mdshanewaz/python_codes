import random

low = 1
high = 50

correct_answer = random.randint(low, high)
print(correct_answer)

for i in range (0, 5):
    user_ans = int(input("Enter your estimated answer:"))
    
    if user_ans > correct_answer:
        print("Correct answer is smaller!")
        
    elif user_ans < correct_answer:
        print("Correct answer is greater!")
    
    else:
        print("You Win")
        break 