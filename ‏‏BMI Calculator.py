import os

def CalculateBMI(Weight, Height):
    BMI = (Weight / (Height ** 2))
    return BMI

def InterpretBMI():
    os.system("cls")
    Weight = int(input("Enter your weight in kg: "))
    Height = float(input("Enter your height in meters: "))
    BMI = CalculateBMI(Weight, Height)

    if BMI < 18.5:
        print("\nBMI = " + str(BMI) + ", You are underweight 😐")
        Choice = input("\n\nTry again?\n1- Yes\t0- No ")
        if (Choice == "1"):
            InterpretBMI()
        else:
            exit()

    elif BMI >= 18.5 and BMI < 25:
        print("\nBMI = " + str(BMI) + ", You are normal weight 😊")
        Choice = input("\n\nTry again?\n1- Yes\t0- No ")
        if (Choice == "1"):
            InterpretBMI()
        else:
            exit()

    elif BMI >= 25 and BMI < 30:
        print("\nBMI = " + str(BMI) + ", You are overweight 😅")
        Choice = input("\n\nTry again?\n1- Yes\t0- No ")
        if (Choice == "1"):
            InterpretBMI()
        else:
            exit()

    elif BMI >= 30 and BMI < 40:
        print("\nBMI = " + str(BMI) + ", You are so obese 😲")
        Choice = input("\n\nTry again?\n1- Yes\t0- No ")
        if (Choice == "1"):
            InterpretBMI()
        else:
            exit()


InterpretBMI()