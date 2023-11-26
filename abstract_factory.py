from abc import ABCMeta, abstractmethod, abstractproperty

class Icarbody(metaclass=ABCMeta):
    
    @abstractmethod
    def release_carbody(self):
        pass

class Tuningcarbody(Icarbody):

    def release_carbody(self):
        print("Tuning car carbody created")


class Exoticcarbody(Icarbody):

    def release_carbody(self):
        print("Exotic car carbody created")


class Iengine(metaclass=ABCMeta):

    @abstractmethod
    def release_engine(self):
        pass


class Tuningengine(Iengine):

    def release_engine(self):
        print("Tuning car engine created")


class Exoticengine(Iengine):

    def release_engine(self):
        print("Exotic car engine created")


class Iwheels(metaclass=ABCMeta):

    @abstractmethod
    def release_wheels(self):
        pass


class Tuningwheels(Iwheels):

    def release_wheels(self):
        print("Tuning car wheels created")


class Exoticwheels(Iwheels):

    def release_wheels(self):
        print("Exotic car wheels created")


class Ibrakes(metaclass=ABCMeta):

    @abstractmethod
    def release_brakes(self):
        pass


class Tuningbrakes(Ibrakes):

    def release_brakes(self):
        print("Tuning car brakes created")


class Exoticbrakes(Ibrakes):

    def release_brakes(self):
        print("Exotic car brakes created")


class Isuspension(metaclass=ABCMeta):

    @abstractmethod
    def release_suspension(self):
        pass


class Tuningsuspension(Isuspension):

    def release_suspension(self):
        print("Tuning car suspension created")


class Exoticsuspension(Isuspension):

    def release_suspension(self):
        print("Exotic car suspension created")


class Icar(metaclass=ABCMeta):
    
    @abstractmethod
    def release_car(self, carbody:Icarbody, engine:Iengine, wheels:Iwheels, brakes:Ibrakes, suspension:Isuspension):
        pass


class Tuningcar(Icar):

    def release_car(self, carbody: Icarbody, engine: Iengine, wheels: Iwheels, brakes: Ibrakes, suspension: Isuspension):
        print("Tuning car created")
        carbody.release_carbody()
        engine.release_engine()
        wheels.release_wheels()
        brakes.release_brakes()
        suspension.release_suspension()


class Exoticcar(Icar):

    def release_car(self, carbody: Icarbody, engine: Iengine, wheels: Iwheels, brakes: Ibrakes, suspension: Isuspension):
        print("Exotic car created")
        carbody.release_carbody()
        engine.release_engine()
        wheels.release_wheels()
        brakes.release_brakes()
        suspension.release_suspension()


class Ifactory(metaclass=ABCMeta):

    @abstractmethod
    def create_carbody(self) -> Icarbody:
        pass

    @abstractmethod
    def create_engine(self) -> Iengine:
        pass

    @abstractmethod
    def create_wheels(self) -> Iwheels:
        pass

    @abstractmethod
    def create_brakes(self) -> Ibrakes:
        pass

    @abstractmethod
    def create_suspension(self) -> Isuspension:
        pass

    @abstractmethod
    def create_car(self) -> Icar:
        pass


class Tuningfactory(Ifactory):

    def create_carbody(self) -> Icarbody:
        return Tuningcarbody()
    
    def create_engine(self) -> Iengine:
        return Tuningengine()
    
    def create_wheels(self) -> Iwheels:
        return Tuningwheels()
    
    def create_brakes(self) -> Ibrakes:
        return Tuningbrakes()
    
    def create_suspension(self) -> Isuspension:
        return Tuningsuspension()
    
    def create_car(self) -> Icar:
        return Tuningcar()
    

class Exoticfactory(Ifactory):

    def create_carbody(self) -> Icarbody:
        return Exoticcarbody()
    
    def create_engine(self) -> Iengine:
        return Exoticengine()
    
    def create_wheels(self) -> Iwheels:
        return Exoticwheels()
    
    def create_brakes(self) -> Ibrakes:
        return Exoticbrakes()
    
    def create_suspension(self) -> Isuspension:
        return Exoticsuspension()
    
    def create_car(self) -> Icar:
        return Exoticcar()
    

t_factory = Tuningfactory()
t_carbody = t_factory.create_carbody()
t_engine = t_factory.create_engine()
t_wheels = t_factory.create_wheels()
t_brakes = t_factory.create_brakes()
t_suspension = t_factory.create_suspension()
t_car = t_factory.create_car()

t_car.release_car(t_carbody, t_engine, t_wheels, t_brakes, t_suspension)

e_factory = Exoticfactory()
e_carbody = e_factory.create_carbody()
e_engine = e_factory.create_engine()
e_wheels = e_factory.create_wheels()
e_brakes = e_factory.create_brakes()
e_suspension = e_factory.create_suspension()
e_car = e_factory.create_car()

e_car.release_car(e_carbody, e_engine, e_wheels, e_brakes, e_suspension)