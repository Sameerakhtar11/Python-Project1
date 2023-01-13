def findAge(current_date,current_month,current_year,date_of_birth,month_of_birth,year_of_birth):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (date_of_birth>current_date):
        current_month=current_month-1
        current_date=current_date+month[month_of_birth-1]
    if (month_of_birth>current_month):
        current_year=current_year-1
        current_month=current_month+12
    calculate_date=current_date-date_of_birth
    calculate_month=current_month-month_of_birth
    calculate_year=current_year-year_of_birth
    i=0
    if (calculate_year % 400 ==0) or (calculate_year % 100 ==0) and (calculate_year % 4 == 0):
        i+=1
    else:
        i+=0
    days=366*i+((calculate_year)-i)*365+(calculate_month)*30+calculate_date
    print("Dear user your present age is: ")
    print("Years: ",calculate_year,"Months: ",calculate_month,"Days: ",calculate_date)
    print("Number of days you survived is approx: ",days)
    print("Thank you for using my program")
current_date=int(input("Enter the current date: "))
current_month=int(input("Enter the current month: "))
current_year=int(input("Enter the current year: "))
date_of_birth=int(input("Enter the date of birth: "))
month_of_birth=int(input("Enter the month of birth: "))
year_of_birth=int(input("Enter the year of birth: "))
findAge(current_date,current_month,current_year,date_of_birth,month_of_birth,year_of_birth)