class Person:
    # constructor - initialize and construct a Person object
    def __init__(self, last_name, first_name, address, city, state, postcode):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.city = city
        self.state = state
        self.postcode = postcode

    def __str__(self):
        return f'{self.last_name}, {self.first_name}, {self.address}, {self.city}, {self.state}, {self.postcode}'
