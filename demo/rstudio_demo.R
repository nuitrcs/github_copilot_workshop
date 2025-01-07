# Script to analyze data about meditation and number of children

# The data (a CSV) are hosted here: https://raw.githubusercontent.com/emiliolehoucq/trainings/main/data/nhis_2022_data.csv

# Variables of interest:

#MEDITATE_A
#Meditation includes Mindfulness, Mantra, and Spiritual meditation. In meditation, a person focuses, stills, or quiets the mind. During the past 12 months, did you use any of these types of meditation?
#Asked if HHSTAT_A = 1 (Indicates person is the Sample Adult)
#1 = Yes
#2 = No
#7 = Refused
#8 = Not Ascertained
#9 = Don't know

#PCNTKIDS_A
#Number of children in Sample Adult family, top-coded 3+
#Asked if HHSTAT_A = 1
#0 = 0 children
#1 = 1 child
#2 = 2 children
#3 = 3+ children
#8 = Not ascertained

# Loading libraries
library(tidyverse)

# Read the data

# Print the first rows

# Get unique values of MEDITATE_A and count for each value

# Get unique values of PCNTKIDS_A and count for each value

# Get proportions for each unique value of MEDITATE_A

# For each value of PCNTKIDS_A, get the proportion of rows where MEDITATE_A = 1

# REMEMBER TO SHOW "# q:"
