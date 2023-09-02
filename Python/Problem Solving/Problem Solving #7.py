# Problem 7
# Write a code to check for gender, height, weight
# - return Qualified if all conditions are met, otherwise, return Disqualified

def check_condition(gender, height, weight):
    condition = ""

    if gender == "male":
        if height < 165 or weight < 54:
            condition = "Disqualified"
        else:
            condition = "Qualified"
    elif gender == 'female':
        if height < 160 or weight < 48:
            condition = "Disqualified"
        else:
            condition = "Qualified"

    return condition


print(check_condition("male", 165, 55))

