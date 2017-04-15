from pygame import draw
from math import sin, pi

class SineWave:
	def __init__(self, x, y, w, amp, freq, phase=0, samples=640, color=(255, 255, 255)):
		self.x = x
		self.y = y
		self.w = w
		self.amp = amp
		self.freq = freq
		self.phase = phase
		self.samples = samples
		self.color = color
		self.refresh()

	def refresh(self):
		self.pts = []
		for i in range(0, self.samples):
			self.pts.append(( int((i / self.samples) * self.w + self.x), int(self.amp * sin(2 * pi * self.freq * (i * self.w / self.samples - self.phase * self.w) / self.w) + self.y )))

	def draw(self, win):
		self.refresh()
		draw.lines(win, self.color, False, self.pts, 1)