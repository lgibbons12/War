import pygame
import os
import random



pygame.init()

#create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("War")


#load images
bg_img = pygame.image.load("C:/Users/liamw/Documents/CardGame/bg.jpg").convert_alpha()
bg_img = pygame.transform.scale(bg_img, (750, 550))

bg2_img = pygame.image.load("C:/Users/liamw/Documents/CardGame/bg2.jpg").convert_alpha()
bg2_img = pygame.transform.scale(bg2_img, (800, 600))

back_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/back.png').convert_alpha()
war_img = pygame.transform.scale(back_img, (60, 50))

next_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/button.png').convert_alpha()
next_img = pygame.transform.scale(next_img, (150, 150))

war_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/war.png').convert_alpha()
war_img = pygame.transform.scale(war_img, (200, 100))

start_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/start.png').convert_alpha()
start_img = pygame.transform.scale(start_img, (200, 100))

exit_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/exit.png').convert_alpha()
exit_img = pygame.transform.scale(exit_img, (200, 100))

reset_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/rest.png').convert_alpha()
reset_img = pygame.transform.scale(reset_img, (200, 100))

backarrow_img = pygame.image.load('C:/Users/liamw/Documents/CardGame/back_arrow.png').convert_alpha()
backarrow_img = pygame.transform.scale(backarrow_img, (50, 50))
#used to make lists more intuitive
spade3_img = 0

#define colors
BG = (255, 255, 255)
BLACK = (0, 0, 0)

#frame rate
clock = pygame.time.Clock()
fps = 60

#define font
font = pygame.font.SysFont('Bauhaus 93', 30)
bigfont = pygame.font.SysFont('Bauhaus 93', 90)

#make lists and add one thing to each to make ranged fuctions easier
clubs = []
clubs.append(spade3_img)
hearts = []
hearts.append(spade3_img)
spades = []
spades.append(spade3_img)
diamonds = []
diamonds.append(spade3_img)

#counters for open animation
animation_cooldown_1 = 1
animation_cooldown_2 = 1
animation_cooldown_3 = 1


#make hands
player_hand = []
enemy_hand = []

#scores for point keeping and displaying
player_score = 26
enemy_score = 26

#turn keepers
turn_num = 1
temp_turn_num = 1
clicked = 0
game_state = 0
temp_game_started = False
game_started = False

#for hand distribution
fill_counter = 0

#war variables
war_counter = 1
war_clicked = 0
war_done = False
war_temp_num = 0
one_in_a_million = False
war_turn_num = 0

#for multiple playthroughs
player_wins = 0
enemy_wins = 0
multi_games = False


def draw_bg():
    screen.fill(BG)
    screen.blit(bg_img, (25, 25))


#load in card images and add them to hands
def load_cards():
	for i in range(1, 5):
		if i == 1:
			for i in range(1, 14):
				club_img = pygame.image.load(f"C:/Users/liamw/Documents/CardGame/Clubs/card{i + 1}.png")
				card = Cards(i, 2, club_img, 0, 0)
				card.add_hand()
		elif i == 2:
			for i in range(1, 14):
				heart_img = pygame.image.load(f"C:/Users/liamw/Documents/CardGame/Hearts/{i + 1}.png")
				card = Cards(i, 2, heart_img, 0, 0)
				card.add_hand()
		elif i == 3:
			for i in range(1, 14):
				spade_img = pygame.image.load(f"C:/Users/liamw/Documents/CardGame/Spades/{i + 1}.png")
				card = Cards(i, 2, spade_img, 0, 0)
				card.add_hand()
		elif i == 4:
			for i in range(1, 14):
				diamond_img = pygame.image.load(f"C:/Users/liamw/Documents/CardGame/Diamonds/{i + 1}.png")
				card = Cards(i, 2, diamond_img, 0, 0)
				card.add_hand()
	

class Cards(pygame.sprite.Sprite):
	def __init__(self, rank, hand_location, image, x, y):
		self.rank = rank
		self.image = image
		self.location = hand_location
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.fill_counter = fill_counter

	#add cards to player and enemy hands randomly
	def add_hand(self):

		#makes hands even
		if len(player_hand) == 26:
			enemy_hand.append(self)

		elif len(enemy_hand) == 26:
			player_hand.append(self)

		else:
			#randomly sort cards into one hand or another
			self.location = random.randint(0, 1)
			if self.location == 1:
				player_hand.append(self)
			if self.location == 0:
				enemy_hand.append(self)

		
		#shuffle the hands
		random.shuffle(player_hand)
		random.shuffle(enemy_hand)

                                
                  
	def draw(self, x, y):
		self.x = x
		self.y = y
		screen.blit(self.image, (self.x, self.y))





def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
	

class Button():
        def __init__(self, x, y, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.clicked = False
        def draw(self):
                action = False
                #get mouse position
                pos = pygame.mouse.get_pos()

                #check mouseover and click conditions
                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] and self.clicked == False:
                                self.clicked = True
                                action = True             

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                
                                
                  
                screen.blit(self.image, self.rect)

                return action



def draw_cards(war_temp_num, war_turn_num, turn_num, game_state, clicked, war_counter, war_done):


	
	#show two backs
	screen.blit(back_img, (325, 350))
	screen.blit(back_img, (325, 50))


	if clicked > 0:

		#draw cards on once clicked
		player_hand[turn_num].draw(325, 350)
		enemy_hand[turn_num].draw(325, 50)
		if game_state == 1:
			if player_hand[turn_num].rank > enemy_hand[turn_num].rank:
				draw_text("Player Wins", font, BLACK, 325, 275)

			elif enemy_hand[turn_num].rank > player_hand[turn_num].rank:
				draw_text('Enemy Wins', font, BLACK, 325, 275)

		if game_state == 2 and war_done == False:
			for i in range(3):
				screen.blit(back_img, (510 + (i * 30), 300))
				screen.blit(back_img, (510 + (i * 30), 100))


	#war
	#used to display the next card in the war

	if game_state == 2:
		if war_clicked != 1:
			draw_text("War!", bigfont, BLACK, 300, 250)
		
		
		if war_temp_num > 0:
			for i in range(4):
				player_hand[turn_num + 1 + (3-i)].draw(360 - (i * 20), 350)
				enemy_hand[turn_num + 1 + (3-i)].draw(360 - (i * 20), 50)

			
		else:
			player_hand[turn_num].draw(325, 350)
			enemy_hand[turn_num].draw(325, 50)
			
		if war_clicked == 1:
			index_error = False
			if war_turn_num > len(enemy_hand):
				enemy_score = 0
				game_state = 3
				war_counter = 1
				war_done = True
				war_temp_num = 0
				one_in_a_million = False
				index_error = True
					
			elif war_turn_num > len(player_hand):
				player_score = 0
				game_state = 3
				war_counter = 1
				war_done = True
				war_temp_num = 0
				one_in_a_million = False
				index_error = True
			if index_error == False:
				if player_hand[war_turn_num].rank > enemy_hand[war_turn_num].rank:
					draw_text("Player Wins", font, BLACK, 325, 275)
					

				elif enemy_hand[war_turn_num].rank > player_hand[war_turn_num].rank:
					draw_text('Enemy Wins', font, BLACK, 325, 275)
					
				if war_temp_num == 0:
					cards_left = 10
				else:
					cards_left = 18
				draw_text(f"Cards to be Won: {cards_left}", font, BLACK, 500, 500)
				
				if war_counter > 0:
					for i in range(3):
						screen.blit(back_img, (510 + (i * 30), 300))
						screen.blit(back_img, (510 + (i * 30), 100))
					player_hand[turn_num + 4 + war_temp_num].draw(600, 300)
					enemy_hand[turn_num + 4 + war_temp_num].draw(600, 100)

					if war_counter > 1:
						player_hand[turn_num + 3 + war_temp_num].draw(570, 300)
						enemy_hand[turn_num + 3 + war_temp_num].draw(570, 100)
					
						if war_counter > 2:
							player_hand[turn_num + 2 + war_temp_num].draw(540, 300)
							enemy_hand[turn_num + 2 + war_temp_num].draw(540, 100)
					
							if war_counter == 4:
								player_hand[turn_num + 1 + war_temp_num].draw(510, 300)
								enemy_hand[turn_num + 1 + war_temp_num].draw(510, 100)
		

#define buttons
next_button = Button(325, 350, back_img)
draw_button = Button(50, 200, next_img)
war_button = Button(510, 300, war_img)
start_button = Button(150, 245, start_img)
exit_button = Button(400, 245, exit_img)
one_in_a_million_button = Button(300, 245, exit_img)
reset_button = Button(150, 245, reset_img)
backarrow_button = Button(25, 15, backarrow_img)


#load in cards and distribute into hands
load_cards()


running = True

while running:
	for event in pygame.event.get():

		#define fps and draw background
		clock.tick(fps)
		draw_bg()


		#check for 8 wars in a row (game ender)
		if one_in_a_million == True:
			game_state = 4
			draw_text("Congrats this is nearly impossible", font, BLACK, 150, 200)
			draw_text("You have won at life", font, BLACK, 260, 350)
			if one_in_a_million_button.draw():
				running = False


		#start of game menu and animations
		if game_state == 0:
			if animation_cooldown_1 < 57:
				for i in range(animation_cooldown_1):
					screen.blit(back_img, (50 + (10 * i), 50))
				animation_cooldown_1 += 1
			else:
				for i in range(56):
					screen.blit(back_img, (50 + (10 * i), 50))
			
			if animation_cooldown_2 < 57:
				for x in range(animation_cooldown_2):
					screen.blit(back_img, (600 - (10 * x), 350))
				animation_cooldown_2 += 1
			else:
				for x in range(57):
					screen.blit(back_img, (600 - (10 * x), 350))
			
				draw_text("War", bigfont, BLACK, 300, 100)
				
				if start_button.draw():
					game_state = 1
					temp_game_started = True
				if exit_button.draw():
					running = False
		index_error = False
		if war_turn_num > len(enemy_hand):
			enemy_score = 0
			game_state = 3
			war_counter = 1
			war_done = True
			war_temp_num = 0
			one_in_a_million = False
			index_error = True
			war_turn_num = 0
		
		if war_turn_num > len(player_hand):
			player_score = 0
			game_state = 3
			war_counter = 1
			war_done = True
			war_temp_num = 0
			one_in_a_million = False
			index_error = True
			war_turn_num = 0

		
		#war checker
		if index_error == False:
			if player_hand[turn_num].rank == enemy_hand[turn_num].rank and game_started == True and one_in_a_million == False:
				game_state = 2
				
		#normal game loop		
		if game_state == 1 and index_error == False:
			#check to make sure if the button is clicked it hasn't been clicked already
			if next_button.draw() and clicked == 0:
				clicked = 1
				if player_hand[turn_num].rank > enemy_hand[turn_num].rank:
					player_score += 1
					enemy_score -= 1
					player_hand.append(player_hand[turn_num])
					player_hand.append(enemy_hand[turn_num])

						
				elif enemy_hand[turn_num].rank > player_hand[turn_num].rank:

					enemy_score += 1
					player_score -= 1
					enemy_hand.append(player_hand[turn_num])
					enemy_hand.append(enemy_hand[turn_num]) 

				temp_turn_num += 1

				
		#war loop	
		elif game_state == 2:
			if next_button.draw() and clicked == 0:
				clicked = 1
			if clicked == 1:
				if war_button.draw() and war_clicked == 0:
					war_clicked = 1

					#logic to update war turn number 
					if war_counter == 1:
						if war_temp_num == 0:
							war_turn_num = turn_num + 4
						else:
							war_turn_num = turn_num + 8
					elif war_counter == 2:
						if war_temp_num == 0:
							war_turn_num = turn_num + 3
						else:
							war_turn_num = turn_num + 7
					elif war_counter == 3:
						if war_temp_num == 0:
							war_turn_num = turn_num + 2
						else:
							war_turn_num = turn_num + 6
					elif war_counter == 5:
						if war_temp_num == 0:
							war_turn_num = turn_num + 1
						else:
							war_turn_num = turn_num + 5


					#check in case war_turn_num is out of range of the hands
					index_error = False
					if war_turn_num > len(enemy_hand):
						enemy_score = 0
						game_state = 3
						war_counter = 1
						war_done = True
						war_temp_num = 0
						one_in_a_million = False
						index_error = True
						war_turn_num = 0
					
					if war_turn_num > len(player_hand):
						player_score = 0
						game_state = 3
						war_counter = 1
						war_done = True
						war_temp_num = 0
						one_in_a_million = False
						index_error = True
						war_turn_num = 0


					if index_error == False:

						#another war
						if player_hand[war_turn_num].rank == enemy_hand[war_turn_num].rank:
							war_counter += 1

						#player > enemy
						elif player_hand[war_turn_num].rank > enemy_hand[war_turn_num].rank:	
							#update points and add cards to hands
							if war_temp_num == 0:
								for i in range(0, 4):
									player_hand.append(player_hand[turn_num + i])
									player_hand.append(enemy_hand[turn_num + i])
								player_score += 5
								enemy_score -= 5
								temp_turn_num += 5

							if war_temp_num > 0:
								for i in range(0, 8):
									player_hand.append(player_hand[turn_num + i])
									player_hand.append(enemy_hand[turn_num + i])
								player_score += 9
								enemy_score -= 9
								temp_turn_num += 9
							
							#reset war variables
							war_counter = 1
							war_done = True
							war_temp_num = 0
							one_in_a_million = False

						#enemy > player
						elif player_hand[war_turn_num].rank < enemy_hand[war_turn_num].rank:
							#update points and add cards to hands	
							if war_temp_num == 0:
								for i in range(0, 4):
									enemy_hand.append(player_hand[turn_num + i])
									enemy_hand.append(enemy_hand[turn_num + i])
								enemy_score += 5
								player_score -= 5
								temp_turn_num += 5

							if war_temp_num > 0:
								for i in range(0, 8):
									enemy_hand.append(player_hand[turn_num + i])
									enemy_hand.append(enemy_hand[turn_num + i])
								enemy_score += 9
								player_score -= 9
								temp_turn_num += 9
							
							#reset war variables	
							war_counter = 1
							war_done = True
							war_temp_num = 0
							one_in_a_million = False
		
		#post game loops					
		elif game_state == 3:

			
				
			#animation
			if animation_cooldown_1 < 57:
				for i in range(animation_cooldown_1):
					screen.blit(back_img, (50 + (10 * i), 50))
				animation_cooldown_1 += 1
			else:
				for i in range(56):
					screen.blit(back_img, (50 + (10 * i), 50))
			
			if animation_cooldown_2 < 57:
				for x in range(animation_cooldown_2):
					screen.blit(back_img, (600 - (10 * x), 350))
				animation_cooldown_2 += 1
			else:
				for x in range(57):
					screen.blit(back_img, (600 - (10 * x), 350))	
					
				
			if enemy_score < 1:
				draw_text("You Won!!", bigfont, BLACK, 150, 100)
			elif player_score < 1:
				draw_text("Enemy Won!!", bigfont, BLACK, 75, 100)

					
					
			if reset_button.draw():
				if player_score < 1:
					enemy_wins += 1
				elif enemy_score < 1:
					player_wins += 1
				#make lists
				clubs = []
				clubs.append(spade3_img)
				hearts = []
				hearts.append(spade3_img)
				spades = []
				spades.append(spade3_img)
				diamonds = []
				diamonds.append(spade3_img)



				#make hands
				player_hand = []
				enemy_hand = []

				#scores for point keeping
				player_score = 26
				enemy_score = 26

				#turn keepers
				turn_num = 1
				clicked = 0
				fill_counter = 0
				game_state = 0
				temp_turn_num = 1

				#deck moving counter
				enemy_move = 1
				player_move = 1

				#war variables
				war_counter = 1
				war_clicked = 0
				war_done = False

				#load in cards and distribute into hands
				load_cards()

				game_state = 1

				multi_games = True

			if exit_button.draw():
				running = False

			

		#back arrow
		if game_state == 1 or game_state == 2:
			if backarrow_button.draw():
				#make lists
				clubs = []
				clubs.append(spade3_img)
				hearts = []
				hearts.append(spade3_img)
				spades = []
				spades.append(spade3_img)
				diamonds = []
				diamonds.append(spade3_img)



				#make hands
				player_hand = []
				enemy_hand = []

				#scores for point keeping
				player_score = 26
				enemy_score = 26

				#turn keepers
				turn_num = 1
				clicked = 0
				fill_counter = 0
				game_state = 0
				temp_turn_num = 1

				#deck moving counter
				enemy_move = 1
				player_move = 1

				#war variables
				war_counter = 1
				war_clicked = 0
				war_done = False

				#load in cards and distribute into hands
				load_cards()

				game_state = 0

		#go to next turn
		if clicked == 1:
			if game_state == 2 and war_done == True:
				if draw_button.draw():
					clicked = 0
					war_clicked = 0

			elif game_state == 1:
				if draw_button.draw():
					clicked = 0


		
		
		if game_state == 1 or game_state == 2:
			#animate points and stuff
			draw_text("You", font, BLACK, 365, 540)
			draw_text("Enemy", font, BLACK, 350, 20)
			draw_text(f'Your Cards: {player_score}', font, BLACK, 30, 50)
			draw_text(f'Enemy Cards: {enemy_score}', font, BLACK, 545, 50)
			if multi_games:
				draw_text(f'Your Wins: {player_wins}', font, BLACK, 30, 450)
				draw_text(f'Enemy Wins: {enemy_wins}', font, BLACK, 30, 500)


			if war_counter > 4:
				war_counter = 1
				war_temp_num += 4

			if war_temp_num > 4:
				one_in_a_million = True
			draw_cards(war_temp_num, war_turn_num, turn_num, game_state, clicked, war_counter, war_done)

		#game started variable to help with start of game animations
		if game_started == False:
			if temp_game_started == True:
				game_started = True
		
		#update turn after the cards have been drawn
		if clicked == 0:
			turn_num = temp_turn_num
			if war_done == True:
				war_done = False
				game_state = 1

		if player_score < 1 or enemy_score < 1:
			game_state = 3

		
		if event.type == pygame.QUIT:
			running = False

    

        

	pygame.display.update()


pygame.quit()
