import unittest
from modules.Car import *
from modules.Engine import*
from modules.Gearbox import *

class Test(unittest.TestCase):
    def test_engine_volume(self):
        engine1 = Engine(2)
        result = engine1.volume
        self.assertEqual(2, result)

    def test_engine_ignite(self):
        result = Engine.ignite(self)
        self.assertEqual("Engine Started", result)

    def test_gearbox_num(self):
        gearbox = GearBox(2)
        result = gearbox.num_of_gears
        self.assertEqual(2, result)

    def test_gearbox_Shiftgear(self):
        result = GearBox.shift_gear(self)
        self.assertEqual("Gear shifted", result)

    def test_gearbox_engage(self):
        result = GearBox.engage(self)
        self.assertEqual("clutch engaged", result)
        
    def test_car_ignite(self):
        gearbox = GearBox(20)
        engine = Engine(2)
        car1 = Car("yellow", "honda", engine, gearbox)
        result = car1.colour
        self.assertEqual("yellow", result)

if __name__ == '__main__':
    unittest.main()
