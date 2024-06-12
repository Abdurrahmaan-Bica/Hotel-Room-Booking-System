def makeReservation(type_of_room, number_of_guests, has_beach_view, date_of_reservation):
    database = conn["hotelreservation"]
    colection = database["reservations"]

    reservations_list = [
        {"Type of Room": type_of_room, "Number of Guests": number_of_guests, "Beach View": has_beach_view,
         "Date of Reservation": date_of_reservation}]

    colection.insert_one(reservations_list)


def changeReservationDetails():
    pass


print("----- Welcome to Mozotel -----")

while True:
    try:
        userInput = int(input("1.Make a Reservation" + "\n" + "2. Change Reservation Details" + "\n" + "3. Exit \n"))
        if userInput < 1 or userInput > 3:
            print("The number you have inserted does not exist. Please try again!")
        elif userInput == 1:
            typeOfRoom = input("Type of Room (Standard / Double): \n").lower()
            numberOfGuests = int(input("Number of Guests: \n"))
            hasBeachView = input("With Beach View: (Yes/No) \n").lower()

            makeReservation(typeOfRoom, numberOfGuests, hasBeachView)

        elif userInput == 2:
            print('hello')


        else:
            print("Bye :)")
            break



    except ValueError:
        print("Please insert a valid number!")
    except Exception:
        print("Unspecified error!")
