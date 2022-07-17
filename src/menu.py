from constants import *
import arcade

#Menu states
MAIN = 1
CONTROLS = 2
DIFFICULTY = 3

class Button:
    def __init__(self, texture_file, center_x, center_y):
        self.sprite = arcade.Sprite(texture_file, 1)
        self.sprite.center_x = center_x
        self.sprite.center_y = center_y

        self.hoovered_by_mouse = False

    def draw(self):
        self.sprite.draw()

    def hoover(self):
        self.hoovered_by_mouse = True
        self.sprite.scale = 1.05

    def unhoover(self):
        self.hoovered_by_mouse = False
        self.sprite.scale = 1

    def is_hoovered(self):
        return self.hoovered_by_mouse


class Menu:
    def __init__(self):
        self.best_score = 0
        self.last_score = 0

        self.play_button = Button("textures/play_button.png", 300, 390)
        self.controls_button = Button("textures/controls_button.png", 300, 280)
        self.difficulty_button = Button("textures/difficulty_button.png", 300, 190)
        self.exit_button = Button("textures/exit_button.png", 520, 50)

        self.easy_button = Button("textures/easy_button.png", 300, 420)
        self.normal_button = Button("textures/normal_button.png", 300, 320)
        self.hard_button = Button("textures/hard_button.png", 300, 220)
        self.back_button = Button("textures/back_button.png", 80, 50)

        self.difficulty = NORMAL

    def setup(self):
        self.play_button_pressed = False
        self.state = MAIN

    def update(self):
        if self.state == DIFFICULTY:
            if not self.easy_button.is_hoovered():
                self.easy_button.sprite.scale = 1
            if not self.normal_button.is_hoovered():
                self.normal_button.sprite.scale = 1
            if not self.hard_button.is_hoovered():
                self.hard_button.sprite.scale = 1

            if self.difficulty == EASY:
                self.easy_button.sprite.scale = 1.1
            elif self.difficulty == NORMAL:
                self.normal_button.sprite.scale = 1.1
            elif self.difficulty == HARD:
                self.hard_button.sprite.scale = 1.1

    def draw(self):
        input = "Snake game"
        font_siz = 40
        error = 10
        arcade.draw_text(text=input, start_x=(SCREEN_WIDTH - (len(input) * font_siz - error)) / 2, start_y=540,
                         color=arcade.color.BLACK, font_size=font_siz, font_name=FONT_NAME)

        if self.state == MAIN:
            input = "Last score: " + str(self.last_score) + "    Best score: " + str(self.best_score)
            font_siz = 14
            error = 85
            arcade.draw_text(text=input, start_x=(SCREEN_WIDTH-(len(input)*font_siz-error))/2, start_y=470,
                             color=arcade.color.BLACK, font_size=font_siz, font_name=FONT_NAME)
            self.play_button.draw()
            self.controls_button.draw()
            self.difficulty_button.draw()
        elif self.state == CONTROLS:
            input = "W / ARROW UP -> Move up"
            arcade.draw_text(text=input, start_x=110, start_y=470,
                             color=arcade.color.BLACK, font_size=15, font_name=FONT_NAME)
            input = "S / ARROW Down -> Move down"
            arcade.draw_text(text=input, start_x=110, start_y=400,
                             color=arcade.color.BLACK, font_size=15, font_name=FONT_NAME)
            input = "A / LEFT ARROW -> Move left"
            arcade.draw_text(text=input, start_x=110, start_y=330,
                             color=arcade.color.BLACK, font_size=15, font_name=FONT_NAME)
            input = "D / RIGHT ARROW -> Move right"
            arcade.draw_text(text=input, start_x=110, start_y=260,
                             color=arcade.color.BLACK, font_size=15, font_name=FONT_NAME)
            input = "ESCAPE -> Pause game"
            arcade.draw_text(text=input, start_x=110, start_y=190,
                             color=arcade.color.BLACK, font_size=15, font_name=FONT_NAME)

            self.back_button.draw()
        elif self.state == DIFFICULTY:
            self.easy_button.draw()
            self.normal_button.draw()
            self.hard_button.draw()
            self.back_button.draw()

        self.exit_button.draw()

    def is_play_button_pressed(self):
        return self.play_button_pressed

    def get_difficulty(self):
        return self.difficulty

    def set_last_score(self, score):
        self.last_score = score
        if score > self.best_score:
            self.best_score = score

    def change_play_button_texture(self):
        self.play_button = Button("textures/play_again_button.png", 300, 390)

    def back_to_main_menu(self):
        self.state = MAIN

    def mouse_motion_handler(self, x, y):
        if self.state == MAIN:
            self.play_button.unhoover()
            self.controls_button.unhoover()
            self.difficulty_button.unhoover()
        if self.state == CONTROLS:
            self.back_button.unhoover()
        elif self.state == DIFFICULTY:
            self.easy_button.unhoover()
            self.normal_button.unhoover()
            self.hard_button.unhoover()
            self.back_button.unhoover()

        self.exit_button.unhoover()

        if self.state == MAIN:
            if y > self.play_button.sprite.bottom and y < self.play_button.sprite.bottom + self.play_button.sprite.height and x > self.play_button.sprite.left and x < self.play_button.sprite.left + self.play_button.sprite.width:
                self.play_button.hoover()
            elif y > self.controls_button.sprite.bottom and y < self.controls_button.sprite.bottom + self.controls_button.sprite.height and x > self.controls_button.sprite.left and x < self.controls_button.sprite.left + self.controls_button.sprite.width:
                self.controls_button.hoover()
            elif y > self.difficulty_button.sprite.bottom and y < self.difficulty_button.sprite.bottom + self.difficulty_button.sprite.height and x > self.difficulty_button.sprite.left and x < self.difficulty_button.sprite.left + self.difficulty_button.sprite.width:
                self.difficulty_button.hoover()
        elif self.state == CONTROLS:
            if y > self.back_button.sprite.bottom and y < self.back_button.sprite.bottom + self.back_button.sprite.height and x > self.back_button.sprite.left and x < self.back_button.sprite.left + self.back_button.sprite.width:
                self.back_button.hoover()
        elif self.state == DIFFICULTY:
            if y > self.easy_button.sprite.bottom and y < self.easy_button.sprite.bottom + self.easy_button.sprite.height and x > self.easy_button.sprite.left and x < self.easy_button.sprite.left + self.easy_button.sprite.width:
                self.easy_button.hoover()
            elif y > self.normal_button.sprite.bottom and y < self.normal_button.sprite.bottom + self.normal_button.sprite.height and x > self.normal_button.sprite.left and x < self.normal_button.sprite.left + self.normal_button.sprite.width:
                self.normal_button.hoover()
            elif y > self.hard_button.sprite.bottom and y < self.hard_button.sprite.bottom + self.hard_button.sprite.height and x > self.hard_button.sprite.left and x < self.hard_button.sprite.left + self.hard_button.sprite.width:
                self.hard_button.hoover()
            elif y > self.back_button.sprite.bottom and y < self.back_button.sprite.bottom + self.back_button.sprite.height and x > self.back_button.sprite.left and x < self.back_button.sprite.left + self.back_button.sprite.width:
                self.back_button.hoover()

            if self.difficulty == EASY:
                self.easy_button.sprite.scale = 1.1
            elif self.difficulty == NORMAL:
                self.normal_button.sprite.scale = 1.1
            elif self.difficulty == HARD:
                self.hard_button.sprite.scale = 1.1

        if y > self.exit_button.sprite.bottom and y < self.exit_button.sprite.bottom + self.exit_button.sprite.height and x > self.exit_button.sprite.left and x < self.exit_button.sprite.left + self.exit_button.sprite.width:
            self.exit_button.hoover()

    def mouse_click_handler(self, x, y):
        self.mouse_motion_handler(x, y)

        if self.state == MAIN:
            if self.play_button.is_hoovered():
                self.play_button_pressed = True
            elif self.controls_button.is_hoovered():
                self.state = CONTROLS
            elif self.difficulty_button.is_hoovered():
                self.state = DIFFICULTY
        elif self.state == CONTROLS:
            if self.back_button.is_hoovered():
                self.state = MAIN
        elif self.state == DIFFICULTY:
            if self.easy_button.is_hoovered():
                self.difficulty = EASY
            elif self.normal_button.is_hoovered():
                self.difficulty = NORMAL
            elif self.hard_button.is_hoovered():
                self.difficulty = HARD
            elif self.back_button.is_hoovered():
                self.state = MAIN

        if self.exit_button.is_hoovered():
            arcade.exit()
