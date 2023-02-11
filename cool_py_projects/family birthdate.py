birthdays = {'opeyemi': 'march 23', 'blessing': 'feb 25', 'favour':'july 27', 'nifemi':'july 20'}
while True:
    print('Enter a name: (blank is quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + " is " + name + "'s" + ' birthday')
    else:
        print('Name not found in database')
        print('Enter the date to update my database')
        bday = input()
        birthdays[name] = bday
        print('database updated successfully')
