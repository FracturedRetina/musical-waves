import pygame, sys
from wave import SineWave
from music import *

pygame.init()

win = pygame.display.set_mode((640, 480))
w = SineWave(0, 240, 640, 100, 2)
w2 = get_interval(w, PYTHAGOREAN["P8"])
w2.color = (255, 0, 0)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()
	
	kShift = False
	k2 = False
	k3 = False
	k4 = False
	k5 = False
	k6 = False
	k7 = False
	k8 = False

	if keys[pygame.K_2] and not k2:
		#M2
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and not kShift:
			w2 = get_interval(w, PYTHAGOREAN["M2"])
		#m2
		else:
			w2 = get_interval(w, PYTHAGOREAN["m2"])
		k2 = True
	elif keys[pygame.K_3] and not k3:
		#M3
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and not kShift:
			w2 = get_interval(w, PYTHAGOREAN["M3"])
		#m3
		else:
			w2 = get_interval(w, PYTHAGOREAN["m3"])
		k3 = True
	elif keys[pygame.K_4] and not k4:
		#Tritone
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and not kShift:
			w2 = get_interval(w, PYTHAGOREAN["+4"])
		#P4
		else:
			w2 = get_interval(w, PYTHAGOREAN["P4"])
		k4 = True
	elif keys[pygame.K_5] and not k5:
		#Tritone
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and not kShift:
			w2 = get_interval(w, PYTHAGOREAN["*5"])
		#P5
		else:
			w2 = get_interval(w, PYTHAGOREAN["P5"])
		k5 = True
	elif keys[pygame.K_6] and not k6:
		#M6
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and not kShift:
			w2 = get_interval(w, PYTHAGOREAN["M6"])
		#m6
		else:
			w2 = get_interval(w, PYTHAGOREAN["m6"])
		k6 = True
	elif keys[pygame.K_7] and not k7:
		#M7
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and not kShift:
			w2 = get_interval(w, PYTHAGOREAN["M7"])
		#m7
		else:
			w2 = get_interval(w, PYTHAGOREAN["m7"])
		k7 = True
	elif keys[pygame.K_8] and not k8:
		w2 = get_interval(w, PYTHAGOREAN["P8"])
		k8 = True


	if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
		kShift = True


	w.phase += 0.002
	w2.phase += 0.002

	w2.color = (255, 0, 0)

	win.fill((0,0,0))
	w.draw(win)
	w2.draw(win)
	pygame.display.update()
