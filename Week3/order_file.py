from tracemalloc import start
import store_app as ap
import os 
import pickle
save = 'Data/'
order_file = "Order.txt"        

if not os.path.exists(save):
    os.mkdir(save)

order_file = os.path.join(save,order_file)

order_choice = ['[0].Main Menu','[1].Order list','[2].Place Order','[3].Update Order Status','[4].Update Existing Order','[5].Delete Order']

order_status = ['Oreder Recived','Preparing', 'Out of Delivery','Delivered']

default_order = {"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                 "customer_phone": "0789887334", "courier": 2, "status": "preparing"}

order_list = []
#order_list.append(default_order)


def load_order_data():
    try:
        with open(order_file,'r+') as f:
            order_list = [line.strip() for line in f]
        return order_list
        
    except FileNotFoundError:
        with open(order_file,'w+') as f:
            for listitem in order_list:
                for key,value in listitem:
                    f.write('%s:%s\n'%(key,value))
            return order_list



def write_into_order_file():
    with open(order_file, 'w+') as f:
            for listitem in order_list:
                # f.write('---------------------------\n')
                for key, value in listitem.items():
                    f.write('%s:%s\n' % (key, value))
                #f.write(str(listitem) + '\n')
             

def view_order():
    #order_list.clear()
    load_order_data()
    if len(order_list):
        order = 0
        try:
            while order <= (len(order_list)):
                if order <= len(order_list):
                    for i, value in order_list[order].items():
                        print(i, value)
                    ap.line_Space()
                    View_next_order = input(
                        'Please enter to view next order ({}/{}) or else PRESS E To exit='.format(order+1, len(order_list)))
                    ap.line_Space
                    order += 1

                if View_next_order == 'E':
                    break
            else:
                print('Sorry.! You don\'t have more order to view.')
                ap.line_Space
        except IndexError:
            print('Sorry.! You don\'t have more order to view.')
    

def place_order():
    try:
        customer_name = input('Please input customer name:')
        customer_address = input('Please input address:')        
        customer_phone_number = input('Please input phone number:')
        print('Please select couriers list below:')
        ap.Display_menu(ap.Couriers_list)
        ap.select_courier = int(input('Please select index='))
        ap.courier = ap.select_courier
        status = 'Order Recived'
        print('order status'+status)
        order_details = {'customer_name':customer_name, 'customer_address':customer_address,
                        'customer_phone_number':customer_phone_number,'courier':ap.courier,'status':status}
        order_list.append(order_details)
        print('Congratulation your order successfully placed.')
        write_into_order_file()
    except ValueError:
        print('Please enter valid input! try again')




def update_order_status():
    #order_list.clear()
    load_order_data()
    #order_list.pop()
    i=0
    try:
        if(len(order_list)>0):
            for data in order_list:
                ap.line_Space()
                i+=1
                print('Order no:-',i)
                ap.line_Space()
                for k,v in data.items():
                    print(k,v)

            ord_inx=int(input('Please select order for update status-:'))
            for i,v in enumerate(order_status, start=1):
                print(i,v)
            ord_sts=int(input('Please select order status:'))
            
            order_list[ord_inx-1]['status']=order_status[ord_sts-1]
            ap.line_Space()
            
            print('Your order status has been successfully updated.')
            ap.line_Space()
            for k,v in order_list[ord_inx-1].items():
                print(k,v)
            write_into_order_file()
        else:
            print('Sorry.! you don\'t have order.')
    except IndexError:
            print('Sorry.! please insert valid input.')  
    except ValueError:
            print('Sorry.! please insert valid input.') 

def update_order_data():
    try:
        #order_list.clear()
        load_order_data()
        #order_list.pop()
        i = 0
        if (len(order_list)>0):
            for data in order_list:
                ap.line_Space()
                i+=1
                print('Order No:', i)
                ap.line_Space()
                for (key,value) in data.items():
                    print(key,value)
            ap.line_Space()

            order_number = int(input('Please selcet order for update:'))
            ap.line_Space()
            for k,v in order_list[order_number-1].items():
                print(k,v)
                ap.line_Space()
                update_inx = input(f'Please enter {k}:')
                if update_inx == '':
                    print('Order Not Update')
                else:
                    order_list[order_number-1][key] = update_inx
            
            write_into_order_file()
            ap.line_Space()
            print('Your order successfully updated')
        
        else:
            print('Sorry! order is not update!!!!')
    
    except IndexError:
        print('You not update order data')
    except ValueError:
        print('Please enter valid input')

def delete_order():
    #order_list.clear()
    load_order_data()
    #order_list.pop()
    i=0
    try:
        if(len(order_list)>0):
            for data in order_list:
                ap.line_Space()
                i+=1
                print('Order No: ', i)
                ap.line_Space()
                for key,value in data.items():
                    print(key,value)
            order_number=int(input('Please select order number for delete:'))
            print(len(order_list))
            order_list.pop(order_number-1)
            write_into_order_file()
            ap.line_Space()
            print('Your order successfully updated')
        else:
            print('Sorry your input order not delete')
    except IndexError:
        print('You not delete order data')
    except ValueError:
        print('Please enter valid input')

def Order_Menu_Logic(data_list):
    while True:
        if (data_list == order_choice):
            ap.All_Choice(order_choice)
        choices = input(f'Enter choice from 0 to 5:')
        ap.line_Space()
        if choices in('0','1','2','3','4','5'):
            if choices == '0':
                ap.Start()
                break
            elif choices == '1':
                view_order()
            elif choices == '2':
                place_order()
            elif choices == '3':
                update_order_status()
            elif choices == '4':
                update_order_data()
            elif choices == '5':
                delete_order()
        else:
            print("Invalid Input")


if __name__ == '__main__':
    pass

# # def order_print():
# #     with open(order_file,'w+') as f:
# #         for key, value in default_order.items():
# #             f.write('%s:%s\n' %(key,value))



# # print(all_order_list)


# # order_print()


