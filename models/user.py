class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def get_complete_name(self):
        return self.firstName + " " + self.lastName