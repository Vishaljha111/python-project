class Car:            # ← capital C
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def drive(self):
        self.is_running = True
        print(f"{self.year} {self.make} {self.model} is now driving.")

    def stop(self):
        self.is_running = False
        print(f"{self.year} {self.make} {self.model} has stopped.")