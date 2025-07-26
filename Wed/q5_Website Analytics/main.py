monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}


# 1. Find the total number of unique visitors who visited on any of the three days.

total_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
print(total_visitors)
print(len(total_visitors))

# 2. Identify users who visited on both Monday and Tuesday.
both_monday_tuesday = monday_visitors & tuesday_visitors
# print("Users who visited on both Monday and Tuesday:", both_monday_tuesday)

# 3.Determine which users visited for the first time each day (i.e., not seen on previous days).

# Monday – all are first-time visitors
monday_first_time = monday_visitors


# Tuesday – only those not seen on Monday
tuesday_first_time = tuesday_visitors - monday_visitors

previous_days = monday_visitors | tuesday_visitors
wednesday_first_time = wednesday_visitors - previous_days

loyal_visitors = monday_visitors & tuesday_visitors & wednesday_visitors
print("Loyal visitors (all 3 days):", loyal_visitors)



# Monday-Tuesday overlap
monday_tuesday = monday_visitors & tuesday_visitors
print("Monday & Tuesday:", monday_tuesday)

# Tuesday-Wednesday overlap
tuesday_wednesday = tuesday_visitors & wednesday_visitors
print("Tuesday & Wednesday:", tuesday_wednesday)

# Monday-Wednesday overlap
monday_wednesday = monday_visitors & wednesday_visitors
print("Monday & Wednesday:", monday_wednesday)
