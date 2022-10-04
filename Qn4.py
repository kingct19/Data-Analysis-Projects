speed = int(input("Enter your running speed(mph): "))

time = 5/speed
hours = int(time)
minutes = int((time - hours) * 60)
print("To run 5 miles it takes " + str(hours) + " hours and " + str(minutes) + " minutes")

time = 10/speed
hours = int(time)
minutes = int((time - hours) * 60)
print("To run 10 miles it takes " + str(hours) + " hours and " + str(minutes) + " minutes")

time = 13.1/speed
hours = int(time)
minutes = int((time - hours) * 60)
print("To run half marathon it takes " + str(hours) + " hours and " + str(minutes) + " minutes")

time = 26.2/speed
hours = int(time)
minutes = int((time - hours) * 60)
print("To run a marathon it takes " + str(hours) + " hours and " + str(minutes) + " minutes")
