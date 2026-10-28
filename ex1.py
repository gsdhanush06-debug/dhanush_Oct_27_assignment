
cracker_name=input("Enter your cracker name:")
quantity=int(input("Enter the quantity:"))
one_cracker=100

total=one_cracker*quantity

gst_rate=5
gst_amount=total*gst_rate/100 #GST Formula
total_amount=total+gst_amount
print(f"Total amount for {quantity} {cracker_name} is: {total_amount} including GST")