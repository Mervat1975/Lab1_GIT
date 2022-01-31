

# Name:Mervat Mustafa
# created Date: Jan 30,2022
# Description of the program:calculate annual salary of five employees in a small hypothetical company


from datetime import date
# Global Constants
COMPANY_NAME = "DigiTech"
NAME_INDEX = 0
POSITION_INDEX = 1
SALARRY_INDEX = 2
BONUS_FIRST_START_RANGE = 25000
BONUS_SECOND_START_RANGE = 50000
BONUS_THIRD_START_RANGE = 55000
BONUS_FIRST_PERCENTAGE = 10.5/100
BONUS_SECOND_PERCENTAGE = 11.5/100
BONUS_THIRD_PERCENTAGE = 12.5/100
TAXES_PERCENTAGE = 15.5/100
BENEFITES_PERCENTAGE = 6.5/100

# function name: print_paystub
# function description: Receives a list contains data of 5 employees and print out the pay stub for each  employee
# parameters : employees:list
# return value: no return value


def print_paystub(employees):
    emp_index = 0
    while emp_index < len(employees):
        # calcualate bonus
        salary = employees[emp_index][SALARRY_INDEX]
        bonus = 0
        # less or equal to $25,000, the company has allocated 10.5% bonus
        if (salary <= BONUS_FIRST_START_RANGE):
            bonus = salary*BONUS_FIRST_PERCENTAGE
        elif (salary <= BONUS_SECOND_START_RANGE):  # 11.5% bonus between $25,000 and $50,000
            bonus = salary*BONUS_SECOND_PERCENTAGE
        elif (salary >= BONUS_THIRD_START_RANGE):  # 12.5% bonus if more than $55,000
            bonus = salary*BONUS_THIRD_PERCENTAGE
        # calcualate gross annual income
        gross_annual_income = salary+bonus

        # calclate taxes (15.5%)
        deductible_taxes = gross_annual_income * TAXES_PERCENTAGE
        # calculate benefits (6.5%)
        deductible_benefits = gross_annual_income * BENEFITES_PERCENTAGE
        # calculate total deductibles
        deductibles = deductible_taxes + deductible_benefits
        # calaclate Net Annual Income
        net_annual_income = gross_annual_income-deductibles

        # print pay stab

        print('Company name: ', COMPANY_NAME)
        today = str(date.today())
        print('Date of Pay-Stub: ', today)
        print(f'Employee: \"{ employees[emp_index][NAME_INDEX].strip()}\"')
        print(f'Position: \"{ employees[emp_index][POSITION_INDEX].strip()}\"')
        print('Salary: ',  "${:,.2f}".format(salary))
        print('Bonus: ', "${:,.2f}".format(bonus))
        print('Gross Annual Income:', "${:,.2f}".format(gross_annual_income))
        print('Deductibles:', "${:,.2f}".format(deductibles))
        print('Deductible (Taxes):', "${:,.2f}".format(deductible_taxes))
        print('Deductible (Benefits):', "${:,.2f}".format(deductible_benefits))
        print('Net Annual Income: ', "${:,.2f}".format(net_annual_income))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        emp_index = emp_index+1


# declaring a 2D list to store the data of the 5 employees
employees = [['Mervat', 'Web devloper', 50000], ['Omer', 'Programmer', 25000], [
    'Johan', 'Data Scientist', 70000], ['Ali', 'Accountant', 53000], ['Stephen', 'CEO', 100000]]
# call function to print pay stub of 5 employees
print('+++++++++++++++++++ PAY STAB +++++++++++++++++++++')
print_paystub(employees)
