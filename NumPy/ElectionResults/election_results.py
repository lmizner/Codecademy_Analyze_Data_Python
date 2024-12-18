# Election Results
# You’re part of an impartial research group that conducts phone surveys prior to local elections. During this election season, the group conducted a survey to determine how many people would vote for Cynthia Ceballos vs. Justin Kerrigan in the mayoral election.
# Now that the election has occurred, your group wants to compare the survey responses to the actual results.
# Was your survey a good indicator? Let’s find out!


# First, import numpy and matplotlib.
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']


# Calculate the number of people who answered ‘Ceballos’ and save the answer to the variable total_ceballos.
# Print the variable to the terminal to see its value.
total_ceballos = sum([1 for response in survey_responses if response == 'Ceballos'])
print(total_ceballos)


# Calculate the percentage of people in the survey who voted for Ceballos and save it to the variable percentage_ceballos.
# Print the variable to the terminal to see its value.
survey_length = len(survey_responses)

percentage_ceballos = (total_ceballos/survey_length) * 100
print(percentage_ceballos)


# Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town’s population as its parameters.
# Then divide the distribution by the number of survey responses.
# Save your calculation to the variable possible_surveys.
possible_surveys = np.random.binomial(survey_length, 0.54, size = 10000) / survey_length


# Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.
plt.hist(possible_surveys, range = (0, 1), bins = 20)
plt.show()


# Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote and save it to the variable ceballos_loss_surveys.
# Print the variable to the terminal.
possible_surveys_length = float(len(possible_surveys))
incorrect_predictions = len(possible_surveys[possible_surveys < 0.5])

ceballos_loss_surveys = (incorrect_predictions / possible_surveys_length) * 100
print(ceballos_loss_surveys)


# Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people. 
# Divide the distribution by the size of the survey and save your findings to large_survey.
large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size = 10000) / large_survey_length

plt.close()
plt.hist(possible_surveys, range = (0, 1), bins = 20)
plt.hist(large_survey, alpha = 0.5, range = (0, 1), bins = 20)
plt.show()


# Now, recalculate the percentage of surveys that would have an outcome of Ceballos losing and save it to the variable ceballos_loss_new, and print the value to the terminal.
incorrect_predictions = len(large_survey[large_survey < 0.5])
ceballos_loss_new = incorrect_predictions / large_survey_length
print(ceballos_loss_new)

