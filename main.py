from game_data import data
import random
import art
from replit import clear

#Random person A and B from a list. Make sure that A is not equal to B
def index():
  index_a = random.randint(0,49)
  index_b = random.randint(0,49)
  while index_b == index_a:
    index_b = random.randint(0,49)
  return [index_a, index_b]

#Assign information to candidate A and B
def assign(index_of_a,index_of_b):
  name_a = data[index_of_a]['name']
  description_a = data[index_of_a]['description']
  country_a = data[index_of_a]['country']

  name_b = data[index_of_b]['name']
  description_b = data[index_of_b]['description']
  country_b= data[index_of_b]['country']

  print(f"Compare A: {name_a}, {description_a}, from {country_a}")
  print(art.vs)
  print(f"Against B: {name_b}, {description_b}, from {country_b}")

score = 0
end_game = False

print(art.logo)
print("Which instagram account has higher follower?")

#assign index of A and B
num_a = index()[0]
num_b = index()[1]

#retrieve follower of A and B
follower_a = data[num_a]['follower_count']
follower_b = data[num_b]['follower_count']

assign(index_of_a = num_a, index_of_b = num_b)
choice = input("Type 'A' or 'B': ")

#Check answer of the user and calculate score
while not end_game:
  if ((choice == "A" and follower_a > follower_b) or (choice == "B" and follower_b > follower_a)):
    clear()
    score += 1
    num_a = num_b
    num_b = index()[0]
    follower_a = data[num_a]['follower_count']
    follower_b = data[num_b]['follower_count']

    print(art.logo)
    print(f"You are right. Current score is {score}.")

    assign(index_of_a = num_a, index_of_b = num_b)
    choice = input("Type 'A' or 'B': ")
  else:
    clear()
    print(art.logo)
    end_game = True
    print(f"Game over you got it wrong. Your final score is {score}")

