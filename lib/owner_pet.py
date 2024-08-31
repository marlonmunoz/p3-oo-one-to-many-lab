class Owner:
    def __init__(self, name):   # we will create an owner with a name
        self.name = name 

    def pets(self):  # this method will return all pets for a given owner
        return [pet for pet in Pet.all if pet.owner == self] # iterate over all pets and return the ones that have the owner we are looking for
    
    def add_pet(self, pet):  # this method will add a pet to the owner
        pet.owner = self

    def get_sorted_pets(self):
        def get_pet_name(pet):
            return pet.name
        return sorted(self.pets(), key=get_pet_name)

    def __repr__(self) -> str:  # this will be called when we print the object
        return f"<Owner {self.name}>"
    
    
class Pet:

    all = [] # this will store all instances of the Pet class

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] # list of valid pet types
    

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:  # check if the pet type is valid
            raise Exception(f"Invalid pet type. Must be one of: {self.PET_TYPES}")  # if not, raise an exception
        self.name = name
        self.pet_type = pet_type  # this will call the setter
        self.owner = owner
        Pet.all.append(self) # add the new instance to the list of all pets
     
    def __repr__(self) -> str: 
        return f"<Pet {self.name} {self.pet_type}>" # this will be called when we print the object


    

