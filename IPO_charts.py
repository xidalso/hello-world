print ('How many people are attending your party?')
number_of_people = input ()
number_of_people = int(number_of_people)
slices = 2 * number_of_people
people = 2
pizzas = slices / 8


print (f"You are hosting {number_of_people}, and each person eats 2 slices of a pizza, you will need {pizzas} pizzas.")