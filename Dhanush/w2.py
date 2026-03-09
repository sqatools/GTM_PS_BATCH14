products=[]
while True:
    name=input("Enter Product Name:")
    if name.lower()=="done":
        print("Stop Tracking!")
        break


    url=input("Enter Product URL:")
    items={"name":name,"url":url}
    products.append(items)
    print(f"Tracking:{name}")
print("\nAll products tracked:")
for items in products:
    print(f"{items['name']} -> {items['url']}")
