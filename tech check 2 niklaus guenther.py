#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: niklaus guenther 
Program Title: tech check 2 
Description: Tax Withheld Calculator   
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #weekly salary and dependents
    weeklySalary = float(input("Please enter the full amount of your weekly salary:"))
    dependents = int(input("How many dependents do you have?:"))

    #tax for provincial, federal and the dependant deductions
    ProvWithheld = weeklySalary * 0.06
    FedWithheld =  weeklySalary * 0.25
    dependentDeduc = dependents * 20

    #Calculates total withheld and your total takehome
    TotalWithheld= float(ProvWithheld + FedWithheld - dependentDeduc)
    TotalTakehome = float(weeklySalary - TotalWithheld)

    #output
    print(f"Provincial Tax Withheld: ${ProvWithheld:.2f}")
    print(f"Federal Tax Withheld: ${FedWithheld:.2f}")
    print(f"Total Dependents Deduction: ${dependentDeduc:.2f}")
    print(f"Total Amount Withheld: ${TotalWithheld:.2f}")
    print(f"Total Take-Home Pay: ${TotalTakehome:.2f}")
    #Your code ends on the line above

#Do not change any of the code below!
main()