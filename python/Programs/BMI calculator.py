#welcome
print("Welcome to BMI Calculating Engine")
print()
print("To calculate BMI in Kilograms and Metres, press 1")#module1
print("To calculate BMI in Kilograms and centiMetres ,press 2")#module2
print("To calculate BMI in Pounds and feets ,print 3")#module3
module=int(input())

#module 1; BMI in kgs and m.
if module==1:
    #input
    Weight=int(input("How much load you are contributing to mother earth?(the weight should be in kgs)"))
    Height=int(input("Are you High to touch the sky? Enter your height(in metres) to let us know "))
    #arithematics of module 1
    Height_square=Height*Height
    BMI=Weight/Height_square
    print("BMI is",BMI)
    #fokat ka gyan
    if BMI<18.5:
        print("Iam feared that you will be blown away with winds , sorry to say but you are under nourished ")
    elif BMI>24.5:
        print("You contribute lots of mass to the mother earth, try searching fat killing exercises. You are over nourished")
    else:
        print("you are doing it good , you are healthy :)")

#module 2; BMI in kgs and cm
elif module==2:
    #input
    Weight=int(input("How much load you are contributing to mother earth?(the weight should be in kgs"))
    Height=int(input("Are you High to touch the sky? Enter your height(in centi metres) to let us know "))
    #arithematics of module 2
    Height=Height/100
    Height_square=Height*Height
    BMI=Weight/Height_square
    print("BMI is",BMI)
    #fokat ka gyan
    if BMI<18.5:
        print("Iam feared that you will be blown away with winds , sorry to say but you are under nourished ")
    elif BMI>24.5:
        print("You contribute lots of mass to the mother earth, try searching fat killing exercises. You are over nourished")
    else:
        print("you are doing it good , you are healthy :)")
    
#module 3;BMI in Pounds amd Feets
elif module==3:
    #input
    Weight=int(input("How much load you are contributing to mother earth?(the weight should be in Pounds)"))
    Height=int(input("Are you High to touch the sky? Enter your height(in feets) to let us know "))
    #Arithematics of module 3
    Weight_in_grams=Weight*454
    Weight=Weight_in_grams/1000
    Height_in_cm=30.48*Height
    Height=Height_in_cm/100
    Height_square=Height*Height

    BMI=Weight/Height_square
    print("BMI is",BMI)
    #fokat ka gyan
    if BMI<18.5:
        print("Iam feared that you will be blown away with winds , sorry to say but you are under nourished ")
    elif BMI>24.5:
        print("You contribute lots of mass to the mother earth, try searching fat killing exercises. You are over nourished")
    else:
        print("you are doing it good , you are healthy :)")

