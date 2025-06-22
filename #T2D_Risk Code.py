#Ask the user their height, weight, family history of diabetes, how many relatives have the disease, the user's age, the user's ethnicity, and other factors, and calculate their risk of Type II Diabetes.
#This version of the program was written by Yamir Richmond on Thursday, June 19, 2025.
def calculate_bmi(feet, inches, lbs): #Python will show a weak warning if the parameters are the same as the names of variables in the program.
    return 702.9 * lbs/(((12 * feet) + inches) ** 2) #The value is the user's BMI.
def calculate_moderate_minutes(minutes):
    return 150 - (2 * minutes)
def calculate_risk(BMI, Activity, eats_healthy, has_been_diagnosed, is_over_45, is_vulnerable_race, is_a_smoker, is_a_drinker, has_disrupted_sleep, has_good_mental_health, has_bad_mental_health, has_large_waist, struggles_with_symptoms, eats_unhealthy, user_members): #Function declaration of calculate_risk().
    t2d_risk = 0 #t2d_risk is the user's risk of Type II Diabetes, and it is initialized as 0.
    if BMI: #Most of these if statements will increase the risk of Type II Diabetes if true, and will have no change to the risk if false.
        t2d_risk += 9.6 #This value to this factor was calculated and/or specifically researched. Thus, this shouldn't be altered.
    else:
        t2d_risk += 0
    if Activity: #Activity and BMI are uppercase because I did not want to write different variable names for parameters that would be difficult to remember.
        t2d_risk -= 16 #This if statement will decrease the risk of Type II Diabetes if true, and will not change the risk if false.
    else:
        t2d_risk += 0
    if eats_healthy:
        t2d_risk -= 20 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if has_been_diagnosed:
        t2d_risk += 30 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if is_vulnerable_race:
        t2d_risk += 5 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if is_a_drinker:
        t2d_risk += 10 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
        t2d_risk += 0
    if has_disrupted_sleep:
        t2d_risk += 0
    else:
        t2d_risk -= 10 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    if has_good_mental_health:
        t2d_risk -= 5 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if has_bad_mental_health:
        t2d_risk += 5 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if has_large_waist:
        t2d_risk += 10 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if struggles_with_symptoms:
        t2d_risk += 15 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    if eats_unhealthy:
        t2d_risk += 15 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else:
        t2d_risk += 0
    t2d_risk += is_a_smoker #is_a_smoker is a numeric value, not a boolean.
    if is_over_45: #Age as a risk factor works differently because it increases the risk of Type II Diabetes multiplicatively.
        t2d_risk = t2d_risk * 1.1 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    if user_members == 0: #How many members a user has in their lineage that has Type II Diabetes also somewhat works differently. The more members a person has in their family that has Type II Diabetes, the greater the multiplicative factor is of their Type II Diabetes risk.
        t2d_risk += 0
    elif user_members == 1:
        t2d_risk = t2d_risk * 2 #This value to this factor was calculated and/or specifically researched. Thus, this shouldn't be altered.
    elif user_members > 1:
        t2d_risk = t2d_risk * 3 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    return t2d_risk #This is the final line of the function calculate_risk().
user_height_ft = str(input("What is your height? (ft)\n")) #This is the first question of the program.
while user_height_ft < 1: #Input validation so the user enters a positive value for their height.
    user_height_ft = int(input("Invalid. What is your height? (ft)\n")) #Using #int(input()) is important because it converts the user's answer to an integer.
user_height_in = int(input("\nWhat is your height? (in)?\n"))
while user_height_in < 0 or user_height_in >= 12: #Input validation for entering the user's height.
        user_height_in = int(input("\nInvalid. What is your height? (in)\n"))
user_weight = float(input("\nWhat is your weight? (lbs)\n"))
while user_weight <= 0: #Input validation for entering the user's weight.
    user_weight = float(input("\nInvalid. What is your weight? (lbs)\n"))
user_bmi = calculate_bmi(user_height_ft, user_height_in, user_weight) #The goal is to make the function that calculates the risk for Type II Diabetes as simple as possible. Thus, these other calculations must be made in these other functions.
if user_bmi >= 25: #These if statements will determine the value of boolean variables. The boolean variables will be passed to the calculate_risk() function.
    bmi_over_25 = True
else: #This else statement, indicating the boolean variable is False otherwise, is a necessity. If not included, the boolean variable might not be initialized when it's passed into the function.
    bmi_over_25 = False
print("Your BMI is " + str(user_bmi) + ".") #To tell the user what their BMI is.
family_history = input("\nDoes anyone in your blood family have Type II Diabetes?\n")
while family_history != "YES" and family_history != "yes" and family_history != "Yes" and family_history != "No" and family_history != "NO" and family_history != "no": #Input validation to limit the user's responses to either "Yes" or "No".
    family_history = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if family_history == "YES" or family_history == "yes" or family_history == "Yes":
    number_of_members = int(input("\nHow many members?\n"))
    while number_of_members < 1: #Input validation so the user enters a positive number for the number of family members that have Type II Diabetes.
        number_of_members = int(input("\nPlease enter a positive value.\n")) #The value must be at least 1 because the user indicated that they have at least one family member that has Type II Diabetes.
else:
    number_of_members = 0 #Number of members with diabetes because there will be more than 2 possible values for how the T2D risk can change.
user_age = int(input("\nHow old are you?\n"))
while user_age < 1: #Input validation to make sure the user entered a positive number.
    user_age = int(input("Invalid. What is your age?\n")) #Always use int(input()) whenever the user is supposed to type an integer value.
if user_age >= 45: #Many of these variables will be boolean, so the risk of Type II Diabetes will increase.
    over_45 = True #This value is a boolean.
else:
    over_45 = False
race = input("What is your race? (Please type the LETTER, not the whole race.)\nA. White\nB. African American\nC. Asian American\nD. Hispanic/Latino\nE. Pacific Islander\nF. Other\n")
while race != "A" and race != "a" and race != "B" and race != "b" and race != "C" and race != "c" and race != "D" and race != "d" and race != "E" and race != "e" and race != "F" and race != "f": #Input validation to limit the user's responses to either 'A', 'B', 'C', 'D', 'E', or 'F'.
    race = str(input("\nPlease select from one of the available letters, and only from the available letters."))
if race == "b" or race == "B" or race == "c" or race == "C" or race == "d" or race == "D" or race == "e" or race == "E": #A is not included in the options for this if statement because the 'white' race is not more vulnerable to Type II Diabetes, compared to other races.
    vulnerable_race = True #True and False must be written with the first letter in uppercase. The compiler won't recognize the values otherwise.
else:
    vulnerable_race = False
moderate_minutes = input("\nHow many minutes, on average, do you exercise moderately (brisk walking, water aerobics, bicycling, dancing, etc.) in a given week?\n") #str() in front of input makes sure that whatever the user types will be contained as a string. If they type a number, for example, that will be converted to a string.
while not moderate_minutes.isnumeric() or int(moderate_minutes) < 0:
    moderate_minutes = int(input("\nInvalid. Please enter a non-negative number of minutes that you exercise moderately."))
vigorous_minutes = int(input("How many minutes, on average, do you exercise vigorously (running, swimming laps, sports that require strong cardiorespiratory endurance, lifting heavy weights, etc.)?"))
while not vigorous_minutes.isnumeric() or moderate_minutes < 0:
    vigorous_minutes = int(input("\nInvalid. Please enter a non-negative number of minutes that you exercise vigorously."))
necessary_moderate_minutes = calculate_moderate_minutes(vigorous_minutes)

if moderate_minutes >= necessary_moderate_minutes: #In a later version of this program, I want the user to enter the number of minutes they exercise moderately and vigorously. The program will determine from that if their exercises is "active" enough to lower their risk of Type II Diabetes.
    active_lifestyle = True #If the user has an active lifestyle, this will decrease their chances of getting Type II Diabetes. Otherwise, it would not affect their chances.
else:
    active_lifestyle = False
fruit_content = input("\nHow often do you consume fruit in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n") #The following questions will ask the user about their healthy food choices.
while (not fruit_content.isnumeric()) or (fruit_content != "1" and fruit_content != "1" and fruit_content != "2" and fruit_content != "3" and fruit_content != "4") : #Use not. DO NOT use !.
        fruit_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n") #.isnumeric() is a method that checks if all the characters in the user's response are numbers.
vegetable_content = input("\nHow often do you consume vegetables in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
while (not vegetable_content.isnumeric()) or (vegetable_content != "1" and vegetable_content != "1" and vegetable_content != "2" and vegetable_content != "3" and vegetable_content != "4"): #Input validation that makes sure the user's input for vegetable content IS a number, and that number is between 1 and 4, inclusively.
        vegetable_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")
whole_grain_content = input("\nHow often do you consume whole grains in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
while (not whole_grain_content.isnumeric()) or (whole_grain_content != "1" and whole_grain_content != "1" and whole_grain_content != "2" and whole_grain_content != "3" and whole_grain_content != "4") : #Use not. DO NOT use ! for negating boolean variables.
       whole_grain_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")
lean_protein_content = input("\nHow often do you consume lean protein (e.g. fish, poultry, beans) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
while (not lean_protein_content.isnumeric()) or (lean_protein_content != "1" and lean_protein_content != "1" and lean_protein_content != "2" and lean_protein_content != "3" and lean_protein_content != "4"):
        lean_protein_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")
if (int(fruit_content) + int(vegetable_content) + int(whole_grain_content) + int(lean_protein_content))/4 >= 3.5: #This calculates the average amount the user's consumes healthy foods. If the average is high enough, their risk of Type II Diabetes will decrease.
    healthy_diet = True
else:
    healthy_diet = False
sugary_drinks_content = input("\nHow often do you consume sugary drinks (e.g. sweetened juices, sodas, or sports drinks) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n") #The following questions will ask the user about their unhealthy food choices.
while (not sugary_drinks_content.isnumeric()) or (sugary_drinks_content != "1" and sugary_drinks_content != "1" and sugary_drinks_content != "2" and sugary_drinks_content != "3" and sugary_drinks_content != "4"):
        sugary_drinks_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")
fried_food_content = input("\nHow often do you consume fried foods (e.g. french fries, fried chicken, or onion rings) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
while (not fried_food_content.isnumeric()) or (fried_food_content != "1" and fried_food_content != "1" and fried_food_content != "2" and fried_food_content != "3" and fried_food_content != "4"):
        fried_food_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")
processed_meat_content = input("\nHow often do you consume processed meats (e.g. bacon, sausage, or deli meat) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
while (not processed_meat_content.isnumeric()) or (processed_meat_content != "1" and processed_meat_content != "1" and processed_meat_content != "2" and processed_meat_content != "3" and processed_meat_content != "4"): #Input validation that checks that what the user entered is both a number and is 1, 2, 3, or 4, inclusive.
        processed_meat_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")

dessert_content = input("\nHow often do you consume sweets in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
while (not dessert_content.isnumeric()) or (dessert_content != "1" and dessert_content != "1" and dessert_content != "2" and dessert_content != "3" and dessert_content != "4"):
        dessert_content = input("\nInvalid. Please type 1, 2, 3, or 4.\n")

if (int(sugary_drinks_content) + int(fried_food_content) + int(processed_meat_content) + int(dessert_content))/4 >= 3.5: #This calculates the average amount the user's consumes unhealthy foods. If the average is high enough, their risk of Type II Diabetes will increase.
    unhealthy_diet = True
else:
    unhealthy_diet = False
Diagnosis = input("Have you ever been diagnosed with prediabetes, gestational diabetes, or any other type of diabetes, either now or in the past?\n") #I believe it's unlikely that the user would take this quiz if they are currently diagnosed with Type II Diabetes. That is why this question doesn't prompt they answer if they have been diagnosed for it.
while Diagnosis != "YES" and Diagnosis != "yes" and Diagnosis != "Yes" and Diagnosis != "No" and Diagnosis != "NO" and Diagnosis != "no":
    Diagnosis = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if Diagnosis == "Yes" or Diagnosis == "Yes" or Diagnosis == "yes":
    diagnosed = True
else:
    diagnosed = False
smoking_history = input("\nHave you smoked consistently before?\n") #This smoking question will likely be changed to attempt to capture more possibilities of the user's smoking history.
while smoking_history != "YES" and smoking_history != "yes" and smoking_history != "Yes" and smoking_history != "No" and smoking_history != "NO" and smoking_history != "no":
    smoking_history = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if smoking_history == "YES" or smoking_history == "yes" or smoking_history == "Yes":
    current_smoker = input("Do you currently smoke?\n")
    while current_smoker != "YES" and current_smoker != "yes" and current_smoker != "Yes" and current_smoker != "No" and current_smoker != "NO" and current_smoker != "no":
        current_smoker = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
    if current_smoker == "YES" or current_smoker == "Yes" or current_smoker == "yes":
        T2D_risk_from_smoking = 35 #T2D risk is highest if the user is currently smoking.
    else:
        T2D_risk_from_smoking = 15 #T2D risk is lower if the user is not currently smoking, but did previously. This is value was written arbitrarily, and is subject to change.
else:
    T2D_risk_from_smoking = 0 #T2D risk from smoking does not change if the user does not smoke.
sleep_condition = input("Do you struggle with disrupted or insufficient sleep?\n")
while sleep_condition != "YES" and sleep_condition != "yes" and sleep_condition != "Yes" and sleep_condition != "No" and sleep_condition != "NO" and sleep_condition != "no":
    sleep_condition = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if sleep_condition == "YES" or sleep_condition == "yes" or sleep_condition == "Yes":
        troubled_sleep = True
else:
    troubled_sleep = False
good_mental_factor = input("Do you feel happy, fulfilled, and productive?\n")
while good_mental_factor != "YES" and good_mental_factor != "yes" and good_mental_factor != "Yes" and good_mental_factor != "No" and good_mental_factor != "NO" and good_mental_factor != "no":
    good_mental_factor = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if good_mental_factor == "YES" or good_mental_factor == "yes" or good_mental_factor == "Yes":
       good_mental_health = True
else:
    good_mental_health = False
bad_mental_factor = input("Do you often struggle with depression or chronic stress?\n") #During research, these were the main mental health illnesses that contributed to Type II Diabetes.
while bad_mental_factor != "YES" and bad_mental_factor != "yes" and bad_mental_factor != "Yes" and bad_mental_factor != "No" and bad_mental_factor != "NO" and bad_mental_factor != "no":
    bad_mental_factor = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if bad_mental_factor == "YES" or bad_mental_factor == "yes" or bad_mental_factor == "Yes":
       bad_mental_health = True
else:
        bad_mental_health = False
sex = input("\nWhat is your biological sex?\nA. Male\nB.Female\n") #Sex, not gender, because there are generally two sexes, with multiple genders.
while sex != "a" and sex != "A" and sex != "b" and sex != "B": #Input validation that ensures the user types only 'A' or 'B'.
    sex = input("\nInvalid response. Please answer 'A' or 'B'.\n")
waist = int(input("What is the size of your waist? (in inches)\n"))
if waist <= 0: #Input validation that checks that the user entered a positive value for waist size.
    waist = int(input("\nInvalid response. Please enter a positive number.\n"))
if (sex == "A" and waist > 40) or (sex == "a" and waist > 40) or (sex == "B" and waist > 35) or (sex == "b" and waist > 35): #This if statement has more conditions because whether someone has a waist that is too large is dependent on their sex.
    over_sized_waist = True
else:
    over_sized_waist = False
symptoms = str(input("\nHave you struggled with at least 2 of the following symptoms in the last week?\nIncreased thirst\nUnexplained weight loss\nIncreased hunger\nFatigue\nSlow healing\nNumbness in the hands or feet\nBlurred vision\nFrequent urination\nDry skin\n")) #Adding the str() function here is more important because the user may enter a number of how many symptoms they have encountered.
while symptoms != "YES" and symptoms != "yes" and symptoms != "Yes" and symptoms != "No" and symptoms != "NO" and symptoms != "no": #As of Thursday, June 19, there are 7 instances of these 'weak' warnings where the code is duplicated. I did not try to resolve them. They don't stop the program from running. Furthermore, yes, I did copy the code to form these questions. I do not understand why these errors appear.
    symptoms = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if symptoms == "YES" or symptoms == "yes" or symptoms == "Yes":
    has_symptoms = True
else:
    has_symptoms = False
drinker = input("\nDo you routinely drink alcohol?\n") #This is the final question of the questionnaire.
while drinker != "YES" and drinker != "yes" and drinker != "Yes" and drinker != "No" and drinker != "NO" and drinker != "no":
    drinker = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
if drinker == "YES" or drinker == "yes" or drinker == "Yes":
    is_drinker = True
else:
    is_drinker = False
user_risk = calculate_risk(bmi_over_25, active_lifestyle,  healthy_diet, diagnosed, over_45, vulnerable_race, T2D_risk_from_smoking, is_drinker, troubled_sleep, good_mental_health, bad_mental_health, over_sized_waist, has_symptoms, unhealthy_diet, number_of_members) #Variable user_risk is the risk of the user of getting Type II Diabetes.
if user_risk <= 0: #Technically, it is possible for the user to receive a negative risk score. But that is a meaningless result, so if their calculation is less than 0, their actual risk will be 0.
    user_risk = 0
else:
    user_risk = user_risk #I wouldn't know what else to put for this else statement, but I believed one was necessary to cover all possibilities.
if user_risk <= 20: #This if statement prints different statements based on the value of user_risk.
    print("Your risk is low. Your risk of Type II Diabetes is " + str(user_risk)) #str() is necessary here because print() only works with strings, and user risk would be a number, not a string.
elif  20 < user_risk <= 40: #These will be ranges of values, where the increment per each risk level is about 20.
    print("Your risk is somewhat low. Your risk of Type II Diabetes is " + str(user_risk))
elif  40 < user_risk <= 60:
    print("Your risk is moderate. Your risk of Type II Diabetes is " + str(user_risk))
elif  60 < user_risk <= 80:
    print("Your risk is somewhat high. Your risk of Type II Diabetes is " + str(user_risk))
elif user_risk > 80: #This is the final elif statement, and could have been written as an else statement, since the only possible values for user_risk that wouldn't have a condition are the ones greater than 80. Therefore, there wouldn't need to be an else statement after it.
    print("Your risk is high. Your risk of Type II Diabetes is " + str(user_risk))
    #End of program.