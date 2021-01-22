from models.vegetable import Vegetable
from factory.vegetable_factory import Vegetable_Factory
from models.garden import Garden

class Gardner:
    """
    Gardner class, allow to add a gardner object, and plant a vegetable
    """

    def __init__(self, name):
        self.name = name

    def plant(self, vegetable):
        """
        function to plant a vegetable
        Args:
            vegetable (enum): vegetable from enum

        Returns:
            vegetable: use a facgtory to return a vegetable sub class type 
        """

        # use a factory to return the object of the chosen vegetable
        return Vegetable_Factory.plant(vegetable)