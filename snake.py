from PIL import Image, ImageDraw
import pygame
import time


SIZE = 40
BACKGROUND_COLOR = (226,190,162)


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = Image.open("resources/circular_block.png").convert("RGBA")
        self.direction = 'down'
        self.snake_speed = 0.1 # Initial speed of the snake
        self.default_snake_speed = 0.1

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
       
        speed_factor = self.snake_speed
        time.sleep(speed_factor)
        self.draw()

    def draw(self):
        for i in range(self.length):
            pygame_surface = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode).convert_alpha()
            self.parent_screen.blit(pygame_surface, (self.x[i], self.y[i]))

            # Add eyes to the snake's head
            if i == 0:
                eye_position_left = (self.x[i] + SIZE // 6, self.y[i] + SIZE // 4)
                eye_position_right = (self.x[i] + 3 * SIZE // 6, self.y[i] + SIZE // 4)

                # Adjust eye positions based on direction
                if self.direction == 'left':
                    eye_position_left = (self.x[i] + SIZE // 6, self.y[i] + SIZE // 4)
                    eye_position_right = (self.x[i] + 3 * SIZE // 6, self.y[i] + SIZE // 4)
                elif self.direction == 'right':
                    eye_position_left = (self.x[i] + SIZE // 2, self.y[i] + SIZE // 4)
                    eye_position_right = (self.x[i] + 5 * SIZE // 6, self.y[i] + SIZE // 4)
                elif self.direction == 'up':
                    eye_position_left = (self.x[i] + SIZE // 4, self.y[i] + SIZE // 6)
                    eye_position_right = (self.x[i] + 3 * SIZE // 4, self.y[i] + SIZE // 6)
                elif self.direction == 'down':
                    eye_position_left = (self.x[i] + SIZE // 4, self.y[i] + SIZE // 2)
                    eye_position_right = (self.x[i] + 3 * SIZE // 4, self.y[i] + SIZE // 2)

                pygame.draw.circle(self.parent_screen, (0, 0, 0), eye_position_left, SIZE // 15)  # Left eye
                pygame.draw.circle(self.parent_screen, (0, 0, 0), eye_position_right, SIZE // 15)  # Right eye

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    def increase_speed(self):
     # Adjust the threshold as needed
      if self.snake_speed > 0.001:
            self.snake_speed -= 0.001
