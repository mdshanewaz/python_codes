user_are = "Mirpur"

total_purchase_price = 100

if user_are in ["Mirpur", "Motijil", "Monardip"]:

    if total_purchase_price >= 600:
        print("Shipping is free")
    
    elif total_purchase_price >= 300 and total_purchase_price < 600:
        print("Shipping price is 80")
    
    else:
        print("Shipping is 120")
    
# elif user_are in ["Mohakhali", "Uttora", "Gulshan"]:

# else:
#     print("Shipping is not available") 