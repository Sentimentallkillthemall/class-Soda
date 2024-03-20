class Soda:
    def __init__(self, taste):
        self.taste = taste

    def info (self):
        print(f"You have a soda with {self.taste} taste")

first_soda = Soda(taste='Cherry')
second_soda = Soda(taste='Apple & Grape')
third_soda = Soda(taste='Banana')
fouth_soda = Soda(taste='Pineapple & Mango')

first_soda.info()
second_soda.info()
third_soda.info()
fouth_soda.info()