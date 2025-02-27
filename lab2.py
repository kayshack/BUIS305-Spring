Grade1=int(input('Enter Grade Between (0-100)'))
Grade2=int(input('Enter Grade Between (0-100)'))
Grade3=int(input('Enter Grade Between (0-100)'))
average = (Grade1 + Grade2 + Grade3)/3
if average > 80:
    print('Grade:A')
if average > 70:
    print('Grade B')
if average < 69:
    print('Grade F')