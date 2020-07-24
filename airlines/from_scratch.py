import sys
from random import randint


def menu():
    """
    Va a pedir un input de teclado de tipo `int` (numerico), y lo que el usuario ingrese,
    lo va a poner en la variable `selected_choice`
    """
    selected_choice = int(input("Decime que queres hacer: "))
    return selected_choice


def seat_price(age):
    base_seat_price = 1500
    if age > 65:
        return base_seat_price * 0.9
    return base_seat_price


def plane_seats():
    """
    This method creates a matrix that simulates the plane,
    with n_rows of n_columns
    """
    plane = []
    n_rows = 28
    n_columns = 6
    for i in range(n_rows):
        plane.append([0] * n_columns)  # Is the same than plane.append([0, 0, 0, 0, 0, 0])

    return plane


def show_plane_seats(matrix):
    """
    Given a matrix, it prints each row of it and its index
    https://www.w3schools.com/python/ref_func_enumerate.asp
    """
    for index, row in enumerate(matrix):
        print("Row number: " + str(index + 1) + " --- " + str(row))


def ticket_purchase():
    passengers = [] # List of passengers.
    plane = plane_seats()
    selected_choice = menu()
    if selected_choice == 3:
        return
    elif selected_choice == 1:
        show_plane_seats(plane)
        customer_wants_to_pick_seat = want_to_pick_seat()
        if customer_wants_to_pick_seat:
            # In case the user wants to pick a seat
            """
            - Como lo diria en voz alta:
            asiento = dame_asiento()
            si es_invalido(asiento):
                asiento = dame_asiento()
                si es_invalido(asiento):
                    asiento = dame_asiento()

            - Como lo traduciria a python (pero repito asiento = dame_asiento()):  
            asiento = dame_asiento()
            while es_invalido(asiento):
                asiento = dame_asiento()
            
            - Una forma correcta de hacerlo:
            while True:
                asiento = dame_asiento()
                if es_valido(asiento):
                    break	
            """
            while True:
                chosen_row_number = int(input("Choose row number: "))
                chosen_column_number = int(input("Choose column number: "))
                if (chosen_row_number >= 1 and chosen_row_number <= 28) and (chosen_column_number >= 1 or chosen_column_number <= 6):
                    break

            plane[chosen_row_number - 1][chosen_column_number - 1] = 1
            show_plane_seats(plane)
        else:
            # In case the user does not want to pick a seat
            while True:
                """
                I'll try to assign a seat, and keep trying until I find some empty one. In case
                I find and empty one, I'll break
                """
                random_row_number = randint(1, 29)
                random_column_number = randint(1, 7)
                if plane[random_row_number - 1][random_column_number - 1] == 0:
                    plane[random_row_number - 1][random_column_number - 1] = 1
                    print(random_row_number, random_column_number)
                    show_plane_seats(plane)
                    break

        dni = int(input("Insert your DNI: "))
        passengers.append(dni)
        age = int(input("Insert your age: "))
        passenger_seat_price = seat_price(age)
        print(passenger_seat_price)



def want_to_pick_seat():
    """
    Defines if the user wants or doesn't want to pick a seat.
    """
    user_choice = str(input("Do you want to pick a seat?: "))
    print(user_choice)
    if user_choice == "yes":
        print("The user wants to pick a seat")
        return True
    if user_choice == "no":
        print("The user does not want to pick a seat")
        return False


def third_choice():
    """
    `sys.exit(0)` finished our program execution.
    """
    print("I'll exit because you chose option 3.")
    sys.exit(0)


if __name__ == "__main__":
    ticket_purchase()
