import os
import csv
csvpath = os.path.join(".", "election_data.csv")
output_path = os.path.join(".","output.csv")

# Define all variables
vote_count = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0
khan_place = 0
correy_place = 0
li_place = 0
tooley_place = 0
vote_list = []

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    with open(output_path, "w", newline='') as csvoutput:
        csvwriter = csv.writer(csvoutput,delimiter =' ')
#   count all votes
        csvwriter.writerow(['Election Results'])
        csvwriter.writerow(['---------------------------'])
        print("Election Results")
        print("---------------------------")
        for row in csvreader:
            vote_count = vote_count + 1
            if row[2] == "Khan":
                khan_votes = khan_votes + 1
            if row[2] == "Correy":
                correy_votes = correy_votes + 1
            if row[2] == "Li":
                li_votes = li_votes + 1
            if row[2] == "O'Tooley":
                tooley_votes = tooley_votes + 1  
            
#   add total votes to a list
        csvwriter.writerow(["Total Votes:",vote_count])
        csvwriter.writerow(['---------------------------'])
        print(f"Total Votes: {vote_count}")
        print("---------------------------")
        vote_list.extend([correy_votes, khan_votes, li_votes, tooley_votes])

# sort the list from greatest to least to determine most votes received    
        sorted_list = sorted(vote_list,reverse=True)

# find where each candidate's votes received equals the correct place in list and print results of voting  
        for x in sorted_list:
            if x == khan_votes:
                csvwriter.writerow(["Khan:", (round((khan_votes/vote_count)*100,3)),"%", ((khan_votes))])
                print(f"Khan: {(round((khan_votes/vote_count)*100,3))}% ({khan_votes})")
            if x == correy_votes:
                csvwriter.writerow(["Correy:", (round((correy_votes/vote_count)*100,3)),"%", ((correy_votes))])
                print(f"Correy: {(round((correy_votes/vote_count)*100,3))}% ({correy_votes})")
            if x == tooley_votes:
                csvwriter.writerow(["Tooley:", (round((tooley_votes/vote_count)*100,3)),"%", ((tooley_votes))])
                print(f"O'Tooley: {(round((tooley_votes/vote_count)*100,3))}% ({tooley_votes})")
            if x == li_votes:
                csvwriter.writerow(["Li:", (round((li_votes/vote_count)*100,3)),"%", ((li_votes))])
                print(f"Li: {(round((li_votes/vote_count)*100,3))}% ({li_votes})")
    
        print("---------------------------")
        csvwriter.writerow(['---------------------------'])
# print election winner

        if sorted_list[0] == li_votes:
            csvwriter.writerow(["Winner:","Li"])
            print(f"Winner: Li")
        if sorted_list[0] == khan_votes:
            csvwriter.writerow(["Winner:","Khan"])
            print(f"Winner: Khan")    
        if sorted_list[0] == tooley_votes:
            csvwriter.writerow(["Winner:","Tooley"])
            print(f"Winner: O'Tooley")    
        if sorted_list[0] == correy_votes:
            csvwriter.writerow(["Winner:","Correy"])
            print(f"Winner: Correy")

        print("---------------------------")           
        csvwriter.writerow(['---------------------------'])