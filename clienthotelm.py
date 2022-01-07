
def perform_search_and_print(data,filename):
    ob1=open(filename,"r")
    filedata1 = ob1.readlines()
    ob1.close()
    for one in filedata1:
        ind = 0
        if data in one:
            print(one)
        else:
            ind += 1



def check_presence(data,filename):
    obj = open(filename,"r")
    file_data = obj.read()
    if file_data.__contains__(data):
        return True
    else:
        return False



def search_data():
    print("1 - Search for Hotel Names")
    print("2 - Search for Dishes")
    ch=input("Provide Your choice : ")
    if ch == '1':
        ob=open("all_hotels.txt",'r')
        print(ob.read())
        ob.close()
    elif ch=='2':
        ob1 = open("all_dishes.txt", 'r')
        print(ob1.read())
        ob1.close()
        



def order_data():
    print("1 - Order by Hotel")
    print("2 - Order by Dish")
    total = 0
    final = ""
    ch = input("Provide Your choice : ")
    if ch == '1':
        hname = input("Enter Hotel name to show available items : ")
        perform_search_and_print(hname, "all_dishes.txt")
        while True:
           order = input("Enter 1 to give order and to continue or Enter 0 to Exit : ")
           if order=="0":
               break
           else:
             dishname=input("Enter Dish name : ")
             p=check_presence(dishname,'all_dishes.txt')
             if p==True:
               dishcode = input("Enter Dish code : ")
               q = check_presence(dishcode, 'all_dishes.txt')
               if q==True:
                       obj1 = open("all_dishes.txt", 'r')
                       file_data_ls = obj1.readlines()
                       i = 0
                       while i < len(file_data_ls):
                           one_data = file_data_ls[i]
                           ls = one_data.split("-")
                           if one_data.__contains__(dishcode):
                               final += dishname + " :    " + str(ls[3]) + "\n"
                               total = total + int(ls[3])
                               break
                           else:
                               i += 1
                               break

               else:
                   print("invalid code")
             else:
               print("invalid")
        print("\nyour Bill is:")
        print(final, end="")
        print("Total Bill amount : ", total, "\n")




    elif ch == '2':
        dname = input("Enter dish to Order : ")
        p=check_presence(dname,"all_dishes.txt")
        if p==True:
          perform_search_and_print(dname, "all_dishes.txt")
          while True:
            order = input("Enter 1 to give order and to continue or Enter 0 to Exit : ")
            if order == "0":
                break
            else:
              dishcode = input("Enter Dish code : ")
              q = check_presence(dishcode, 'all_dishes.txt')
              if q == True:
                        obj1 = open("all_dishes.txt", 'r')
                        file_data_ls = obj1.readlines()
                        i = 0
                        while i < len(file_data_ls):
                            one_data = file_data_ls[i]
                            ls = one_data.split("-")
                            if one_data.__contains__(dishcode):
                                final += dname + " :    " + str(ls[3]) + "\n"
                                total = total + int(ls[3])
                                break
                            else:
                                i += 1
                                break

              else:
                print("invalid code")

          print("\nyour Bill is:")
          print(final, end="")
          print("Total Bill amount : ", total, "\n")
        else:
            print("invalid!!!")


while True:
    print("1 - Search for Hotel Nmaes and Dish")
    print("2 - Order by Hotel and by Dish")
    print("0 - Exit")
    ch = input("Provide your choice : ")

    if ch=='1':
        search_data()
    elif ch=='2':
        order_data()
    elif ch=='0':
        exit(0)
