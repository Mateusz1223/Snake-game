from constants import *
import arcade
import random

class Player:
    def __init__(self):
        self.direction = 'E'
        self.head_position_x = None
        self.head_position_y = None
        self.body_list = []

class Apple:
    def __init__(self):
        self.is_eaten = True
        self.sprite = None

        img = "textures/apple.png"
        self.sprite = arcade.Sprite(img, 1)

class Game:
    def __init__(self):
        pass

    def setup(self):
        self.score = 0
        self.game_over = False

        self.player = Player()
        self.apple = Apple()

        # Set up the player
        self.player.direction = RIGHT
        self.player.head_position_x = FRAME_SIZE + TILE_SIZE + TILE_SIZE/2
        self.player.head_position_y = FRAME_SIZE + MAP_SIZE/2

        head_sprite = arcade.Sprite("textures/snake_body.png", 1)
        head_sprite.center_x = self.player.head_position_x
        head_sprite.center_y = self.player.head_position_y
        self.player.body_list.append(head_sprite)

        head_sprite = arcade.Sprite("textures/snake_body.png", 1)
        head_sprite.center_x = self.player.head_position_x - TILE_SIZE
        head_sprite.center_y = self.player.head_position_y
        self.player.body_list.append(head_sprite)

        self.paused = False

    def update(self):
        if not self.game_over and not self.paused:
            if self.player.direction == UP:
                self.player.head_position_y += TILE_SIZE
            elif self.player.direction == DOWN:
                self.player.head_position_y -= TILE_SIZE
            elif self.player.direction == RIGHT:
                self.player.head_position_x += TILE_SIZE
            elif self.player.direction == LEFT:
                self.player.head_position_x -= TILE_SIZE

            # Game Over colisions
            if self.player.head_position_x < FRAME_SIZE or self.player.head_position_x > FRAME_SIZE+MAP_SIZE:
                self.game_over = True
            elif self.player.head_position_y < FRAME_SIZE or self.player.head_position_y > FRAME_SIZE+MAP_SIZE:
                self.game_over = True

            for each in self.player.body_list:
                if each.center_x == self.player.head_position_x and each.center_y == self.player.head_position_y:
                    self.game_over = True
                    break

            if not self.game_over:
                # Collision with apple
                if self.player.head_position_x == self.apple.sprite.center_x and self.player.head_position_y == self.apple.sprite.center_y:
                    new_head_sprite = arcade.Sprite("textures/snake_body.png", 1)
                    self.player.body_list.append(new_head_sprite)
                    self.apple.is_eaten = True
                    self.score += 1

                new_head = self.player.body_list.pop()
                new_head.center_x = self.player.head_position_x
                new_head.center_y = self.player.head_position_y
                self.player.body_list.insert(0, new_head)

            if self.apple.is_eaten:
                self.apple.sprite.center_x = FRAME_SIZE + random.randint(0, 16)*TILE_SIZE + TILE_SIZE / 2
                self.apple.sprite.center_y = FRAME_SIZE + random.randint(0, 16)*TILE_SIZE + TILE_SIZE / 2
                self.apple.is_eaten = False

    def draw(self):
        output = "Score: " + str(self.score)
        # Put the text on the screen.
        arcade.draw_text(text=output, start_x=FRAME_SIZE, start_y=590,
                         color=arcade.color.BLACK, font_size=25, font_name=FONT_NAME)

        arcade.draw_lrtb_rectangle_filled(FRAME_SIZE, FRAME_SIZE + MAP_SIZE, MAP_SIZE + FRAME_SIZE, FRAME_SIZE,
                                          arcade.color.BITTER_LEMON)

        # Draw our sprites
        self.apple.sprite.draw()

        for each in self.player.body_list:
            each.draw()

        if self.paused:
            arcade.draw_lrtb_rectangle_filled(FRAME_SIZE, FRAME_SIZE + MAP_SIZE, MAP_SIZE + FRAME_SIZE, FRAME_SIZE,
                                              (132, 132, 130, 150) )

            input = "Game Paused"
            font_siz = 30
            error = 10
            arcade.draw_text(text=input, start_x=(SCREEN_WIDTH - (len(input) * font_siz - error)) / 2, start_y=400,
                             color=arcade.color.BLACK, font_size=font_siz, font_name=FONT_NAME)

            input = "To reasume press ESCAPE"
            font_siz = 20
            error = 30
            arcade.draw_text(text=input, start_x=(SCREEN_WIDTH - (len(input) * font_siz - error)) / 2, start_y=300,
                             color=arcade.color.BLACK, font_size=font_siz, font_name=FONT_NAME)

    def is_game_over(self):
        return self.game_over

    def get_score(self):
        return self.score

    def set_direction(self, direction):
        if not self.paused:
            self.player.direction = direction

    def pause_unpause(self):
        if self.paused == False:
            self.paused = True
        else:
            self.paused = False
