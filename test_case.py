from main import ExistUser
from main import NewUser

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

exist_user_data = {}
for name in data:
    exist_user_data[name] = ExistUser(name, data[name][0], data[name][1])

# Test Case 1
# check all plan benefits
exist_user_data['Cahya'].check_benefit()

# Test Case 2
# check a user plan
exist_user_data['Shandy'].check_plan()

# Test Case 3
# upgrade an user plan (>24 month of usage)
exist_user_data['Cahya'].upgrade_plan('Premium Plan')

# Test Case 4
# New User using existing Referral Code
new_user = NewUser('Faizal')
new_user.pick_plan('Standard Plan', 'bagus-9f92')
