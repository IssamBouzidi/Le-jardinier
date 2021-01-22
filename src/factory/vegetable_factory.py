from models.tomato import Tomato
from models.carrot import Carrot
from models.pickle import Pickle
from enums.vegetable_enum import Vegetable_enum

class Vegetable_Factory:

    @classmethod
    def plant(self, vegetable_id):
        
        if(vegetable_id == Vegetable_enum.TOMATO.value):
            return Tomato()
        
        elif(vegetable_id == Vegetable_enum.CARROT.value):
            return Carrot()

        elif(vegetable_id == Vegetable_enum.PICKLE.value):
            return Pickle()
        
        else:
            print('Vegetable not valid!')

