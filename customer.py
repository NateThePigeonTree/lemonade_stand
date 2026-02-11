from customer_class import Customer
num=1
Customer_list=[]
new_customer=Customer()
for _ in range(5):
    Customer_list.append(Customer())
    print(f"the customer prefence for sweetness is"(new_customer.get_customer_attributes()['sweetness']))
    print(f"the customer prefence for ice is"(new_customer.get_customer_attributes()['ice']))
    print(f"the customer prefence for price is"(new_customer.get_customer_attributes()['price']))
for i in Customer_list:
    for each in ['sweetness''ice''price']:
        print(f"customer {num}`s prefernces for{each}")