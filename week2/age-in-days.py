def isLeapYear(year):
	multiple_of_4 = year % 4 == 0
	divisible_by_100 = year % 100 == 0
	multiple_of_400 = year % 400 == 0

	return multiple_of_4 and not (divisible_by_100 and not multiple_of_400)

def daysInMonth(year, month):
	if month in (1, 3, 5, 7, 8, 10, 12):
		return 31
	else: 
		if month == 2:
			if isLeapYear(year):
				return 29
			else:
				return 28
		else:
			return 30
	return 30

def nextDay(year, month, day):
	if day < daysInMonth(year, month):
		return year, month, day + 1
	else:
		if month < 12:
			return year, month + 1, 1
		else:
			return year + 1, 1, 1

	return (year, month, day)

def dateIsBefore(year, month, day, current_year, current_month, current_day):
	if year < current_year:
		return True
	if year == current_year:
		if month < current_month:
			return True
		if month == current_month: 
			return day < current_day

	return False

def daysBetweenDates(year, month, day, current_year, current_month, current_day):
	assert dateIsBefore(year, month, day, current_year, current_month, current_day)

	sumDays = 0

	while dateIsBefore(year, month, day, current_year, current_month, current_day):
		year, month, day = nextDay(year, month, day)
		sumDays = sumDays + 1

	return sumDays		
		
	
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "expected: ", answer, " got: ", result)
        else:
            print ("Test case passed!")

test()

