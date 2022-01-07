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

total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning candidate, votes and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:


    file_reader = csv.reader(election_data)        
    
    # read header
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # Condition to make sure we have the candidate only once
        if candidate_name not in candidate_options:
            #Add candidate name to the list
            candidate_options.append(candidate_name)
            # Begin tallying votes
            candidate_votes[candidate_name] = 0
        
        
        # Add a vote to that Candidate
        candidate_votes[candidate_name] += 1 


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
      # Save the final vote count to the text file.
    txt_file.write(election_results)


    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage =  float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

          # Determing the winning candidate and the amount they won count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If the votes and percentage is greater then the winning votes and percentage, 
            # then we will change it to that amount
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
  