# Ticket-analysis

In this fast-moving world, we have to constantly look for opportunities to optimize and improve IT operations.
AIOps will greatly help to classify your ticket data into buckets and then looking towards the biggest bucket data, you can think of the next set of automation or self-services portal/tool or improve documentation so that your end users/developers don't have to open tickets.
https://yadavmukund.blogspot.com/2023/06/aiops-for-tenant-and-platform-operations.html 
In this repo, you will find 2 files
## Ticket-Bucket.py:
In this example, we assume you have an Excel file named "tickets.xlsx" with a column called "Ticket Subject" containing the ticket subjects. We define the categories and their corresponding keywords in the categories dictionary.
The program then loads the Excel file into a DataFrame using the read_excel() function from the pandas library. It creates a new column called "Category" to store the assigned category for each ticket.
Next, it iterates over each ticket subject and checks if any of the keywords in the categories dictionary are present in the subject. If a match is found, the program assigns the corresponding category to the ticket.
Finally, the updated DataFrame is saved to a new Excel file named "categorized_tickets.xlsx" using the to_excel() function.
You can modify the categories dictionary to include your specific categories and keywords. Additionally, you may need to install the pandas library if you don't have it installed already (pip install pandas).
## Ticket-Bucket-ML.py
You can use machine learning (ML) algorithms to categorize ticket subjects into buckets. One popular approach is to use text classification algorithms. Here's an example using the scikit-learn library in Python.
we use the scikit-learn library to build a text classification model. The ticket subjects are split into the input data X, and the corresponding categories are stored in the target data y. We then use TF-IDF vectorization to convert the ticket subjects into numerical features.
A Linear Support Vector Classifier (LinearSVC) model is trained on the vectorized data. This model learns to classify ticket subjects into the appropriate categories based on the provided training data.
To categorize new ticket subjects, you can use the trained model and vectorizer. After vectorizing the new ticket subjects, the model predicts the categories for each subject. The predicted categories are then printed.
Finally, the trained model and vectorizer are saved using the joblib library for future use.
Note that this is a basic example, and you can further enhance the model's performance by exploring other algorithms, performing hyperparameter tuning, or using more advanced techniques like deep learning-based models.
