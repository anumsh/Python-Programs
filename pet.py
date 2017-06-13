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
    
def sumOfFoodCost(pet_list):
  """ This function sums the cost of food of all instances"""
  sum_of_food_cost=0
  for pet in pet_list:
    sum_of_food_cost+= pet.food_cost_for_day
  return sum_of_food_cost
    

def stringFormat(pet_list):
           """ This function returns the unique formatted string"""
           string_formatted_list = [] # empty list
           for pet  in pet_list:
                      result = "The "+ pet.species + " says "+ pet.noise
                      string_formatted_list.append(result) # appending the values in string_formatted_list
           return (list(set(string_formatted_list)))

""" Pet objects/instances"""
spot=Pet("Spot","dog",5.00,"woof")  
fido=Pet("Fido","dog",7.00,"woof")  
jorge=Pet("jorge","dog",2.00,"yip")  

pet_list=[spot,fido,jorge]

print (spot.speak())   # woof
print (sumOfFoodCost(pet_list)) # 14.0
print (stringFormat(pet_list)) # ['The dog says yip', 'The dog says woof']
