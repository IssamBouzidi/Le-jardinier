from models.vegetable import Vegetable
class Garden:
    """
    Garden class
    """
    
    # class attribute to stock number of vegetables planted in the garden
    type_vegetables = 0
    
    # initialize a garden object with name, list of vetables ans seed sum
    def __init__(self, name):
        self.name = name
        self.list_vegetables = []
        self.__seed_sum = 0

    # getter of seed sum
    def get_seed_sum(self):
        return self.__seed_sum

    # setter of a seed sum
    def set_seed_sum(self, seed_sum) -> bool:
        #BONUS 2 : Lorsque les graines sont supérieures à 30 dans le jardin afficher une erreur
        if self.__seed_sum + seed_sum < 30:
            self.__seed_sum += seed_sum
            return True
        return False

    # add funciton to add a new vegetables
    def add(self, vegetable):
        if self.set_seed_sum(vegetable.nbr_seed) == True:
            self._plant(vegetable)
        else:
            print("Can not add seed!")

    # protected function called by add function
    def _plant(self, vegetable):
        self.list_vegetables.append(vegetable)
        Garden.type_vegetables += 1
