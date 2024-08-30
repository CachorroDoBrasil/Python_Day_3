#asking user for the day of the week
# day_of_week = input("What day is it today?")
# print("Today is "+ day_of_week)
# Movies_this_week = input("What movies are you watching this week? ")
# print("I am watching "+ Movies_this_week + " this week")
# mood = input("How are you feeling today? ")
# print("I am feeling "+ mood )

#program was having syntax errors, turns out it was an error with the terminal

#data types for variables in python
#strings - text/words
# name = "john"
# #whenever it's wrapped in quotes, it's a string, single, double, but it has to end in the same type of quotes. Python sees this as a word
# year = "2024"
# #integers - whole numbers (ie: 1,2,3), don't have to be wrapped in quotes, otherwise it'll make the number into a word
# year = 2024
# #floats - decimal numbers (ie: 5.453, 3.99, 4.45)
# yearfourfromnow = 2028
# subtract = yearfourfromnow - year 
# print(subtract)
# #booleans - yes or no/true or false
# BigMac = 3.99
# DoublePounder = 4.99
# Total = BigMac + DoublePounder 
# print(Total)

# #boolean
# IsRaining = False
# print (IsRaining)
# #lists - a collection of items
# Groceries = ["apples", "Bananas", "Carrots"]
# print(Groceries)

#challenge 1
#you and your family are going to a movie and dinner, you need a list of movies to choose from, the place of the restaurant, & the address of the restaurant 
# you also need the time of the movie, dinnertime, and the name of the movie, while also accounting for the amount of people going. And the prices of all of them, while checking to see if the movie is going to play in the evening
#print the entire output into one sentence/string. 
movielist = input("Which movies have you selected for your family? ")
print ("you have selected the following movies for your family " + movielist)

place = input ("Select where your family will be eating for dinner ")
print ("You have decided to eat at " + place)

address = "1234 random place lol"
# movietime = input ("Will the movie play in the evening? ")
# if movietime == ("Yes"): print("You will watch the movie after eating dinner")
# if movietime == ("no"): print ("You will watch the movie before dinner")
movietime = "5:00 PM"
#I should've put set values instead of asking the user for more inputs


people = input ("how many people are you going to buy tickets for? ")
#type conversion
print ("You have decided to buy" + people + "tickets")


print ("You are going to see " + movielist +
       " at " + movietime +
       " You are going to eat at " + place + 
       " Which will be at " + address + 
       " ,about " + people + " will be coming")