from abc import ABC

class Vegetable(ABC):

    @property
    def nbr_seed(self) -> int:
        return self._nbr_seed
    
    def __init__(self):
        self._nbr_seed = 0
    
    def grow(self, nbr_seed:int):
        self._nbr_seed += nbr_seed
        return self._nbr_seed

    def get_nbr_seed(self):
        return self._nbr_seed