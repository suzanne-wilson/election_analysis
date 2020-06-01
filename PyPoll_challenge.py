# MODULE 3 ASSIGNMENTS AND CHALLENGE
# Assignment summary instructions:
#   Open the data file.
#   Write down the names of all the candidates.
#   Add a vote count for each candidate.
#   Get the total votes for each candidate.
#   Get the total votes cast for the election.
#
# Challenge instructions:
#   1. Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
#   2. Create a list for the counties.
#   3. Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
#   4. Create an empty string that will hold the county name that had the largest turnout.
#   5. Declare a variable that represents the number of votes that a county received. Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. If not, add it to the list of county names.
#   6. Inside the with open() function where you are outputting the file, do the following:
#           Create three if statements to print out the voter turnout results similar to the results shown above.
#           Add the results to the output file.
#           Print the results to the command line.
############################################################################################################
#
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

   # Read the election results file
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #FOR LOOP FOR EACH ROW: Calculate summary stats.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        #CANDIDATE COUNTS
        # Print the candidate name from each row.
        candidate_name = row[2]

        # compile a list with unique candidate names found in the election file
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # END compile a list with unique candidate names found in the election file

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # END FOR LOOP FOR EACH ROW: Calculate summary stats.

        # COUNTY COUNTS
        # Print the county name from each row.
        county_name = row[1]

        # compile a list with unique county names found in the election file
        # If the county does not match any existing county...
        if county_name not in county_options:

            # Add it to the list of counties.
            county_options.append(county_name)
            
          # 2. Begin tracking that county's vote count. 
            county_votes[county_name] = 0

        # END compile a list with unique county names found in the election file

        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
        # END COUNTY COUNTS
    #END FOR ROW LOOP
# END Read the election results file

# OPEN OUTPUT FILE    
with open(file_to_save, "w") as txt_file:

    election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n"
                f"\nCounty Votes:"
                f"\n")

    # Print the election results to the terminal.
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)    

    # FOR LOOP TO CALCULATE COUNTY LEVEL RESULTS
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
  
        # if loop to determine county with largest turnout.
        if (votes > biggest_count) and (vote_percentage > biggest_percentage):

            # 2. If true then set biggest_count = votes and biggest_percent = vote_percentage.
            biggest_count = votes
            biggest_percentage = vote_percentage

            # 3. Set the biggest_county equal to the county's name.
            biggest_county = county      

        #END if loop to determine county with largest turnout.
    # END FOR LOOP TO CALCULATE COUNTY LEVEL RESULTS  
      
    # 4. Print the county name and percentage of votes.
    biggest_county_summary = (
            f"\n---------------------------------------------\n"
            f"Largest County Turnout: {biggest_county}\n"
            f"-----------------------------------------------\n")

    # print the largest turnout county results to the terminal.        
    print(biggest_county_summary)

    # Save the largest turnout county results to our text file.
    txt_file.write(biggest_county_summary)

    # FOR LOOP TO CALCULATE CANDIDATE LEVEL RESULTS
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:

        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]

        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)    

        # If loop to determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate    

        # END If loop to determine winning vote count and candidate
   # END FOR LOOP TO CALCULATE CANDIDATE LEVEL RESULTS

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # 4. Print the candidate name and percentage of votes to the terminal.
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)   

# END Open the election results output file
