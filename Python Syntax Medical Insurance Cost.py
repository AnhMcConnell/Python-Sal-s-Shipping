Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # create the initial variables below
age = 28
sex = 0
smoker = 0
num_of_children = 3
bmi = 26.2

# Add insurance estimate formula below
insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

print(insurance_cost)
print("This person's insurance cost is {} dollars.".format(insurance_cost))

# Age Factor
age += 4
new_insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is {} dollars.".format(change_in_insurance_cost))

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is {} dollars".format(change_in_insurance_cost))


# Male vs. Female Factor
bmi  = 26.2
sex = 1

new_insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is {} dollars.".format(change_in_insurance_cost))

# Extra Practice

smoker = 1

new_insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female and is a smoker is {} dollars.".format(change_in_insurance_cost))

sex = 0

new_insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being female and is a smoker is {} dollars.".format(change_in_insurance_cost))

smoker = 0
sex = 1
num_of_children = 5

new_insurance_cost = 250*age - 128*sex + 370*bmi +425*num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being a male and have 5 children is {} dollars.".format(change_in_insurance_cost))



