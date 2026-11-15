year = int(input("Give me a year and ill check if its a leap year: "))
if year % 4 == 0 and year > 2025:
    year = str(year)
    print("YEAR " + year + " WILL BE A LEAP YEAR")
elif year % 4 == 0 and year < 2025:
    year = str(year)
    print("YEAR " + year + " WAS A LEAP YEAR")
elif year % 4 != 0 and year < 2025:
    year = str(year)
    print("YEAR " + year + " WAS NOT A LEAP YEAR")
elif year % 4 != 0 and year > 2025:
    year = str(year)
    print("YEAR " + year + " WILL NOT BE A LEAP YEAR")
