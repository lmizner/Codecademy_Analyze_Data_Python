# Start by importing NumPy as np.
import numpy as np


# All of Betty’s recipes call for milk, eggs, sugar, flour, and butter. For
# Create a NumPy array that represents this data. 
# Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes.
cupcakes = np.array([2, 0.75, 2, 1, 0.5])


# Betty’s assistant has compiled all of her recipes into a csv (comma-separated variable) file called recipes.csv.
# Load this file into a variable called recipes.
recipes = np.genfromtxt('recipes.csv', delimiter = ',')


# Display recipes using print.
# Each row represents a different recipe. Each column represents a different ingredient.
print(recipes)


# The 3rd column represents the number of eggs that each recipe needs.
# Select all elements from the 3rd column and save them to the variable eggs.
eggs = recipes[0:4, 2]
print(eggs)


# Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs.
results = [egg == 1 for egg in eggs]
print(results)


# Betty is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).
# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.
cookies = recipes[2]
print(cookies)


# Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch.
double_batch = cupcakes * 2
print(double_batch)


# Create a new variable called grocery_list by adding cookies and double_batch.
grocery_list = double_batch + cookies
print(grocery_list)






