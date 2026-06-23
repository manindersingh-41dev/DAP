def cel_to_Far(cel):
    far = (cel*(9/5)) + 32
    return far

def cel_to_kel(cel):
    kel = (cel+273.15)
    return kel

def far_to_cel(far):
    cel = (5/9) * (far-32)
    return cel

def far_to_kel(far):
    kel = cel_to_kel(far_to_cel(far))
    return kel

def kel_to_cel(kel):
    cel = kel-273.15
    return cel

def kel_to_far(kel):
    far = cel_to_Far(kel_to_cel(kel))

if __name__ == "__main__":
    while True:

        print(f"{'*'*20}\nPress C to Convert from Celcius\nPress F to convert from Fahrenheit\nPress K to convert from Kelvin\nPress Q to quit\n{'*'*20}")
        from_temp = input("Enter from which temperature to convert: ")
        if from_temp.lower() == 'q':
            break
        
        if from_temp.upper() == "C":
            print(f"\n\n{'*'*20}\nPress F to convert to Fahrenheit\nPress K to convert to Kelvin\n{'*'*20}")
            to_temp = input("Enter which temperature to convert to: ")
            temp = float(input("Enter value of temperature: "))

            if to_temp.lower() == 'f':
                conv_temp = cel_to_Far(temp)
                print(f"\t\t\t\t\t\t\tConverted Temprature: {conv_temp}\n")
            elif to_temp.lower() == 'k':
                conv_temp = cel_to_kel(temp)
                print(f"\t\t\t\t\t\t\tConverted Temprature: {conv_temp}\n")
            else:
                print("invalid choice")
            

        elif from_temp.upper() == "F":
            print(f"\n\n{'*'*20}\nPress C to convert to Celsius\nPress K to convert to Kelvin\n{'*'*20}")
            to_temp = input("Enter which temperature to convert to: ")
            temp = float(input("Enter value of temperature: "))

            if to_temp.lower() == 'c':
                conv_temp = far_to_cel(temp)
                print(f"\t\t\t\t\t\t\tConverted Temprature: {conv_temp}\n")
            elif to_temp.lower() == 'k':
                conv_temp = far_to_kel(temp)
                print(f"\t\t\t\t\t\t\tConverted Temprature: {conv_temp}\n")
            else:
                print("invalid choice")

        elif from_temp.upper() == "K":
            print(f"\n\n{'*'*20}\nPress C to convert to Celsius\nPress F to convert to Fahrenheit\n{'*'*20}")
            to_temp = input("Enter which temperature to convert to: ")
            temp = float(input("Enter value of temperature: "))

            if to_temp.lower() == 'c':
                conv_temp = kel_to_cel(temp)
                print(f"\t\t\t\t\t\t\tConverted Temprature: {conv_temp}\n")
            elif to_temp.lower() == 'f':
                conv_temp = kel_to_far(temp)
                print(f"\t\t\t\t\t\t\tConverted Temprature: {conv_temp}\n")
            else:
                print("invalid choice")
        
        else:
            print("Invalid choice")