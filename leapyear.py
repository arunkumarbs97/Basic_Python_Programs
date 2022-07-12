Year = int(input("Enter a year:"))
if Year % 4==0 and Year % 100 !=0:
    print(Year, "is not a leap year")
elif Year % 100 == 0:
    print(Year, "is not a leap year")
elif Year % 400 == 0:
    print(Year, "is a leap Year")
else:
    print(Year, "is not a Leap year")