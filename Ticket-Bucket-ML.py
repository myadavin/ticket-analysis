#===========================================================
# Objective: Machine Learning program to classify tickets
# This is a generic program to analyze any Ticket data set 
#===========================================================
# Version | Name           | Change details   | Date
#-----------------------------------------------------------
# 1.0     | Mukund Yadav   | Baseline version | 01-June-2023
#         |                |                  |
#         |                |                  |
#         |                |                  |
#===========================================================
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Load the Excel file into a DataFrame
data = pd.read_excel("tickets.xlsx")

# Split the data into input (ticket subjects) and target (categories)
X = data["Ticket Subject"]
y = data["Category"]

# Vectorize the ticket subjects using TF-IDF
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train a LinearSVC model for text classification
model = LinearSVC()
model.fit(X_vectorized, y)

# Categorize new ticket subjects
new_tickets = ["New ticket subject 1", "New ticket subject 2", ...]
new_tickets_vectorized = vectorizer.transform(new_tickets)
predicted_categories = model.predict(new_tickets_vectorized)

# Print the predicted categories
for ticket, category in zip(new_tickets, predicted_categories):
    print("Ticket:", ticket)
    print("Predicted Category:", category)
    print()

# Save the trained model and vectorizer for future use
import joblib
joblib.dump(model, "ticket_classifier_model.pkl")
joblib.dump(vectorizer, "ticket_vectorizer.pkl")
