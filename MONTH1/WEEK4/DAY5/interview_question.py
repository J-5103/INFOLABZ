

AC="off"

is_stop=False

while True:
    if is_stop==False:
        user_input = input("please anter AC off orr on")
        if AC=="off":
            if user_input=="off":
                print("AC is already off")
            elif user_input=="on":
                AC="on"
                print("AC is on now")
        elif AC=="on":
            if user_input=="on":
                print("Ac is already on")
            elif user_input=="off":
                AC="off"
                print("AC is off now")

        else:

            user = input("do you want to stop this process?---yes/no:")
            if user == "yes":
                break
            if user == "no":
                is_stop = False









