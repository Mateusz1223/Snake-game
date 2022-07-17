from constants import *
import arcade
from game import Game
from menu import Menu

class App(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.set_update_rate(1 / 5)

        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        self.game = Game()
        self.menu = Menu()

        self.state = MENU

        self.is_return_to_menu_scheduled = False

    def setup(self):
        self.menu.setup()
        self.game.setup()

    def on_update(self, delta_time):
        if self.state == MENU:
            self.menu.update()
            if self.menu.is_play_button_pressed():
                self.game.setup()
                self.state = GAME
            self.set_update_rate(1 / self.menu.get_difficulty())
        else:
            self.game.update()

            if self.game.is_game_over():
                if self.is_return_to_menu_scheduled == False:
                    arcade.schedule(self.return_to_menu, 1.5)
                    self.is_return_to_menu_scheduled = True

    def on_draw(self):
        """Render the screen."""
        self.clear()

        if self.state == MENU:
            self.menu.draw()
        elif self.state == GAME:
            self.game.draw()

        if self.game.is_game_over() and self.is_return_to_menu_scheduled:
            arcade.draw_text(text="GAME OVER!", start_x=120, start_y=300, color=arcade.color.BLACK, font_size=40,
                             font_name=FONT_NAME)

    def return_to_menu(self, delta_time):
        self.menu.setup()
        self.menu.set_last_score(self.game.get_score())
        self.menu.change_play_button_texture()
        self.state = MENU
        arcade.unschedule(self.return_to_menu)
        self.is_return_to_menu_scheduled = False


    def on_key_press(self, symbol, modifiers):

        if self.state == GAME:
            if symbol == arcade.key.W or symbol == arcade.key.MOTION_UP:
                self.game.set_direction(UP)
            elif symbol == arcade.key.S or symbol == arcade.key.MOTION_DOWN:
                self.game.set_direction(DOWN)
            elif symbol == arcade.key.D or symbol == arcade.key.MOTION_RIGHT:
                self.game.set_direction(RIGHT)
            elif symbol == arcade.key.A or symbol == arcade.key.MOTION_LEFT:
                self.game.set_direction(LEFT)
            elif symbol == arcade.key.ESCAPE:
                self.game.pause_unpause()

        if self.state == MENU:
            if symbol == arcade.key.ESCAPE:
                self.menu.back_to_main_menu()

    def on_mouse_motion(self, x, y, dx, dy):
        #print("x: " + str(x) + ", y: " + str(y) + "\n")

        if self.state == MENU:
            self.menu.mouse_motion_handler(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == MENU and button == 1:
            self.menu.mouse_click_handler(x, y)