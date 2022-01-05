# The data that needs to be retrieve.

# 1. Total number of votes casted
# 2. A list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The number of votes each candidate won
# 5. The winner of the election based on popular vote.

import os
import csv

# Assiging variable for file to load and it's path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
     txt_file.write("Counties in the Election")
     txt_file.write("\n---------------------------\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")

     


