# packages
import pandas as pd
import csv

# load csv to data frame and sum total profit
df = pd.read_csv("budget_data.csv")

# lists/variables
total_months = df["Date"].value_counts()
total = df["Profit/Losses"].sum()
change_in_profit = 0
count = 0
starting = 0

monthly_changes = []
date = []


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
# print("Total: $")
# print("Average  Change: $")
# print("Greatest Increase in Profits: ")
# print("Greatest Decrease in Profits: ")
