import arcade
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Snake"

TILE_SIZE = 30
MAP_SIZE = 17*TILE_SIZE
FRAME_SIZE = (SCREEN_WIDTH - MAP_SIZE)/2

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

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

class Game(arcade.Window):

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.set_update_rate(1 / 5)

        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        self.score = 0
        self.game_over = False

        self.player = Player()
        self.apple = Apple()

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Set up the player

        self.player.direction = RIGHT
        self.player.head_position_x = FRAME_SIZE + TILE_SIZE + TILE_SIZE/2
        self.player.head_position_y = FRAME_SIZE + MAP_SIZE/2

        head_sprite = arcade.SpriteSolidColor(TILE_SIZE, TILE_SIZE, arcade.color.AZURE)
        head_sprite.center_x = self.player.head_position_x
        head_sprite.center_y = self.player.head_position_y
        self.player.body_list.append(head_sprite)

        head_sprite = arcade.SpriteSolidColor(TILE_SIZE, TILE_SIZE, arcade.color.AZURE)
        head_sprite.center_x = self.player.head_position_x - TILE_SIZE
        head_sprite.center_y = self.player.head_position_y
        self.player.body_list.append(head_sprite)

    def on_update(self, delta_time):
        if not self.game_over:
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
                    new_head_sprite = arcade.SpriteSolidColor(TILE_SIZE, TILE_SIZE, arcade.color.AZURE)
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

    def on_draw(self):
        """Render the screen."""
        self.clear()

        output = "Score: " + str(self.score)
        # Put the text on the screen.
        arcade.draw_text(text=output, start_x=FRAME_SIZE, start_y=590,
                         color=arcade.color.BLACK, font_size=25)

        arcade.draw_lrtb_rectangle_filled(FRAME_SIZE, FRAME_SIZE+MAP_SIZE, MAP_SIZE+FRAME_SIZE, FRAME_SIZE, arcade.color.BITTER_LEMON)

        # Draw our sprites
        self.apple.sprite.draw()

        for each in self.player.body_list:
            each.draw()

        if self.game_over:
            arcade.draw_text(text="GAME OVER!", start_x=120, start_y=300, color=arcade.color.BLACK, font_size=40)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.player.direction = UP
        elif symbol == arcade.key.S:
            self.player.direction = DOWN
        elif symbol == arcade.key.D:
                self.player.direction = RIGHT
        elif symbol == arcade.key.A:
                self.player.direction = LEFT