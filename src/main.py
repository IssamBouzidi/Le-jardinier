from models.vegetable import Vegetable
from enums.vegetable_enum import Vegetable_enum as ve
from models.garden import Garden
from models.gardner import Gardner


def menu():
    """
    menu funciton to allow user to choose a vegetable to plant
    Returns:
        vegetable enum: type of vegetable to plant
    """

    # while user did not chose the write vegetable
    while "vegetable not valid!":
        print('1: Tomato')
        print('2: Carrot')
        print('3: Pickle')
        # get user choice
        choice = int(input('What do you want to plant ? : '))
        
        # return the vegetable type of chosen vegetable
        if choice == 1:
            print('Tomato')
            return ve.TOMATO.value
        elif choice == 2:
            print('Carrot')
            return ve.CARROT.value
        elif choice == 3:
            print('Pickle')
            return ve.PICKLE.value
        else:
            print('vegetable not valid!')


def vegetable_manager():
    """
    application manager interface
    """

    # initialize a new garden with
    garden = Garden("Eden")

    # initialize a new gardner object 
    gardner = Gardner("Issam")

    # call menu to get user choice
    choice = menu()

    # plant vegetable bu gardner 
    vegetable_to_plant = gardner.plant(choice)

    # add grow value
    vegetable_to_plant.grow(9)

    # add planted vegetable to the garden
    garden.add(vegetable_to_plant)


    choice = menu()
    vegetable_to_plant = gardner.plant(choice)
    vegetable_to_plant.grow(8)
    garden.add(vegetable_to_plant)

    # print summary
    print(f'Garden: {garden.name}')
    print(f'Gardner: {gardner.name}')
    for veg in garden.list_vegetables:
        print(f'Vegetable: {type(veg).__name__}, number of seed: {veg.nbr_seed}')
    print(f'Vegetables type num: {Garden.type_vegetables}')
    print(f'Total seed sum: {garden.get_seed_sum()}')


if __name__ == '__main__':
    """
    main function
    """
    vegetable_manager()