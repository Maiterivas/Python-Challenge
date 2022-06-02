# Python-Challenge
Homework 3 - Northwestern Data Science Boot Camp

For this challenge, we were asked to create 2 different codes to read through different CSV files and output text files also.

# PyBank:
This part consisted of analyzing the financial records of my company using the budget_data.csv file provided.

From here, the Python script analyzed the CSV file and successfully calculated:

-The total number of months included in the dataset

-The net total amount of "Profit/Losses" over the entire period

-The changes in "Profit/Losses" over the entire period, and then the average of those changes

-The greatest increase in profits (date and amount) over the entire period

-The greatest decrease in profits (date and amount) over the entire period

This same script was able to output these results into the terminal and a separate .txt file within the "Analysis" folder of this project:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```
  
  # PyPoll:
  
The second part consisted of analyzing the election results of a small, rural town using the election_data.csv file provided.

From there, the Python script analyzed the CSV file provided and calculated:

-The total number of votes cast

-A complete list of candidates who received votes

-The percentage of votes each candidate won

-The total number of votes each candidate won

-The winner of the election based on popular vote.

The same script was also able to successfully output these results into the terminal and a .txt file within the "Analysis" folder of this project:

  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```
