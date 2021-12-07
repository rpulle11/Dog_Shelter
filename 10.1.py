# Roshini Pulle 
# Assignment 10.1 
# Sources: Assignment 6.2 load_contact_list function, Lecture 8.1

dog_list = {}
def load_dog_list(filename):
    # Initilizes an empty dictionary
    # Opens a file the mode "rt" which allows the function to read the file as a text
    with open(filename,"rt") as file:
        # Iterates through a loop to read every line in the file
        for line in file:
            # .rstrip() strips the excess space line after every line
            line = line.rstrip()
            # Splits into a list at ","
            dog_name = line.split(",")
            # Defines the key and value pairs
            # The key is name
            dog_list[dog_name[0]] = {}
            dog_list[dog_name[0]]["name"] = dog_name[1][1:]
            dog_list[dog_name[0]]["age"] = dog_name[2][1:]
            dog_list[dog_name[0]]["hunger"] = dog_name[3][1:]
            dog_list[dog_name[0]]["sleep"] = dog_name[4][1:]

    return dog_list
print("Available Breeds: Siberian Husky, Pug, Pomerian, Poodle, Golden Retriever, German Shepard")

class Dog_shelter:
    def __init__(self,dog_list= {}, breed=""):
        self.breed = breed
        self.dog_list = dog_list
    def get_name(self):
        self.name = self.dog_list[self.breed]["name"]
        if self.breed in self.dog_list:
        # Returns the Dog's name 
            answer = self.breed + "'s name: " + self.name
            return answer
        else:
        # If the name isn't found, None is returned
            return print("Breed not found!")
    def get_age(self):
        self.age = self.dog_list[self.breed]["age"]
        if self.breed in self.dog_list:
        # Returns the Dog's age
            answer = self.breed + "'s age: " + self.age
            return answer
        else:
        # If the name isn't found, None is returned
            return print("Breed not found!")

    def get_hunger_level(self):
        self.hunger_level = self.dog_list[self.breed]["hunger"]
        if self.breed in self.dog_list:
        # Returns the Dog's hunger level 
            answer = self.breed + "'s hunger level: " + self.hunger_level 
            return answer
        else:
        # If the name isn't found, None is returned
            return print("Breed not found!")

    def get_sleep_level(self):
        self.sleep_level = self.dog_list[self.breed]["sleep"]
        if self.breed in self.dog_list:
        # Returns Dog's sleep level 
            answer = self.breed + "'s sleep level: " + self.sleep_level
            return answer
        else:
        # If the name isn't found, None is returned
            return print("Breed not found!")

    def set_location(self,location):
        # Creating private instance variable 
        self.__location = location
        # Returns the location 
        return "Location: " + self.__location
    def set_donation(self,donation):
        # Creating private instance variable 
        self.__donation = donation
        # Returns the donation 
        return "Donation Amount: $" + str(self.__donation)
# Stores the file in filename
filename = load_dog_list("/Users/roshinipulle/Downloads/Dogshelter.txt")


def main():
    # Creates an object of class Dog_shelter
    x = Dog_shelter()
    # Tests all the functions in class Dog_shelter
    x.__init__(dog_list, "Poodle")
    print(x.get_name())
    print(x.get_age())
    print(x.get_hunger_level())
    print(x.get_sleep_level())
    print(x.set_location("Santa Cruz"))
    print(x.set_donation(30))
    
if __name__ == "__main__":
    main()
