year = int(input("Enter a year: "))
for year in range(2000, 2201):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year")
  else:
        print(year, "is not a Leap Year")