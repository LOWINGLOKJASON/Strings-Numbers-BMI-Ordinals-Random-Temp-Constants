#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/hirbbymrzc-lowinglokjason
#****************************************************************

# import random package for question 4, 5, 7
import random as random

#############
#Question #1
#############

# tests for equality and inequality with strings
car_brand = 'Koenigsegg'
print('Is car brand equal to Vorsteiner? I predict False.')
print(car_brand == 'Vorsteiner')

print('Is car brand equal to Dunlop? I predict True.')
print(car_brand != 'Dunlop')

# tests using the lower() method
car_brand = 'Koenigsegg'
print('Is car brand equal to koenigsegg(lower-cased)? I predict False.')
print(car_brand.lower() == 'Koenigsegg')

# numerical tests for equality and inequality
score = 100
print('Is the score equal to 100? I predict True.')
print(score == 100)

print('Is the score not equal to 120? I predict True.')
print(score != 120)

# greater than and less than, greater than or equal to, and less than and equal to
score = 100
print('Is the score greater than 120? I predict False.')
print(score > 120)

print('Is the score not greater than 120? I predict True.')
print(score < 120)

print('Is the score not greater or equal to 100? I predict True.')
print(score >= 100)

print('Is the score not greater or equal to 90? I predict False.')
print(score <= 90)

# tests that use and / or keyword operators
car_brand = 'Koenigsegg'
score = 100
print('Is the car brand Koenigsegg and it scores more than 110? I predict False.')
print(car_brand == 'Koenigsegg' and score >= 110)

print('Is the car brand Koenigsegg or it scores more than 110? I predict True.')
print(car_brand == 'Koenigsegg' or score >= 110)

# test if the item is in a list
car_parts = ['engine', 'suspension', 'chassis']
print('Is passenager one of the car parts? I predict False.')
print('passenager' in car_parts)

# test if the item is not in a list 
car_parts = ['engine', 'suspension', 'chassis']
print('Is passenager one of the car parts? I predict True.')
print('passenager' not in car_parts)

#############
#Question #2
#############

# input the weight in kilogram and height in meter
weight_kg = 65
height_m = 1.7

# create a formula as bmi
bmi = weight_kg/(height_m**2)

# list out the explanations if bmi fall into one of the ranges
if bmi < 18.5:
  print(f'The BMI is {bmi} kg/m² which is underweight.')
elif bmi >= 18.5 and bmi <= 24.9:
  print(f'The BMI is {bmi} kg/m² which is normal weight.')
elif bmi >= 25.0 and bmi <= 29.9:
  print(f'The BMI is {bmi} kg/m² which is overweight.')
elif bmi >= 30.0 and bmi <= 34.9:
  print(f'The BMI is {bmi} kg/m² which is obese class I.')
elif bmi >= 35.0 and bmi <= 39.9:
  print(f'The BMI is {bmi} kg/m² which is obese class II.')
else:
  print(f'The BMI is {bmi} kg/m² which is obese class III')

#############
#Question #3
#############

# store the numbers 1-9 in a list 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# use an if-elif-else chain inside the loop
for x in numbers:
  if x == 1:
    print(f'{x}st')
  elif x == 2:
    print(f'{x}nd')
  elif x == 3:
    print(f'{x}rd')
  else:
    print(f'{x}th')

#############
#Question #4
#############

# set a random number to the omputer
computer = random.randint(1, 10)
# assign a number to the player
player = 6

# list out the results if the above met one of the below conditions
if computer == player:
  print(f"The computer's number is {computer}. The player's number is {player}. They are the same!")
elif computer < player:
  print(f"The computer's number is {computer}. The player's number is {player}. The player's number is higher!")
else:
  print(f"The computer's number is {computer}. The player's number is {player}. The computer's number is higher!")

#############
#Question #5
#############
  
# Make two lists: card numbers and suits
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'spades', 'hearts']

# print out randomized card numbers and suits
print(f'You got the {random.choice(numbers)} of {random.choice(suits)}!')

# ########## Bonus Questions ###########################################

#############
#Question #6
#############

# create member list and candidate list of the exclusive club in Tasty Pizza
members = ['Mary', 'Arial', 'Ben', 'Jack', 'Tim']
candidates = ['Tim', 'Mary', 'Dom', 'Penny', 'Gary']

# Loop the candidate list to find any duplicate names on member list (the comparison case is insensitive), If yes, notify they are member; if not, let them know they are able to join and tell there is benefit of joining the club
for candidate in candidates:
  if candidate.lower() in ' '.join(members).lower():
    print(f'{candidate}, you are already a member.')
  else:
    print(f'{candidate}, you are able to join the exclusive club that will offer discount on pizza after joining the club.')

#############
#Question #7
#############

# Create the first random list with 1 dice
die = [random.randint(1, 6)]

# Create the second random list with 2 dices
dice = []
dice.append(random.randint(1, 6))
dice.append(random.randint(1, 6))

# Print the first and the second random lists
print(die)
print(dice)

#############
#Question #8
#############

# The temperature in Hong Kong is 19C 
hk = 19

# formulas of celsius, fahrenheit and kelvin
F = hk*9/5+32
K = (F-32)*5/9+273.15
C = K-273.15

# print the sentence with temperature in different units
print(f'The weather in Hong Kong is {K-273.15}C which is {hk*9/5+32}F and {(F-32)*5/9+273.15}K.')

#############
#Question #9
#############

# Find the constants through SciPy Constants
from scipy import constants 

# Find the kilometers per hour in each meter per second
print(constants.kmh)
# the result shows there is 0.2777777777777778 kilometers per hour as one meter per second.