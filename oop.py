class Person:
    def __init__(self, name, age, gender):
        # Constructor method to initialize attributes
        self.name = name  # Assigning the 'name' attribute
        self.age = age    # Assigning the 'age' attribute
        self.gender = gender  # Assigning the 'gender' attribute

    def introduce(self):
        # Method to introduce the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Natasha", 20, "female")

# Calling the introduce method to display the person's information
person1.introduce()
