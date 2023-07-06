#===========================================================
# Objective: Categorise the tickets using keywords
# This is a generic program to analyze any Ticket data set 
#===========================================================
# Version | Name           | Change details   | Date
#-----------------------------------------------------------
# 1.0     | Mukund Yadav   | Baseline version | 11-Apr-2022
#         |                |                  |
#         |                |                  |
#         |                |                  |
#===========================================================
import pandas as pd

# Load the Excel file into a DataFrame
data = pd.read_excel("tickets.xlsx")

# Define your categories and corresponding keywords
# Add more categories and keywords as needed
categories = {
    "Alert": ["alert"],
    "Access": ["access"],
    "Deploy": ["deploy", "sync"],
    "Patch": ["patch"],
    "Upgrade": ["upgrade"],
    "Log": ["log"],
    "Bounce": ["restart", "bounce", "stop", "start", "reboot", "shutdown", "health", "maintenance", "itcm", "phc", "fhc"],
    "Refresh": ["refresh"],
    "Storage": ["storage", "disk", "size", "space"],
    "Job": ["job"],
    "Restore": ["restore"],
    "Password": ["password"],
    "Certificate": ["cert"],
    "Vulnerabilities": ["vulnerabilities", "advisory", "security", "vuln"],
    "Category 1": ["keyword1", "keyword2", "keyword3"],
    "Category 2": ["keyword4", "keyword5"],
    "Category 3": ["keyword6", "keyword7", "keyword8"]
}

# Create a new column for the category
data["Category"] = ""

# Iterate over the ticket subjects and categorize them
for index, row in data.iterrows():
    subject = row["Ticket Subject"]
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in subject.lower():
                data.at[index, "Category"] = category
                break

# Save the updated DataFrame to a new Excel file
data.to_excel("categorized_tickets.xlsx", index=False)
