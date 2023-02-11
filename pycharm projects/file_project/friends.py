# Ask the user for a list three friends
# For each friend we will tell the user whether they are nearby
# For each nearby friends we will save their name to the `nearby_friends.txt`

# hint: readlines()

check = [input('Enter a friend name: ') for _ in range(3)]
people_file = open('people.txt', 'r')
friends = [line.strip() for line in people_file.readlines()]
people_file.close()
nearby_file = open('nearby_friends.txt', 'w')
for friend in check:
    if friend.title() in friends:
        print('This friend is nearby!')
        nearby_file.write(friend)
nearby_file.close()





"""people_file = open('people.txt', 'r')
friends = people_file.readlines()
nearby_file = open('nearby_friends.txt', 'w')
for _ in range(3):
    user_input = input('Enter a friend name: ')
    if user_input.title() in friends:
        print('This friend is nearby!')
        nearby_file.write(user_input)
nearby_file.close()
people_file.close()"""