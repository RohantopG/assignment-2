#here i imported the datetime extention i had some problem so i learnt it from deepseek

from datetime import datetime

year = int(input("Enter birth year: "))
month = int(input("Enter birth month (1-12): "))
day = int(input("Enter birth day: "))

birth_date = datetime(year, month, day)
today = datetime.now()

age_days = (today - birth_date).days
age_years = age_days // 365
age_months = age_years * 12
age_hours = age_days * 24
age_minutes = age_hours * 60

print("\n--- Accurate Age Details ---")
print("Current Age:", age_years, "years")
print("Age in Months (approx):", age_months)
print("Age in Days:", age_days)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years until 100:", 100 - age_years)
