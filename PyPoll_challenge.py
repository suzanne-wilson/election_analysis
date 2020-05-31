# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)
# Close the file.
# election_data.close()
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate and county options and candidate and county votes
candidate_options = []
county_options = []
#
# 1. Declare the empty dictionaries.
candidate_votes = {}
county_votes = {}

candidate_toprint = {}
county_toprint = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

biggest_county = ""
biggest_count = 0
biggest_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

      # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
          # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

       # Print the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county...
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)
          # 2. Begin tracking that county's vote count. 
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1
        # Save the results to our text file.
        # print(county_votes)

with open(file_to_save, "w") as txt_file:
    election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n"
                f"\nCounty Votes:"
                f"\n")
    print(election_results, end="")

    # header for county results
    # county_header = (
    #    f"County Votes:\n")

    # Save the final vote count to the text file.
    txt_file.write(election_results)    

    # Determine the percentage of votes for each county by looping through the counts.
    # 1. Iterate through the county list.
    for county in county_votes:
        # 2. Retrieve vote count of a county.
        votes = county_votes[county]

        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        # print(f"{county}: contributed {vote_percentage:.1f}% of the vote.") 
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each county, their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)        
        # Determine winning vote count and county
        # 1. Determine if the votes are greater than the winning count.
        if (votes > biggest_count) and (vote_percentage > biggest_percentage):

            # 2. If true then set biggest_count = votes and biggest_percent =
            # vote_percentage.
            biggest_count = votes
            biggest_percentage = vote_percentage
                # 3. Set the biggest_county equal to the county's name.
            biggest_county = county      
        
    # 4. Print the county name and percentage of votes.
    biggest_county_summary = (
            f"\n---------------------------------------------\n"
            f"Largest County Turnout: {biggest_county}\n"
            f"-----------------------------------------------\n")
    print(biggest_county_summary)

 #  Save the largest turnout county results to our text file.
    txt_file.write(biggest_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)    

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate      

    # 4. Print the candidate name and percentage of votes.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)   

# # MODULE 3 CHALLENGE
    # Create a list for the counties
    # Open the election results and read the file

    # Save the biggest county's results to the text file.
     # Save the final vote count to the text file.

# election_data.close()
