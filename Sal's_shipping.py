Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def cost_ground_shipping(weight):
  small_flat_rate = 20.00
  if weight <= 2.0:
    return (weight*1.50) + small_flat_rate
  elif 6 >= weight > 2 :
    return (weight*3.00) + small_flat_rate
  elif 10 >= weight > 6:
    return (weight*4.00) + small_flat_rate
  else:
    return (weight*4.75) + small_flat_rate
print(cost_ground_shipping(8.4))
def cost_drone_shipping(weight):
  flat_charge = 0
  if weight <= 2:
    return (weight*4.50) + flat_charge
  elif 6 >= weight > 2:
    return (weight*9.00) + flat_charge
  elif 10 >= weight > 6:
    return (weight*12.00) + flat_charge
  else:
    return (weight*14.25) + flat_charge
print(cost_drone_shipping(1.5))

def cheapest_shipping(weight):
  if (cost_ground_shipping < cost_drone_shipping)and (cost_ground_shipping < cost_premium_shipping):
    print("You should ship using ground shipping,it will cost "+cost_ground_shipping(weight))


  


  
  


  