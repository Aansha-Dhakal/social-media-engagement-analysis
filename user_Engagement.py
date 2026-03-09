import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# loadng the dataset
df = pd.read_csv("users.csv")
#setting up the database 
print("First 5 rows:")
print(df.head())

print("\nDataset info:")
df.info()

print("\nSummary statistics:")
print(df.describe(include="all"))

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())
# preparing the data set and converting Date Joined to datetime
df["Date Joined"] = pd.to_datetime(df["Date Joined"])
# creating join year column
df["Join Year"] = df["Date Joined"].dt.year
# KPI calculations
# number of users by platform
platform_counts = df["Platform"].value_counts()
# average daily time spent by platform
average_time = df.groupby("Platform")["Daily Time Spent (min)"].mean().sort_values(ascending=False)
# average daily time spent by verified accounts
verification = df.groupby("Verified Account")["Daily Time Spent (min)"].mean()
verification1= df.groupby("Platform")["Verified Account"].value_counts()
# top 10 countries by number of users
country_counts = df["Country"].value_counts().head(10)

# users joined by year
join_year_counts = df["Join Year"].value_counts().sort_index()
# printing KPI results
print("\nUsers by Platform:")
print(platform_counts)

print("\nAverage Daily Time Spent by Platform:")
print(average_time)

print("\nAverage Daily Time Spent by Verification Status:")
print(verification)

print("\nTop 10 Countries by User Count:")
print(country_counts)

print("\nUsers Joined by Year:")
print(join_year_counts)

print("\nVerification by Plattform:")
print(verification1)

# visualizations
# chart 1: average time spent by platform
plt.figure(figsize=(8, 5))
average_time.plot(kind="bar")
plt.title("Average Time Spent by Platform")
plt.xlabel("Platform")
plt.ylabel("Average Daily Time Spent (min)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# chart 2: number of users by platform
plt.figure(figsize=(8, 5))
platform_counts.plot(kind="bar")
plt.title("Number of Users by Platform")
plt.xlabel("Platform")
plt.ylabel("Number of Users")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# chart 3: average time spent by verified vs non-verified
plt.figure(figsize=(6, 4))
verification.plot(kind="bar")
plt.title("Average Time Spent: Verified vs Non-Verified")
plt.xlabel("Verified Account")
plt.ylabel("Average Daily Time Spent (min)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# chart 4: top 10 countries by user count
plt.figure(figsize=(10, 5))
country_counts.plot(kind="bar")
plt.title("Top 10 Countries by User Count")
plt.xlabel("Country")
plt.ylabel("Number of Users")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# chart 5: user growth by join year
plt.figure(figsize=(8, 5))
join_year_counts.plot(kind="line", marker="o")
plt.title("User Growth by Year Joined")
plt.xlabel("Join Year")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.show()

#chart6:Distribution of Time Spent: Verified vs Non-Verified Users
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Verified Account", y="Daily Time Spent (min)")
plt.title("Distribution of Time Spent: Verified vs Non-Verified Users")
plt.xlabel("Verified Account")
plt.ylabel("Daily Time Spent (min)")
plt.show()