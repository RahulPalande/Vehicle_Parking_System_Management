from re import L  # re is a package for regular experession
import time  # Importing time stamps
from datetime import datetime  # Importing Date and Time
import math  # Importing math for using maths function

# Creating Dictionary

assigned = dict()
BIKE_CHARGES = 10
CAR_CHARGES = 5
TRUCK_CHARGES = 2.5
vehicle_selection = dict()
CHARGES = [CAR_CHARGES, BIKE_CHARGES, TRUCK_CHARGES]


# Calculations
# 10 -> 60
# x -> 0.19
# 0.19*60/10


def welcomeMessage():
    e = print("Welcome to the SRH parking garage")
    print("Would you like to check-in or check-out?")
    checkin_checkout = int(input("Choose \n 1 for check-in \n 2 for check-out \n "))
    if checkin_checkout == 1:
        print("Welcome to check-in")
        return checkin_checkout
    elif checkin_checkout == 2:
        print("Welcome to check-out.Have a good ride")
        tokenNumber = int(input("Enter your token Number"))
        if tokenNumber in assigned.keys():
            checkOutDetails = assigned.pop(tokenNumber)
            checkInTime = checkOutDetails[0][0]
            minutes = ((time.time() - checkInTime) / 60.0)
            print("--------------Please be patient, we are calculating----------------")
            print("You checkedout after {} minutes".format(round(minutes, 3)))
            vehicleIndex = vehicle_selection[tokenNumber]
            Rate = ((minutes * CHARGES[vehicleIndex - 1]) / 60)
            val = math.ceil(round(((minutes * CHARGES[vehicleIndex - 1]) / 60), 3))
            # val=round(((minutes*CHARGES[vehicleIndex-1])/60), 3)
            val = round(Rate, 3)
            if val > 1:
                print("You have to pay {} Euros".format(val))
                print("Bye..! Have a wonderful day and a safe ride.")
            else:
                print("You have to pay {} Euro".format(val))
                print("Bye..! Have a wonderful day and a safe ride.")

            print("Now remaining check ins are", assigned)
        else:
            print("Token number doesnt exist.")
    else:
        print("please select the correct option")
        restart = input("do you wish to start again").lower()
        if restart == "yes":
            if welcomeMessage() == 1:
                processMsg(1)
        else:
            print("Thankyou for using this system")
            exit()


# Step 3
def processMsg(option):
    userName = input("What is your name ?")

    birthYear = int(input("Whats your birth year?"))
    age = int(2021 - birthYear)
    print("Your age is {} years".format(age))
    licenseNumber = input("enter your vehicle license number")
    print(licenseNumber)
    carBikeTruckIndex = int(input("choose \n 1 for cars \n 2 for bikes \n 3 for Trucks \n "))
    if carBikeTruckIndex == 1:

        print("car")
        if age > 50:
            l1 = list(range(76, 151))
            while l1[-1] in assigned:
                l1.pop()
            if l1:
                assigned[l1[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l1[-1]] = carBikeTruckIndex
                l1.pop()
                print("Your token number is ", l1.pop() + 1)
        elif age < 50:
            l1 = list(range(151, 226))
            l2 = list(range(226, 301))
            l3 = list(range(301, 376))
            while l3[-1] in assigned:
                l3.pop()
            while l2[-1] in assigned:
                l2.pop()
            while l1[-1] in assigned:
                l1.pop()
            if l3:
                assigned[l3[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l3[-1]] = carBikeTruckIndex
                l3.pop()
                print("Your token number is ", l3.pop() + 1)
            elif l2:
                assigned[l2[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l2[-1]] = carBikeTruckIndex
                l2.pop()
                print("Your token number is ", l2.pop() + 1)
            elif l1:
                assigned[l1[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l1[-1]] = carBikeTruckIndex
                l1.pop()
                print("Your token number is ", l1.pop() + 1)
            print(l1)
            print(l2)
            print(l3)
        print(assigned)
    elif carBikeTruckIndex == 2:
        print("bike")
        if age > 50:
            l1 = list(range(76, 151))
            while l1[-1] in assigned:
                l1.pop()
            if l1:
                assigned[l1[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l1[-1]] = carBikeTruckIndex
                l1.pop()
                print("Your token number is ", l1.pop() + 1)
        elif age < 50:
            l1 = list(range(151, 226))
            l2 = list(range(226, 301))
            l3 = list(range(301, 376))
            while l3[-1] in assigned:
                l3.pop()
            while l2[-1] in assigned:
                l2.pop()
            while l1[-1] in assigned:
                l1.pop()
            if l3:
                assigned[l3[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l3[-1]] = carBikeTruckIndex
                l3.pop()
                print("Your token number is ", l3.pop() + 1)
            elif l2:
                assigned[l2[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l2[-1]] = carBikeTruckIndex
                l2.pop()
                print("Your token number is ", l2.pop() + 1)
            elif l1:
                assigned[l1[-1]] = (
                (time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
                vehicle_selection[l1[-1]] = carBikeTruckIndex
                l1.pop()
                print("Your token number is ", l1.pop() + 1)
            print(l1)
            print(l2)
            print(l3)
        print(assigned)

    elif carBikeTruckIndex == 3:
        print("truck")
        l1 = list(range(1, 76))
        while l1[-1] in assigned:
            l1.pop()
        if l1:
            assigned[l1[-1]] = ((time.time(), datetime.today().strftime('%Y-%m-%d: %H-%M-%S')), userName, licenseNumber)
            vehicle_selection[l1[-1]] = carBikeTruckIndex
            l1.pop()
            print("Your token number is ", l1.pop() + 1)
        print(l1)
        print(assigned)


while True:
    welcomeMessageIndex = welcomeMessage()
    if welcomeMessageIndex == 1:
        processMsg(welcomeMessage)
