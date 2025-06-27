#Ask the user their height, weight, family history of diabetes, how many relatives have the disease, the user's age, the user's ethnicity, and other factors, and calculate their risk of Type II Diabetes.
#This version of the program was written by Yamir Richmond on Thursday, June 26, 2025.
def calculate_bmi(feet, inches, lbs): #Python will show a weak warning if the parameters are the same as the names of variables in the program.
    return round(702.9 * lbs/(((12 * feet) + inches) ** 2), 1) #The value is the user's BMI.
def calculate_moderate_minutes(minutes): #The number of minutes the user exercises VIGOROUSLY will be the parameter in this function.
    return 150 - (2 * minutes) #This value may be negative, but I didn't see that as needing correction because this is the NECESSARY number of minutes the user needs to exercise moderately. If this value is negative, that means that 0 is an upper bound for the number of minutes that the user must exercise moderately. But the user cannot exercise fewer than 0 minutes moderately.
def calculate_risk(BMI, Activity, eats_healthy, has_been_diagnosed, is_over_45, is_vulnerable_race, is_a_smoker, is_a_drinker, has_disrupted_sleep, has_good_mental_health, has_bad_mental_health, has_large_waist, struggles_with_symptoms, eats_unhealthy, user_members): #Function declaration of calculate_risk().
    t2d_risk = 0 #t2d_risk is the user's risk of Type II Diabetes, and it is initialized as 0.
    if BMI: #Most of these if statements will increase the risk of Type II Diabetes if true, and will have no change to the risk if false.
        t2d_risk += 9.6 #This value to this factor was calculated and/or specifically researched. Thus, this shouldn't be altered.
    else: #The BMI factor requires 3 questions to be asked to the user.
        t2d_risk += 0
    if Activity: #Activity and BMI are uppercase because I did not want to write different variable names for parameters that would be difficult to remember.
        t2d_risk -= 16 #This if statement will decrease the risk of Type II Diabetes if true, and will not change the risk if false.
    else: #The Activity factor requires 2 questions to be asked to the user.
        t2d_risk += 0
    if eats_healthy:
        t2d_risk -= 20 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The eats_healthy factor requires 4 questions to be asked to the user.
        t2d_risk += 0
    if has_been_diagnosed: #The idea for has_been_diagnosed is if the user has been diagnosed, their risk for having Type II Diabetes should at least be somewhat low, regardless of their other factors.
        t2d_risk += 60 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The has_been_diagnosed factor requires 1 question to be asked to the user.
        t2d_risk += 0
    if is_vulnerable_race:
        t2d_risk += 5 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The is_vulnerable_race factor requires 1 question to be asked to the user.
        t2d_risk += 0
    if is_a_drinker:
        t2d_risk += 10 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The is_a_drinker factor requires 1 question to be asked to the user.
        t2d_risk += 0 
    if has_disrupted_sleep: 
        t2d_risk += 0 #For clarity, I assume the average person does struggle with insufficient sleep. Therefore, if the user does, the risk does not increase. If the user does not, the risk decreases.
    else: #The has_disrupted_sleep factor requires 1 question to be asked to the user.
        t2d_risk -= 10 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    if has_good_mental_health:
        t2d_risk -= 5 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The has_good_mental_health factor requires 1 question to be asked to the user.
        t2d_risk += 0
    if has_bad_mental_health:
        t2d_risk += 5 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The has_bad_mental_health factor requires 1 question to be asked to the user.
        t2d_risk += 0
    if has_large_waist:
        t2d_risk += 10 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The has_large_waist factor requires 2 questions to be asked to the user.
        t2d_risk += 0
    if struggles_with_symptoms:
        t2d_risk += 15 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The struggles_with_symptoms factor requires 1 question to be asked to the user.
        t2d_risk += 0
    if eats_unhealthy: #Even if the user does not eat unhealthy, this would not imply they are consuming the nutrients necessary to lower their risk of Type II Diabetes. That is why eats_healthy and eats_unhealthy are separate variables.
        t2d_risk += 15 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    else: #The struggles_with_symptoms factor requires 4 questions to be asked to the user.
        t2d_risk += 0 #The is_a_smoker factor requires 1-2 questions to be asked to the user.
    t2d_risk += is_a_smoker #is_a_smoker is a numeric value, not a boolean.
    if is_over_45: #Age as a risk factor works differently because it increases the risk of Type II Diabetes multiplicatively.
        t2d_risk = t2d_risk * 1.1 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    if user_members == 0: #How many members a user has in their lineage that has Type II Diabetes also somewhat works differently. The more members a person has in their family that has Type II Diabetes, the greater the multiplicative factor is of their Type II Diabetes risk.
        t2d_risk += 0
    elif user_members == 1: #The user_members factor requires 1-2 questions to be asked to the user.
        t2d_risk = t2d_risk * 2 #This value to this factor was calculated and/or specifically researched. Thus, this shouldn't be altered.
    elif user_members > 1:
        t2d_risk = t2d_risk * 3 #This value for this factor was written arbitrarily, either because no consistent value exists for this factor, or none was found. Thus, it is subject to being altered.
    if t2d_risk < 0: #Technically, it is possible for the user to receive a negative risk score. But that is a meaningless result, so if their calculation is less than 0, their actual risk will be 0.
        t2d_risk = 0 
    else:
        t2d_risk = t2d_risk 
    if t2d_risk > 100:
    else:    t2d_risk = 100 #I wouldn't know what else to put for this else statement, but I believed one was necessary to cover all possibilities.
    print("Your risk is " + str(t2d_risk) + ".") #str() is necessary here because print() only works with strings, and user risk would be a number, not a string.
    if 0 <= t2d_risk <= 20: #This if statement assigns different values of category based on the value t2d_risk.
        category = "low"
    elif 20 < t2d_risk <= 40:
        category = "somewhat low"
    elif 40 < t2d_risk <= 60:
        cateogory = "moderate"
    elif 60 < t2d_risk <= 80:
        category = "somewhat high"
    elif t2d_risk > 80:
        category = "high"
        
    return category #This is the final line of the function calculate_risk().
def main(): #Having a function main is necessary because it "wraps" the code. Otherwise, the unit test will run the actual prompts in the terminal, when it should just use the values in calculate_risk() to check if the values are consistent with the given risk.
    while True: 

        user_input1 = input("Thank you for taking this questionnaire. It is designed to be accurate for assessing the risk of adult Type II Diabetes. \nThus, children aren't recommended to take it. The following two questions will ask for your height.\nWhat is your height, in whole feet?\n") #This is the first question of the program.
        try: #The program will be anywhere from 24 - 26 questions.
            user_height_ft = int(user_input1) #User BMI, Activity, healthy diet, unhealthy diet, smoking history, family history, and waist size will require more than one question.
            if user_height_ft > 1: #I'm declaring it necessary that the user must be at least 1 foot tall.
                break
            else:
                print("Invalid. Please enter a value greater than 1.\n") 
        except ValueError: 
            print("Invalid.\n")
    while True:

        user_input2 = input("\nWhat is your height in inches leftover?\n") #The user_input variables do NOT represent the factors, but the numeric variables the user must enter a value for.
        try:
            user_height_in = int(user_input2)
            if 0 <= user_height_in < 12: #A value of 12 or greater is invalid because the user is entering in inches leftover.
                break
            else:
                print("Invalid. Please enter a value between 0 and 11, inclusive.\n")
        except ValueError:
            print("Invalid. Please make sure your response contains only numbers.\n") 
    while True:

        user_input3 = input("\nWhat is your weight? (lbs)\n") 
        try:
            user_weight = float(user_input3) #User input can be a float because weight isn't a discrete variable.
            if user_weight > 0: 
                break
            else:
                print("Invalid. Please enter a positive number.\n")
        except ValueError:
            print("\nInvalid. Please make sure your response only contains only numbers.\n")

    user_bmi = calculate_bmi(user_height_ft, user_height_in, user_weight) #The goal is to make the function that calculates the risk for Type II Diabetes as simple as possible. Thus, these other calculations must be made in these other functions.
    if user_bmi >= 25: #These if statements will determine the value of boolean variables. The boolean variables will be passed to the calculate_risk() function.
        bmi_over_25 = True #BMI is the first factor of the questionnaire that will be considered.
    else: #This else statement, indicating the boolean variable is False otherwise, is a necessity. If not included, the boolean variable might not be initialized when it's passed into the function.
        bmi_over_25 = False
    print("Your BMI is " + str(user_bmi) + ".") #To tell the user what their BMI is.
    family_history = input("\nDoes anyone in your blood family have Type II Diabetes?\n") 
    while family_history != "YES" and family_history != "yes" and family_history != "Yes" and family_history != "No" and family_history != "NO" and family_history != "no": #Input validation to limit the user's responses to either "Yes" or "No".
        family_history = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
    if family_history == "YES" or family_history == "yes" or family_history == "Yes": 
        while True: #This program should have a 'while True: try/except' block for every instance that a user is supposed to enter a number.

            user_input4 = input("\nHow many members in your family have diabetes?\n")  #The user_input occurrences indicate when the user MUST type a number value in order to proceed.
            try:
                number_of_members = int(user_input4) #This is the variable that will be passed to calculate_risk().
                if number_of_members >= 1:
                    break
                else: 
                    print("Invalid. Please enter a positive value.\n") #The value must be positive. The user already declared that they have a history of Type II Diabetes, so at least one person in their family must have Type II Diabetes.
            except ValueError:
                print("Invalid.\n")
    else:
        number_of_members = 0 #This is important. The user may not have any members in their family at all that have Type II Diabetes, so if they answer "No" to "Does your family have a history of Type II Diabetes", the variable number_of_members will be 0. That variable will be passed to calculate_risk().
    while True: #It is impossible to break out of this loop if the user enters an invalid response. The user will only proceed if they enter a value the function can accept. Thus, the function calculate_risk() will not have null values for any of its arguments.

        user_input5 = input("\nHow old are you? (yrs)\n") #The user will input their age, in years. 
        try:
            user_age = int(user_input5)
            if user_age >= 18: 
                break
            else:
                print("Invalid. This questionnaire is not designed for people under 18.\n") #The questionnaire does not provide accurate results for predicting diabetes for children.
        except ValueError: #The try/except blocks prevent the program from terminating, even if the user types an invalid argument.
            print("Invalid. Please enter a number.\n")
    if user_age >= 45: #Many of these variables will be boolean, so the risk of Type II Diabetes will increase.
        over_45 = True #This variable is a boolean.
    else:
        over_45 = False
    race = input("What is your race? (Please type the LETTER, not the whole race.)\nA. White\nB. African American\nC. Asian American\nD. Hispanic/Latino\nE. Pacific Islander\nF. Other\n")
    while race != "A" and race != "a" and race != "B" and race != "b" and race != "C" and race != "c" and race != "D" and race != "d" and race != "E" and race != "e" and race != "F" and race != "f": #Input validation to limit the user's responses to either 'A', 'B', 'C', 'D', 'E', or 'F'.
        race = str(input("\nPlease select from one of the available letters, and only from the available letters."))
    if race == "b" or race == "B" or race == "c" or race == "C" or race == "d" or race == "D" or race == "e" or race == "E": #A is not included in the options for this if statement because the 'white' race is not more vulnerable to Type II Diabetes, compared to other races.
        vulnerable_race = True #True and False must be written with the first letter in uppercase. The compiler won't recognize the values otherwise.
    else: #An if-else statement inside of a while loop, and a try/except block inside of a while loop are the main ways I perform input validation in this program.
        vulnerable_race = False 
    while True: #This is a while loop that is true indefinitely. The only way to get out of this loop is to satisfy a  condition to break the loop.
        user_input6 = input("\nHow many minutes per week, on average, do you exercise moderately (brisk walking, water aerobics, bicycling, dancing, etc.\n") #I do not use int() on the input variable in this code because the user could enter something that is not an integer.
        try:
            moderate_minutes = int(user_input6) 
            if moderate_minutes >= 0: #So, in this case, for example, the logic is that if the user enters a non-negative value for their number of moderate exercise, 
                break
            else:
                print("\nInvalid. Please type a non-negative integer.") #This occurs if the user_input variable is a number, but is negative, thus being invalid as a total number of minutes exercised moderately.
        except ValueError: #This occurs if it is impossible to convert the user_input variable into an integer.
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input7 = input("\nHow many minutes per week, on average, do you exercise vigorously (running, swimming laps, sports that require strong cardiorespiratory endurance, lifting heavy weights, etc.)?\n") #CDC guidelines are that one should exercise at least 75 minutes vigorously, or at least 150 minutes moderately. I derived an equation from this to determine the necessary amount of moderate minutes for the user.
        try:
            vigorous_minutes = int(user_input7)
            if vigorous_minutes >= 0:
                break
            else:
                print("\nInvalid. Please type a non-negative integer.") #Non-negative because the user can enter 0 as a valid response.
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    necessary_moderate_minutes = calculate_moderate_minutes(vigorous_minutes) #Given a certain number of minutes the user exercises vigorously, the user has a certain number of minutes they must exercise moderately 

    if moderate_minutes >= necessary_moderate_minutes: 
        active_lifestyle = True #If the user has an active lifestyle, this will decrease their chances of getting Type II Diabetes. Otherwise, it would not affect their chances.
    else: 
        active_lifestyle = False 
    while True: 
        user_input8 = input("\nHow often do you consume fruit in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            fruit_content = int(user_input8)
            if 1 <= fruit_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.") #These should also be integers, 
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input9 = input("\nHow often do you consume vegetables in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            vegetable_content = int(user_input9)
            if 1 <= vegetable_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input10 = input("\nHow often do you consume whole grains in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            whole_grain_content = int(user_input10)
            if 1 <= whole_grain_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input11 = input("\nHow often do you consume lean protein (e.g. fish, poultry, beans) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            lean_protein_content = int(user_input11)
            if 1 <= lean_protein_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")#The value calculated from the division need not be an integer. It just needs to be higher than 3.5.
    if (int(fruit_content) + int(vegetable_content) + int(whole_grain_content) + int(lean_protein_content))/4 >= 3.5: #This calculates the average amount the user's consumes healthy foods. If the average is high enough, their risk of Type II Diabetes will decrease.
        healthy_diet = True
    else:
        healthy_diet = False
    while True:
        user_input12 = input("\nHow often do you consume sugary drinks (e.g. sweetened juices, sodas, or sports drinks) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            sugary_drinks_content = int(user_input12)
            if 1 <= sugary_drinks_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input13 = input("\nHow often do you consume fried foods (e.g. french fries, fried chicken, or onion rings) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            fried_food_content = int(user_input13)
            if 1 <= fried_food_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input14 = input("\nHow often do you consume processed meats (e.g. bacon, sausage, or deli meat) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            processed_meat_content = int(user_input14)
            if 1 <= fried_food_content <= 4:
                break
            else:
                print("\nInvalid. Please type a number between 1 and 4.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    while True:
        user_input15 = input("\nHow often do you consume sweets (e.g. cookies, candy, cakes) in your diet? Please type 1, 2, 3, or 4.\n1. Never\n2. Rarely \n3. Sometimes \n4. Often\n")
        try:
            dessert_content = int(user_input15)
            if 1 <= dessert_content <= 4:
                break
            else:
                print("\nInvalid. Please enter a number.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    if (int(sugary_drinks_content) + int(fried_food_content) + int(processed_meat_content) + int(dessert_content))/4 >= 3.5: #This calculates the average amount the user's consumes unhealthy foods. If the average is high enough, their risk of Type II Diabetes will increase.
        unhealthy_diet = True
    else:
        unhealthy_diet = False
    Diagnosis = input("\nHave you ever been diagnosed with prediabetes, gestational diabetes, or any other type of diabetes, either now or in the past?\n") #I believe it's unlikely that the user would take this quiz if they are currently diagnosed with Type II Diabetes. That is why this question doesn't prompt they answer if they have been diagnosed for it.
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
        current_smoker = input("\nDo you currently smoke?\n")
        while current_smoker != "YES" and current_smoker != "yes" and current_smoker != "Yes" and current_smoker != "No" and current_smoker != "NO" and current_smoker != "no":
            current_smoker = input("\nInvalid response. Please answer 'yes' or 'no'.\n") #Overlooking this code, I would like every string requiring input to have '\n' on either side.
        if current_smoker == "YES" or current_smoker == "Yes" or current_smoker == "yes":
            T2D_risk_from_smoking = 35 #T2D risk is highest if the user is currently smoking.
        else:
            T2D_risk_from_smoking = 15 #T2D risk is lower if the user is not currently smoking, but did previously. This is value was written arbitrarily, and is subject to change.
    else: #This else statement aligns with the if-statement that determines whether the user selected "Yes" to the question. Because the user entered an acceptable response, their answer was one of the many variants of "Yes" and "No".
        T2D_risk_from_smoking = 0 #T2D risk from smoking does not change if the user does not smoke.
    sleep_condition = input("\nDo you struggle with disrupted or insufficient sleep?\n")
    while sleep_condition != "YES" and sleep_condition != "yes" and sleep_condition != "Yes" and sleep_condition != "No" and sleep_condition != "NO" and sleep_condition != "no": #A try/except code block isn't necessary here because there is no reason to convert what the user types into a numeric variable. 
        sleep_condition = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
    if sleep_condition == "YES" or sleep_condition == "yes" or sleep_condition == "Yes":
            troubled_sleep = True
    else:
        troubled_sleep = False
    good_mental_factor = input("\nDo you feel happy, fulfilled, and productive?\n")
    while good_mental_factor != "YES" and good_mental_factor != "yes" and good_mental_factor != "Yes" and good_mental_factor != "No" and good_mental_factor != "NO" and good_mental_factor != "no":
        good_mental_factor = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
    if good_mental_factor == "YES" or good_mental_factor == "yes" or good_mental_factor == "Yes":
        good_mental_health = True
    else:
        good_mental_health = False #Not having good mental health doesn't necessarily 
    bad_mental_factor = input("Do you often struggle with depression or chronic stress?\n") #During research, these were the main mental health illnesses that contributed to Type II Diabetes.
    while bad_mental_factor != "YES" and bad_mental_factor != "yes" and bad_mental_factor != "Yes" and bad_mental_factor != "No" and bad_mental_factor != "NO" and bad_mental_factor != "no":
        bad_mental_factor = input("\nInvalid response. Please answer 'yes' or 'no'.\n")
    if bad_mental_factor == "YES" or bad_mental_factor == "yes" or bad_mental_factor == "Yes":
        bad_mental_health = True
    else:
        bad_mental_health = False
    sex = input("\nWhat is your biological sex? Please type the letter.\nM. Male\nF.Female\n") #Sex, not gender, because there are generally two sexes, with multiple genders.
    while sex != "m" and sex != "M" and sex != "f" and sex != "F": #Input validation that ensures the user types only 'M' or 'F'.
        sex = input("\nInvalid response. Please answer 'M' or 'F'.\n") 
    while True:
        user_input16 = input("\nWhat is the size of your waist? (in inches)\n")
        try:
            waist = float(user_input16)
            if waist > 0:
                break
            else:
                print("\nInvalid. Please enter a positive number.\n")
        except ValueError:
            print("\nInvalid. Please enter a number.\n")
    if (sex == "A" and waist > 40) or (sex == "a" and waist > 40) or (sex == "B" and waist > 35) or (sex == "b" and waist > 35): #This if statement has more conditions because whether someone has a waist that is too large is dependent on their sex.
        over_sized_waist = True #The actual sex of the person, along with the size of their waist, are not passed to the function calculate_risk(). What is passed to the function is the boolean over_sized_waist.
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
    if drinker == "YES" or drinker == "yes" or drinker == "Yes": #Being a drinker is the final factor with being considered in the risk of Type II Diabetes.
        is_drinker = True
    else:
        is_drinker = False #The only other possible values the user could have entered were 'no', 'NO', or 'No', so it would be logical to presume they are not a drinker. Thus, is_drinker is false.
    user_category = calculate_risk(bmi_over_25, active_lifestyle,  healthy_diet, diagnosed, over_45, vulnerable_race, T2D_risk_from_smoking, is_drinker, troubled_sleep, good_mental_health, bad_mental_health, over_sized_waist, has_symptoms, unhealthy_diet, number_of_members) #Variable user_risk is the risk of the user of getting Type II Diabetes.
    print("Your category of risk is " + category + ".")
if __name__ == '__main__': #These lines are necessary for the test_T2D_Risk_Ver_6_25_25.py file.
    main() 
        #End of program.
