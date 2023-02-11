
''' Movie collection system

* list of dict as the data structure where each dict holds attributes of a movie

* prompt for user input giving guide to what can be input

* depending on the user_input. we add to the storage if the attribute isn't present by asking
 the user if they like to add it or not or display the movie name due to
an attribute input

* should also ask the user if they are to view their movie shelf or
 search a movie by it's attributes then display the right message due to the user preference
 '''

movie_shelf = [
    {'name': 'Hungry hunter', 'director':'Hollar', 'year': '2020'},
    {'name': 'The Matrix','director': 'Wachowskis','year': '1994'},
    {'name': 'Merlin', 'director': 'Unknown', 'year': '2017'}
]


loop_ctrl = True
while loop_ctrl: #controls the main looping

    movie_key = ['name', 'director', 'year'] # defaulted
    values_nested_list = [list(movie.values()) for movie in movie_shelf]  # Destructure movie shelf for a cool search
    usr_pref = input('\nStrike Enter to do nothing\nWhat will you like to do? search/add/view_all: ')

    ##ADD Operation
    if usr_pref.lower() == 'add':

        #ask the user if they have more information abt the movie than it is in the movie_key
        dplay_ctrl = True
        while dplay_ctrl:
            key_str = ', '.join(movie_key)
            usr_type1 = input(f'''\nBy default you can only add movie {key_str} to your collection\nwould you like to add more movie information (y/n): ''')
            if usr_type1.lower() != 'y':
                if usr_type1 == 'n':
                    dplay_ctrl = False
                else:
                    print('\nEnter either "y" or "n"!')
            else:
                j = True
                while j:
                    mv_inf = input('''\nwhat information would you like to add?\nif no more information to add strike the enter key!: ''' )
                    if mv_inf == '':
                        j = False
                        dplay_ctrl = False
                        break

                    movie_key.append(mv_inf)
                    print('\nmovie properties updated')
#iterates over the movie key properties and allow the user to give the value of each key  taking into account any key update
        new_movie = {}
        for key in movie_key:
            slap1_ctrl = True
            while slap1_ctrl:
                usr_inp = input(f'Enter movie {key}: ')
                if key == 'year':
                    if usr_inp.isalpha() == True or usr_inp.isalnum() == False:
                        print('\nEnter a number or alphabet with number(s) as the movie year!')
                        continue

                new_movie[key] = usr_inp
                slap1_ctrl = False

        movie_shelf.append(new_movie)
        print('\nNEW MOVIE ADDED SUCCESSFULLY!')



        #SEARCH OPERATION

    elif usr_pref.lower() == 'search':
        lap2_ctrl = True
        while lap2_ctrl:
            search_input = input('''\nType any character or words attributed to the movie\nstrike the enter key if no more search: ''')

            if search_input == '':
                lap2_ctrl = False
                break

            dummy = True # Used to catch if the if block is executed or not to know if search found or not
            for value in values_nested_list:
                value_str = ''.join(value)
                value_lower = [val.lower() for val in value]  #Makes all elements in the value list, lower case for comparism with user search
                if search_input.lower() in value_lower or search_input.lower() in value_str.lower() :
                    print(f'\n{movie_shelf[values_nested_list.index(value)]}') #print movie information related to search
                    dummy = False
            if dummy:
                print("\nWe couldn't find a matched item for your search!")




            #VIEW_ALL OPERATION

    elif usr_pref.lower() == 'view_all':
        print('\n') # for spacing effect and output readability
        for movie in movie_shelf:
            print(movie)



    elif usr_pref == '':
        print('\nYou are not performing any operation.')

    else:
        print('\nEnter either "search", "add" or "View_all"')
        continue

    #exit(lap1_ctrl , loop_ctrl)
    exit_ctrl = True
    while exit_ctrl:
        usr_type = input('\nwould you like to exit?(y/n): ')
        if usr_type.lower() == 'y':
            exit_ctrl, loop_ctrl = False, False
        elif usr_type.lower() == 'n':
            exit_ctrl = False
        else:
            print('\nEnter either "y" or "n"')
            continue





















