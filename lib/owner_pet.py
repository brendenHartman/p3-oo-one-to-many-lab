class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner = ""):
        self.name = name
        Pet.set_pet_type(pet_type)
        self.owner = owner
        Pet.all.append(self)

    @classmethod

    def get_pet_type(cls):
        return cls.pet_type
    
    @classmethod

    def set_pet_type(cls, pet_type):
        if pet_type in Pet.PET_TYPES:
            cls.pet_type = pet_type
        else:
            raise Exception()

    pet_type = property(get_pet_type, set_pet_type)
    

class Owner:

    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception()

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)