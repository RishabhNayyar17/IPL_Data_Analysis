import pandas as pd
from matplotlib import pyplot as plt
import csv

ipl = pd.read_csv("C:\\Users\\risha\\OneDrive\\Desktop\ipldata.csv")
print(ipl)

print()

print(ipl.head())  # For 1st 5 Data Sets

print()

print(ipl.shape)   # For the Total No. of Rows and Columns or Data Sets

print()

print(ipl['player_of_match'].value_counts()) # For Most Man of the Match Awards

print()

print(ipl['player_of_match'].value_counts()[0:10]) # For Top 10 Man Of the Match Awards

print()

print(list(ipl['player_of_match'].value_counts()[0:5].keys())) # For Player Names Only
#
# print()
#
# plt.figure(figsize=(8,5))   # For Dimensions of X and Y Axis
# plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), list(ipl['player_of_match'].value_counts()[0:5]), color='g')
# plt.xlabel('Players')
# plt.ylabel('No. Of Matches')
# plt.savefig('1st Graph-Top 5 Man Of Match')
# plt.show()

print()

print(ipl['result'].value_counts())  # For the Frequency of Result Column

print()

print(ipl['toss_winner'].value_counts()) # For the No. of Toss Wins w.r.t each team

print()

batting_first = ipl[ipl['win_by_runs']!=0]  # For the Data where teams won by Batting first and !0 is because the teams who lost the match after batting are given 0
print(batting_first.head())

print()

# plt.figure(figsize=(5,7))   # For Dimensions of X and Y Axis
# plt.hist(batting_first['win_by_runs'])
# plt.title('Distribution Of Runs')
# plt.xlabel('Runs')
# plt.ylabel('Matches')
# plt.savefig('2st Graph-Win by Batting 1st')
# plt.show()

print()

print(batting_first['winner'].value_counts())

# For Top 3 Teams - Batting First
plt.figure(figsize=(6,6))   # For Dimensions of X and Y Axis
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()), list(batting_first['winner'].value_counts()[0:3]), color=["blue", "yellow", "orange"])
plt.savefig('3rd Graph- Top 3 Teams Won by Batting 1st')
plt.show()

# For Win % Data of Teams Batting 1st # We Have autopct to show %  and 0.1f means till 1st Decimal Place and f for floating point value
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()), labels=list(batting_first['winner'].value_counts().keys()), autopct= '%0.1f%%') # In Pie Chart, We 1st Pass Values and then Keys i.e -> It is opposite to that of Bar Graph
plt.savefig('4th Graph- Win % of Teams after Batting 1st')
plt.show()

print()

# For Win % Data of Teams Batting 2st OR Balling 1st
batting_second = ipl[ipl['win_by_wickets']!=0]      # As, Win by Wickets can't be 0
print(batting_second.head())

plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'], bins=30)
plt.xlabel('Wickets')
plt.ylabel('Matches')
plt.savefig('5th Graph- Win % of Teams after Batting 2nd')
plt.show()

print()

print(batting_second['winner'].value_counts())

# For Top 3 Teams - Batting Second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()), list(batting_second['winner'].value_counts()[0:3]), color=["purple", "blue", "red"])
plt.xlabel('Teams')
plt.ylabel('Matches')
plt.savefig('6th Graph- Top 3 Teams after Batting 2nd')
plt.show()

print()

# For Win % Data of Teams Batting 2st # We Have autopct to show %  and 0.1f means till 1st Decimal Place and f for floating point value
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()), labels=list(batting_second['winner'].value_counts().keys()), autopct= '%0.1f%%') # In Pie Chart, We 1st Pass Values and then Keys i.e -> It is opposite to that of Bar Graph
plt.savefig('7th Graph- Win % of Teams after Batting 2st')
plt.show()