import os


save_path = 'Data/'
Product_file = "Product.txt"
Couriers_file = "Couriers.txt"


    
if not os.path.exists(save_path):
    os.mkdir(save_path)

File_name_path = os.path.join(save_path, Product_file)
Couriers_file = os.path.join(save_path, Couriers_file)


Product_choices=['0.Menu','1.Product list','2.ADD Product', '3.Update Product','4.Delete Product']
Courier_choices=['0.Menu','1.Courier list','2.ADD Courier', '3.Update Courier','4.Delete Courier']

main_menu=['0.Exit App','1.Product Menu','2.Couriers menu']

def Load_Couriers_data():
    try:
        with open(Couriers_file,'r+') as f:
            Couriers_list = [line.strip() for line in f]
            return Couriers_list
    except FileNotFoundError:
        with open(Couriers_file,'w+') as f:
            Couriers_list = ['John','Kishan','Kinjal','Piyush','Yesh','Gopi','Pari','Jenish']
            for listitem in Couriers_list:
                f.write('%s\n' % listitem)
            return Couriers_list

def Load_Product_data():
    try:
        with open(File_name_path,'r+') as f:
            Product_list = [line.strip() for line in f]
            return Product_list
    except FileNotFoundError:
        with open(File_name_path,'w+') as f:
            Product_list = ['Coffee','Tea','Pizza','Burge','Fries','Apple','Donut','Cake']
            for listitem in Product_list:
                f.write('%s\n' % listitem)
            return Product_list
         

Product_list = Load_Product_data()
Couriers_list = Load_Couriers_data()

def Add_data(data_list):
    add_courier=input('Please enter data to add in list=')
    data_list.append(add_courier)
    Print_Data(data_list)
    print(f'{add_courier} Successfully added into list.')
    
def Update_data(data_list):
    Display_menu(data_list)  
    Selected_Courier=int(input('Please select index to update ='))
    Updated_Courier= input('Please enter new product=')
    data_list[Selected_Courier]=Updated_Courier
    print(f'{Updated_Courier} Successfully updated into list.')
    Print_Data(data_list)

def Delete_Product(data_list):
    Display_menu(data_list)
    Selected_Courier=int(input('Please select index to delete='))
    print(f'{data_list[Selected_Courier]} Successfully deleted from list.')
    data_list.pop(Selected_Courier)
    Print_Data(data_list)


def Print_Data(data_list):
    if data_list==Product_list:
        with open(File_name_path,'w+') as f:
            for listitem in data_list:
                f.write('%s\n' % listitem)
    elif data_list==Couriers_list:
        with open(Couriers_file,'w+') as f:
            for listitem in data_list:
                f.write('%s\n' % listitem)

def Display_menu(data_list):
        Load_Product_data()
        Load_Couriers_data()
        for i,product in enumerate(data_list):
         print(i,product)  

def All_Menu():
    for menu in main_menu:
        print(menu)

def All_Choice(data_list):
    for choice in data_list:
        print(choice)

def Start():
    All_Menu()
    main_menu_choice = input("Enter choice from 0 to 1:")
    if main_menu_choice in ('0','1','2'):
     if main_menu_choice == '0':
         print('Exitting App')
     elif main_menu_choice == '1':
         Menu_Logic()
     elif main_menu_choice == '2':
         Couriers_Logic()
     else:
         print("Invalid Input")

def Couriers_Logic():
     while True:
         All_Choice(Courier_choices)
         choice = input(f"Enter choice from 0 to 5:")
         if choice in ('0','1', '2', '3', '4','5'):
            if choice == '0':
               Start()
               break
            elif choice == '1':
                Display_menu(Couriers_list)
            elif choice == '2':
                Add_data(Couriers_list)
            elif choice == '3':
                Update_data(Couriers_list)
            elif choice == '4':
                Delete_Product(Couriers_list)
         else:
            print("Invalid Input")

def Menu_Logic():
     while True:
         All_Choice(Product_choices)
         choice = input(f"Enter choice from 0 to 5:")
         if choice in ('0','1', '2', '3', '4','5'):
            if choice == '0':
               Start()
               break
            elif choice == '1':
                Display_menu(Product_list)
            elif choice == '2':
                Add_data(Product_list)
            elif choice == '3':
                Update_data(Product_list)
            elif choice == '4':
                Delete_Product(Product_list)
         else:
            print("Invalid Input")

Start()