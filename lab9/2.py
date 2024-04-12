import pygame
import random
import time

pygame.init()

# Set up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = RIGHT

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.timer = 0
        self.weighted_foods = [(RED, random.randint(1, 5))]  # Colors for different weighted foods
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
        self.timer = time.time() + random.randint(3, 6)  # Randomize timer for food disappearance

    def draw(self, surface):
        # Check if food should disappear
        if time.time() >= self.timer:
            self.randomize_position()
        else:
            choice = random.choices(self.weighted_foods, [w[1] for w in self.weighted_foods])[0]
            color, _ = choice
            r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

            return self.position

# Main function
def main():
    snake = Snake()
    food = Food()
    score = 0
    level = 1
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        snake.handle_keys()
        snake.move()

        food_position = food.draw(screen)
        
        # Check for collision with food
        if snake.get_head_position() == food_position:
            snake.length += random.randint(1, 3)
            score += 1

        # Check for border collision
        if (snake.get_head_position()[0] < 0 or snake.get_head_position()[0] >= SCREEN_WIDTH or
                snake.get_head_position()[1] < 0 or snake.get_head_position()[1] >= SCREEN_HEIGHT):
            snake.reset()
            score = 0
            level = 1
            clock.tick(8)

        snake.draw(screen)
        pygame.display.update()
        clock.tick(8 + level)

if __name__ == '__main__':
    main()
