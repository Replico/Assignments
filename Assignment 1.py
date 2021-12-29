#PART A: House Hunting

def part_a():
    #User Inputs
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))

    #Salary Metrics
    portion_down_payment = .25
    current_savings = 0
    monthly_salary = annual_salary/12
    monthly_payment = monthly_salary * portion_saved
    r = .04
    months = 0

    while (total_cost * portion_down_payment) > current_savings:
        current_savings += monthly_payment + (current_savings * r / 12)
        months += 1

    print("Number of months: ", months)

#PART B Saving, with a raise
def part_b():
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    #Salary Metrics
    portion_down_payment = .25
    current_savings = 0
    monthly_salary = annual_salary/12
    monthly_payment = monthly_salary * portion_saved
    r = .04
    months = 0

    while (total_cost * portion_down_payment) > current_savings:
        if (months % 6 == 0 and months != 0):
            monthly_payment *= (1 + semi_annual_raise)
        current_savings += monthly_payment + (current_savings * r / 12)
        months += 1
    print("Number of months: ", months)

#PART C Finding the right amount to save away
def part_c():
    cost = 250000
    semi_annual_raise = .07
    r = .04

    annual_salary = float(input("Enter your starting salary: "))
    epsilon = 100
    low = 0 
    steps = 0
    high = 10000
    too_low = 0

    possible_to_pay = True

    while True:
        guess = (low + high) / 2
        monthly_payment = (annual_salary / 12) * (guess / 10000)

        current_savings = 0
        months = 0

        while months < 36:
            if (months % 6 == 0 and months != 0):
                monthly_payment *= (1 + semi_annual_raise)
            current_savings += monthly_payment + (current_savings * r / 12)
            if current_savings > cost:
                break
            months += 1

        if abs(current_savings - cost) < 100:
            print("Best savings rate is:", round(guess / 10000, 4))
            print("Number of steps:", steps)
            break

        elif current_savings > cost:
            high = guess
            steps += 1

        else:
            if (too_low > 15):
                print("not possible")
                break
            low = guess
            steps += 1
            too_low += 1


#part_a()
#part_b()
#part_c()
