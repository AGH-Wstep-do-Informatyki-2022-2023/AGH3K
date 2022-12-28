from pygame.math import Vector2

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

LAYERS = {
	'water': 0,
	'ground': 1,
	'soil': 2,
	'soil water': 3,
	'rain floor': 4,
	'house bottom': 5,
	'ground plant': 6,
	'main': 7,
	'house top': 8,
	'fruit': 9,
	'rain drops': 10
}
# Wywaliłem to bo póki co jest zbędne i tak bedzie zmieniane, jak sie wszystko wywali to wtedy bedziemy sie martwic xdd