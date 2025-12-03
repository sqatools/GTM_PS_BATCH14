products=[]

while True:
    pname=input("Enter Product Name:")
    if pname.lower()=="done":

        print("Stop Tracking!!!")
        break
    products.append(pname)
    print(f"Tracking product: {pname}")

print("\nAll products tracked:")
for p in products:
    print(p)
