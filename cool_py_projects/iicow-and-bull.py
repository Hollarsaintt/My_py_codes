import random 

play_again = True
while play_again:
        rand_num = random.randint(1000, 9999)
	lp_ctrl = True
	print('Welcome to Cow and Bull!\nEnjoy!') 
	num_of_guess = 0 

	while lp_ctrl: 
		try:
			gues_num = int(input('Guess a 4-digit number: '))
			print(rand_num)
			
			if len(str(gues_num)) != 4:
				if len(str(gues_num)) < 4: print('Guessed number has {l} digits (less than 4 digits)'.format(l= len(str(gues_num))))

				else: print('Guessed number has {l} digits (more than 4 digits)'.format(l= len(str(gues_num))))

				print('Please make your guess again!\n\n') 
				continue 
			else:
				num_of_guess += 1

				if gues_num == rand_num: 
					print('You have 4 cows!. \nCongratulations! \nYou won!\n')
					ds = True 
					print('You made {g} number of guesses in the game.'.format(g= num_of_guess))

					while ds: 
						dec = input('\nDo you want to play again? (y/n): ')
 
						if ((dec == 'n') or (dec == 'N')): 
							print('Ending game. . .\nGame ended')
							play_again = False
							lp_ctrl = False 
							break 
			
						elif not ((dec == 'Y') or (dec == 'y')):
							print('\nPlease enter the right option.\n')
		
						else:
							lp_ctrl = False 	 
							break  

				else:
					cow = 0
					gues_digit = list(str(gues_num))
					rand_digit = list(str(rand_num))
					rem = [] 
					for x in range(4): 
						if int(gues_digit[x]) == int(rand_digit[x]): 
							cow += 1
		
						else: rem.append(x)

					rand = []
					gues = []
					for x in rem: 
						rand.append(int(rand_digit[x]))
						gues.append(int(gues_digit[x]))
					
					bull = 0					
					for x in gues:
						if x in rand: 
							bull += 1
							index = rand.index(x)
							rand.pop(index) 
							
  	
					print('You have {c} cow(s);'.format(c= cow), end= ' ')
					print('You have {b} bull(s);'.format(b= bull))
				
		except ValueError: print('The number has alphabet. \nPlease make your guess again.') 
	

