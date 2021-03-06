import pygame
import time
import random


pygame.init()
pygame.mixer.music.load('s4.mp3')
crash_sound=pygame.mixer.Sound("s2.wav")


display_width=800
display_height=600
sod_width=100

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
block_color=(51,19,145)
bg_color=(23,24,34)
green=(0,105,34)
gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock=pygame.time.Clock()
car_width=83
car_height=90
carImg = pygame.image.load('car.png')
carImg2= pygame.image.load('car2.png')
def things_dodged(count):
	font = pygame.font.SysFont(None,25)
	text = font.render("Dodged:"+str(count),True,red)
	gameDisplay.blit(text,(0,0))

def sod():
	pygame.draw.rect(gameDisplay,green,(0,0,100,display_height))
	pygame.draw.rect(gameDisplay,green,(700,0,100,display_height))

def things(thingx, thingy, thingw, thingh, color):
	gameDisplay.blit(carImg2,(thingx,thingy))

def tracks(trackx,tracky):
	pygame.draw.rect(gameDisplay,white,(trackx, tracky,25,90))

def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
	textSurface=font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText =pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect= text_objects(text, largeText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():

	#pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	message_display('You crashed')

def game_loop():
	pygame.mixer.music.play(-1)
	x=(display_width*0.45)
	y=(display_height*0.82)
	x_change =0
	y_change =0
	sod_width=100
	thing_width=83
        thing_height=90
	thing_startx = random.randrange(sod_width, display_width-(sod_width))
	thing_starty = -600
	thing_speed = 2
	track_startx = display_width/2
	track_starty = 0
	track_speed=2
	block_count=1
	dodged=0

	gameExit = False

	while not gameExit:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					x_change=-5
				elif event.key == pygame.K_d:
					x_change=5
				if event.key == pygame.K_w:
					y_change=-5
				elif event.key == pygame.K_s:
					y_change=5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d:
					x_change=0
				if event.key == pygame.K_w or event.key == pygame.K_s:
                                        y_change=0

				

		x +=x_change
		y +=y_change
		gameDisplay.fill(bg_color)
		sod()

		tracks(track_startx,track_starty)
               	track_starty += track_speed
		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		thing_starty += thing_speed

		car(x,y)
		things_dodged(dodged)
		if x > display_width-(sod_width + car_width) or x <sod_width:
			crash()
		if y > display_height - car_height or y<0:
			crash()
		if thing_starty > display_height:
			thing_starty= 0 - thing_height
			thing_startx= random.randrange(sod_width, display_width-(sod_width))
			track_starty = 0 - thing_height
			track_startx= display_width/2
			dodged+=1
			thing_speed+=0.25
			track_speed+=0.15
			block_count+=1
			#thing_width += (dodged*1.2)
		if y< thing_starty+thing_height:
			#print('step 1')
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
				#print('x crossover')
				crash()
		pygame.display.update()

		clock.tick(120)


game_loop()
pygame.quit()
quit()


