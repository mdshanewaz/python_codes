bangla = int(input("Marks in Bangla = "))
english = int(input("Marks in English = "))
math = int(input("Marks in Math = "))
science = int(input("Marks in Science = "))

result = (bangla + english + math + science) / 4

print(result)

if result <= 40:
    print("Grade = F")
elif result > 40 and result <= 60:
    print("Grade = D")
elif result > 60 and result <= 70:
    print("Grade = C")
elif result > 70 and result <= 80:
    print("Grade = B")
elif result > 80 and result <= 90:
    print("Grade = A")
else:
    print("Grade = A+")