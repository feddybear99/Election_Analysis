# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Make a total vote counter.
total_votes = 0
# Candidate options and candidate votes as a library.
candidate_options = []
candidate_votes = {}

# Step 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Step 2: Track the largest county and county voter turnout.
largest_county = ""
county_turnout = 0


# Open the election results and read the csv file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row (it starts 0,1,2).
        candidate_name = row[2]

        # Step 3. Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Step 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
             # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
         # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")

    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

 # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        c_votes = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_votes)/ float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (c_votes > county_turnout):
            county_turnout = c_votes
            largest_county = county_name
           
    # 7: Print the county with the largest turnout to the terminal.
            winning_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {county_name}\n"
            f"-------------------------\n") 

            print(winning_county_summary)


    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)


    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)