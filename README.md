# Election_Analysis

## Overview of Election Audit

The purpose of this Election audit was to determine the total amount of votes in the election, the turnout for each county while determining which had the largest county turnout, and figuring out how much vote each candidate received to determine who won.

## Election-Audit Results

- How many votes were cast in this congressional election?

![](https://github.com/Kevin-C3923/Election_Analysis/blob/main/Resources/total_votes.jpg)

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

![](https://github.com/Kevin-C3923/Election_Analysis/blob/main/Resources/county_votes.jpg)

- Which county had the largest number of votes?

![](https://github.com/Kevin-C3923/Election_Analysis/blob/main/Resources/largest_county_votes.jpg)

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

![](https://github.com/Kevin-C3923/Election_Analysis/blob/main/Resources/candidates_votes.jpg)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

![](https://github.com/Kevin-C3923/Election_Analysis/blob/main/Resources/winning_candidate.jpg)

## Election-Audit Summary

With the coding for this election audit, we were able to record county and candidate from a excel file while tallying votes of over 100 thousand of people. Therefor, with a few configuration we would be able to use the code for any other election. One of the first thing that needs to be edited would be the path to load and save file, example.

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

If we are going to use this code for other elections we need to be able to choice. A simple solution of course is just to edit the name for the excel and text file to the correct name, but that becomes time consuming and errors can occure if the person doesn't know what they are doing so we would have to find better solution.

Another thing that would be needed is some new initialization, as some election aren't about choicing a single candidate but as well other postion up for grab and policy that need public vote. In order to do that we would have make extra empty initialization in case their are multiple postion for an election and a boolean in case we have policy that is a simple yes or no. 

Once we store that new information and we need to be able to print it out. Which means we have to edit the print code not just to print out the new information, but to only print out what was given in the election information.


