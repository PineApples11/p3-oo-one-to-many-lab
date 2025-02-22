class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]

    def __init__(self,name,pet_type,optional_owner=None):

        if pet_type not in self.PET_TYPES:
            raise Exception("Pet type is invalid")

        self.name=name
        self.pet_type=pet_type
        self.owner=optional_owner
        Pet.all.append(self)
        pass
    pass


    # @property
    # def pet_type(self):
    #     self._pet_type

    # @pet_type.setter
    # def pet_type(self,pet):
        
      
        
class Owner:
    def __init__(self,name):
        self.name=name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner=self
        else:
            raise Exception ("Couldnt add owner")
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

        
    pass