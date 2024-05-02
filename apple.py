import random
import pygame
from pygame.locals import *
from PIL import Image, ImageDraw

SIZE = 40
BACKGROUND_COLOR = (226,190,162)
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.fruit_images = ["apple.jpg", "banana.jpg", "grapes.jpg", "orange.jpg", "mango.jpg"]
        self.image = None
        self.x = 120
        self.y = 120
        self.load_image()

    def load_image(self):
        fruit_image_path = random.choice(self.fruit_images)
        image = Image.open("resources/" + fruit_image_path).convert("RGBA")
        image = image.resize((SIZE, SIZE))
        # Remove background (assuming it's white)
        image_data = image.getdata()
        transparent_pixels = [(r, g, b, 0) if r > 200 and g > 200 and b > 200 else (r, g, b, 255) for (r, g, b, a) in image_data]
        image.putdata(transparent_pixels)
        self.image = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert_alpha()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.load_image()
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE