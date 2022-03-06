print("Print leap year between two given years")
print("Enter start year")
startYear = int(input())
print("Enter final year")
finalYear = int(input())
print("The leap years are:")
for year in range(startYear, finalYear):
  if(year%4==0) and (year%100!=0) or (year%400==0):
   print(year)
