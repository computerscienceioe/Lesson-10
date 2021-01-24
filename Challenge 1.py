# print(round(4/3, 2)) # 1.33

# print(min([1,2,3])) # 1

# print(max([1,2,3])) # 3

# print(sorted([4,2,6],reverse=True)) # [6,4,2]

# print(sum([1.1,2,3])) # 6

# word = "Dara"
# print(word.count("a"))

# print(pow(3,2)) # 9

# print(abs(-4)) # 4


# age = int(input("Please enter your age: "))
# if age >= 17:
#   print("You are eligible to apply for an Irish driving licence")
# else:
#   print("You are not eligible to apply for an Irish driving licence")

def drivingLicenceEligibility(age):
  if age >= 17:
    return "You are eligible to apply for an Irish driving licence"
  else:
    return "You are not eligible to apply for an Irish driving licence"


# age = int(input("Please enter your age: "))
# print(drivingLicenceEligibility(age))



def testDrivingLicenceEligibility():
  print("Testing driving licence function")
  testAge = 25
  testAnswer = "You are eligible to apply for an Irish driving licence"

  if drivingLicenceEligibility(testAge) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")
  
  testAge = 15
  testAnswer = "You are not eligible to apply for an Irish driving licence"

  if drivingLicenceEligibility(testAge) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

testDrivingLicenceEligibility()


# year = int(input("Enter a year?"))

def isLeapYear(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

def testIsLeapYear():
  print("Testing is leap year function")
  testYear = 2020
  testAnswer = True

  if isLeapYear(testYear) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testYear = 2019
  testAnswer = False

  if isLeapYear(testYear) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testYear = 2000
  testAnswer = True

  if isLeapYear(testYear) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testYear = 1900
  testAnswer = False

  if isLeapYear(testYear) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

testIsLeapYear()

def gradeCalculator(mark):
  if mark <= 100 and mark >= 90:
    return "H1"
  if mark < 90 and mark >= 80:
    return "H2"
  if mark < 80 and mark >= 70:  
    return "H3"
  if mark < 70 and mark >= 60:
    return "H4"
  if mark < 60 and mark >= 50:
    return "H5"
  if mark < 50 and mark >= 40:
    return "H6"
  if mark < 40 and mark >= 30:
    return "H7"
  if mark < 30 and mark >= 0:
    return "H8"
  return "Error, invalid mark"

def isWeekDay(day):
  if day.lower() == "saturday" or day.lower() == "sunday":
    return False
  else:
    return True
