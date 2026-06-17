import pandas as pd
import matplotlib.pyplot as plt

print("="*50)
print("      CREDIT CARD FRAUD DETECTION")
print("="*50)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

try:
    df = pd.read_csv("creditcard.csv")

    print("\nDataset Loaded Successfully")
    print("\nFirst 5 Records:")
    print(df.head())

    print("\nDataset Shape :", df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistical Summary:")
    print(df.describe())

    # ------------------------------------------
    # Fraud vs Normal Transactions
    # ------------------------------------------

    fraud_count = len(df[df['Class'] == 1])
    normal_count = len(df[df['Class'] == 0])

    print("\nFraud Transactions :", fraud_count)
    print("Normal Transactions :", normal_count)

    # ------------------------------------------
    # Graph
    # ------------------------------------------

    labels = ["Normal", "Fraud"]
    values = [normal_count, fraud_count]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title("Fraud vs Normal Transactions")
    plt.xlabel("Transaction Type")
    plt.ylabel("Count")
    plt.show()

except:
    print("\nDataset not found.")
    print("Place creditcard.csv in the same folder.")

# ------------------------------------------
# Rule Based Detection Function
# ------------------------------------------

def check_transaction(amount, country, hour):

    risk_score = 0

    if amount > 50000:
        risk_score += 2

    if country.lower() != "india":
        risk_score += 2

    if 0 <= hour <= 4:
        risk_score += 1

    return risk_score

# ------------------------------------------
# User Input
# ------------------------------------------

print("\n")
print("="*50)
print("CHECK NEW TRANSACTION")
print("="*50)

amount = float(input("Enter Transaction Amount : "))
country = input("Enter Country : ")
hour = int(input("Enter Transaction Hour (0-23) : "))

risk_score = check_transaction(amount, country, hour)

# ------------------------------------------
# Result Decision
# ------------------------------------------

if risk_score >= 4:
    result = "FRAUD"
elif risk_score >= 2:
    result = "SUSPICIOUS"
else:
    result = "SAFE"

# ------------------------------------------
# Final Report
# ------------------------------------------

print("\n")
print("="*50)
print("CREDIT CARD FRAUD DETECTION REPORT")
print("="*50)

print("Transaction Amount :", amount)
print("Country            :", country)
print("Transaction Hour   :", hour)
print("Risk Score         :", risk_score)
print("Status             :", result)

if result == "FRAUD":
    print("\nALERT : Fraudulent Transaction Detected")
elif result == "SUSPICIOUS":
    print("\nWARNING : Transaction Needs Verification")
else:
    print("\nTransaction Approved")

print("="*50)

# ------------------------------------------
# Sample Risk Graph
# ------------------------------------------

categories = ["Amount Risk", "Country Risk", "Time Risk"]
scores = [2 if amount > 50000 else 0,
          2 if country.lower() != "india" else 0,
          1 if 0 <= hour <= 4 else 0]

plt.figure(figsize=(6,4))
plt.bar(categories, scores)
plt.title("Risk Factor Analysis")
plt.ylabel("Risk Score")
plt.show()

print("\nProgram Completed Successfully")
