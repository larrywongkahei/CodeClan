from .vehicle import Vehicle

class Motorbike(Vehicle):
    def start_engine(self):
        supers_start_val = super().start_engine()
        return(supers_start_val)