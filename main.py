from ops import add_product,view_product,update_product,delete_product
while True:
    print("1.add product")
    print("2. view products")
    print("3. update product")
    print("4. delete product")
    print("5. exit")
    choice=int(input("enter a option:"))
    if choice==1:
        add_product()
    elif choice==2:
        view_product()
    elif choice==3:
        update_product()
    elif choice==4:
        delete_product()
    else:
        print("Thank you")
        break
