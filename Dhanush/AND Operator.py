
Username='admin'
password='123'
if Username=='admin' and password=='123':
    print('login success')
else:
    print('login fail')



print("_"*5)

mark =int(input("enter mark"))

if mark <=35:
    print('fail')
elif  mark > 35 and mark <=60:
    print('3rd class pass')
elif mark > 60 and mark <=80:
    print('2nd class pass')
elif mark > 80 and mark <=100:
    print('1st class pass')
else :
    print('Invalid mark')