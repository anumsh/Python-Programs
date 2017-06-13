class Pet:
  """ The constructor with Pet class arguments"""
  def __init__(self,name,species,food_cost_for_day,noise):
    self.name=name
    self.species=species
    self.food_cost_for_day=food_cost_for_day
    self.noise=noise
    
  def speak(self):
    """ The speak method that will return the noise value of Pet instance"""
    return(self.noise)
    
spot=Pet("Spot","dog",5.00,"woof")  # creating the spot instance(object) of Pet class 
fido=Pet("Fido","dog",7.00,"woof")  # fido is the instance of Pet class
jorge=Pet("jorge","dog",2.00,"yip")  # jorge is the instance of Pet class

print spot.speak()   # prints the noise the pet-spot makes.

pet_list=[spot,fido,jorge]

def sumOfFoodCost(pet_list):
  """ This function sums the cost of food of all instances"""
  sum_of_food_cost=0
  for pet in pet_list:
    sum_of_food_cost+= pet.food_cost_for_day
  return sum_of_food_cost
    
print sumOfFoodCost(pet_list)  # 14.0

def stringFormat(pet_list):
           newstringlist = [] # empty list
           for pet  in pet_list:
                      result = "The "+ pet.species + " says "+ pet.noise
                      newstringlist.append(result) # appending the values in newstringlist
           return newstringlist

def uniqueStringFormat(newstringlist):
           uniqueList=set(newstringlist)
           uniqueList=list(uniqueList)
           return uniqueList

print uniqueStringFormat(stringFormat(pet_list)) # ['The dog says yip', 'The dog says woof']
