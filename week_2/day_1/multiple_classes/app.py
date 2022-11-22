from modules.Car import *
from modules.Engine import *
from modules.Gearbox import *

engine = Engine(30)
gearbox = GearBox(2)
car = Car("Yellow", "Honda", engine, gearbox)

print(car.engine.volume)
print(car.engine.ignite())
