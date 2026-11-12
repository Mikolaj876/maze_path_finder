from path_finder import Path
import pygame

pygame.init()

class Bot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.path = []

    def draw_bot(self, screen, square_size, color=(166, 60, 60)):
        rect = pygame.Rect(self.x * square_size, self.y * square_size, square_size, square_size)
        pygame.draw.rect(screen, color, rect)

class Game():
    def __init__(self):
        self.running = True
        self.start = (0,0)
        self.end = (7,7)
        self.path = Path(self.start, self.end)
        self.square_size = 100

        self.path.grid = [  [0, 0, 1, 1, 1, 1, 1, 1], # 0 is empty, 1 - wall, 2 - start, 3 - end
                            [1, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 1, 1, 0, 1, 0, 1],
                            [1, 0, 0, 1, 0, 0, 0, 1],
                            [1, 1, 0, 1, 1, 1, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 0],
                            [0, 0, 1, 1, 1, 1, 1, 1]]

        self.grid = self.path.grid
        self.grid[self.end[1]][self.end[0]] = 3
        self.grid[self.start[1]][self.start[0]] = 2
        self.screen_x = len(self.grid[0]) * self.square_size
        self.screen_y = len(self.grid) * self.square_size

        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.color_table = {0:(255,255,255), 1:(0,0,0), 2:(255, 255, 0), 3:(0, 255, 0)}

        self.bot = Bot()

        self.path_actual = self.path.shortest_path()
        self.indx = 0
        self.clock = pygame.Clock()


        self.fps = 10
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False    

            self.screen.fill((255,255,255))   
            self.draw_grid()
            if self.indx < len(self.path_actual):    
                self.symulate_bot()

            else:
                self.freeze_bot_draw()

            self.clock.tick(self.fps)
            pygame.display.update()

    def draw_grid(self):
        row_counter = 0
        for row in self.grid:
            pixel_counter = 0
            for pixel in row:
                rect = pygame.Rect((pixel_counter * self.square_size, row_counter * self.square_size), (self.square_size, self.square_size))
                pygame.draw.rect(self.screen, self.color_table[pixel], rect)
                pixel_counter += 1

            row_counter += 1

    def symulate_bot(self):
        self.bot.x, self.bot.y = self.path_actual[self.indx]
        self.bot.draw_bot(self.screen, 100, (166, 60, 60))
        self.indx += 1

    def freeze_bot_draw(self):
        self.bot.draw_bot(self.screen, 100, (166, 60, 60))

game = Game()
game.run()