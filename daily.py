# user_are = "Mirpur"

# total_purchase_price = 100

# if user_are in ["Mirpur", "Motijil", "Monardip"]:

#     if total_purchase_price >= 600:
#         print("Shipping is free")
    
#     elif total_purchase_price >= 300 and total_purchase_price < 600:
#         print("Shipping price is 80")
    
#     else:
#         print("Shipping is 120")
    
# elif user_are in ["Mohakhali", "Uttora", "Gulshan"]:

# else:
#     print("Shipping is not available") 


# n = int(input("n = "))

# if n%2 != 0:
#     print("Weird")
# else:
#     if n >= 1 and n <= 5:
#         print("Not Weird")
#     elif n >= 6 and n<= 20:
#         print("Weird")
#     else:
#         print("Not Weird")

# def plusMinus(arr):
#     # Write your code here
#     n = len(arr)
#     p = 0
#     ne = 0
#     z = 0
    
#     for i in arr:
#         if i > 0:
#             p = p+1
#         elif i < 0:
#             ne = ne+1
#         else:
#             z = z+1
    
#     p = p/n
#     ne = ne/n
#     z = z/n

#     print("{:.6f}".format(p))
#     print("{:.6f}".format(ne))
#     print("{:.6f}".format(z))

# plusMinus([1, 1, 0, -1, -1])


# def miniMaxSum(arr):
#     sum = 0
#     arr = sorted(arr)
#     for i in arr:
#          sum = sum + i
    
#     min = sum - arr[-1]
#     max = sum - arr[0]

#     print(min, max)


# miniMaxSum([1, 3, 5, 7, 9])

# def timeConversion(s):

#     o = ''
#     t = ''
#     print(s)

#     for i in range(8, 10):
#         o = o + s[i]
    
#     for i in range(0, 2):
#         t = t + s[i]
    
#     t = int(t)

#     if o == 'AM':
#         if t == 12:
#             t = str('00')
#         else:
#             t = '0' + str(t)
#     else:
#         if t == 12:
#             t = t
#         else:
#             t = t+12
    
#     t = str(t)
#     print("o = ", o)
#     print(t)
#     print(type(t))

    
#     s = t + s[2:] 
#     s = s.replace(o, '')

#     print(s)

# timeConversion('12:45:54PM')

def findMedian(arr):
    arr = sorted(arr)
    print(arr)

    n = len(arr)
    #print(n)

    if n % 2 == 0:
        n = n 
    else:
        n = n + 1
    
    #print(n)

    n = n / 2
    n = int(n)
    n= n-1

    #print(n)

    print(arr[n]) 

findMedian([0, 1, 2, 4, 6, 5, 3])        