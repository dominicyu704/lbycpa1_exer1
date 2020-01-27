
i = 1
while i<100:
    print("Engineering Formula Calculator")
    print()
    print("Which formula would you want to use?")
    print("[1] Acceleration = (Final Velocity - Initial Velocity / Time)")
    print("[2] Potential Energy = (Mass * Gravity * Height)")
    print("[3] Quit")

    choice = int(input("Your choice? "))
    if choice == 1:
        print("You have chosen the formula for Acceleration")
        print()
        print("[1] Acceleration")                   # Unit for Acceleration is meters per second squared (m/s^2)
        print("[2] Final velocity")                 # Unit for Velocity is meters per second (m/s)
        print("[3] Initial velocity")
        print("[4] Time")                           # Unit for Time is seconds (s)
        print("[5] Go back to menu")
        variable_1 = int(input("What variable would you like to solve? "))
        if variable_1 == 1:
            velocity1 = int(input("Insert value of final velocity "))
            velocity2 = int(input("Insert value of initial velocity "))
            time = int(input("Insert value of time "))
            acceleration = ((velocity1 - velocity2) / time)
            print("The acceleration is" ,acceleration)
            break
        elif variable_1 == 2:
            velocity3 = int(input("Insert value of initial velocity "))
            acceleration1 = int(input("Insert value of acceleration "))
            time1 = int(input("Insert value of time "))
            finalvelocity = (acceleration1 + velocity3 / time1)
            print("The final velocity is", finalvelocity)
            break
        elif variable_1 == 3:
            velocity4 = int(input("Insert value of final velocity "))
            acceleration2 = int(input("Insert value of acceleration "))
            time2 = int(input("Insert value of time "))
            initialvelocity = (-acceleration2 + velocity4 / time2)
            print("The initial velocity is", initialvelocity)
            break
        elif variable_1 == 4:
            velocity5 = int(input("Insert value of final velocity "))
            velocity6 = int(input("Insert value of initial velocity "))
            acceleration3 = int(input("Insert value of acceleration "))
            time = (velocity5 - velocity6 / acceleration3)
            print("The time is", time)
            break
        else:
            i+=1
    elif choice == 2:
        print("You have chose the formula for Potential Energy")
        print("[1] Potential Energy")       # Unit for Potential Energy is Joules (J)
        print("[2] Mass")                   # Unit for Mass is Kilograms (kg)
        print("[3] Height")                 # Unit for Height is Meters (m)
        print("[4] Go back to menu")
        variable_2 = int(input("What variable would you like to solve? "))
        if variable_2 == 1:
            mass1 = int(input("Insert value of mass "))
            height1 = int(input("Insert value of height "))
            potentialenergy = (mass1 * height1 * 9.8)
            print("The potential energy is ", potentialenergy)
            break
        elif variable_2 == 2:
            height1 = int(input("Insert value of height "))
            pe = int(input("Insert value of potential energy "))
            mass = (pe / 9.8 * height1)
            print("The mass is", mass)
            break
        elif variable_2 == 3:
            mass2 = int(input("Insert value of mass "))
            pe1 = int(input("Insert value of potential energy "))
            height = (pe1 / mass2 * 9.8)
            print("The height is", height)
            break
        else:
            i=+1
    else:
        i=200
