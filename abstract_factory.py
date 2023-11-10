from abc import ABCMeta, abstractmethod, abstractproperty

class AbstractCarFactory():

    __meta_class__ = ABCMeta

    @abstractmethod
    def carbody():
        """Create carbody"""

    @abstractmethod
    def engine():
        """Create engine"""

    @abstractmethod
    def wheels():
        """Create wheels"""

    @abstractmethod
    def brakes():
        """Create brakes"""

    @abstractmethod
    def suspension():
        """Create suspension"""


class TuningCarFactory(AbstractCarFactory):

    def __init__(self):
        print("Tuning car created")

    def carbody(self):
        print("Created car body for Tuning car")

    def engine(self):
        print("Created engine for Tuning car")

    def wheels(self):
        print("Created wheels for Tuning car")

    def brakes(self):
        print("Created brakes for Tuning car")

    def suspension(self):
        print("Created suspension for Tuning car")


class ExoticCarFactory(AbstractCarFactory):

    def __init__(self):
        print("Exotic car created")

    def carbody(self):
        print("Created car body for Exotic car")

    def engine(self):
        print("Created engine for Exotic car")

    def wheels(self):
        print("Created wheels for Exotic car")

    def brakes(self):
        print("Created brakes for Exotic car")

    def suspension(self):
        print("Created suspension for Exotic car")


tuning_car = TuningCarFactory()
tuning_car.carbody()
tuning_car.engine()
tuning_car.wheels()
tuning_car.brakes()
tuning_car.suspension()

print("-"*40)

exotic_car = ExoticCarFactory()
exotic_car.carbody()
exotic_car.engine()
exotic_car.wheels()
exotic_car.brakes()
exotic_car.suspension()
