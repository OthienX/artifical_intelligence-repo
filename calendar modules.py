import calendar
sep = calendar.TextCalendar(calendar.SUNDAY)
sep.prmonth(2019,9)
nov = calendar.TextCalendar(calendar.TUESDAY)
nov.prmonth(2022, 11)
aug =calendar.TextCalendar(calendar.FRIDAY)
aug. prmonth(2022, 8)
leaps =calendar. leapdays(2000, 2019)
print("these are leaps years", leaps)
#fashioning of the first example
year1 =input("enter the first year ")
year2 =input("enter the second year")
leaps=calendar.leapdays("year1", "year2")
print("number of leap years between", year1,"and", year2 ,"is", leaps)