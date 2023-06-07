import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 25

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.camera = Camera()
        self.player_x = width // 2
        self.player_y = height // 2

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.set_viewport(
            self.camera.camera_x * self.camera.zoom,
            (self.camera.camera_x + SCREEN_WIDTH) * self.camera.zoom,
            self.camera.camera_y * self.camera.zoom,
            (self.camera.camera_y + SCREEN_HEIGHT) * self.camera.zoom
        )
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.RED)
        arcade.draw_rectangle_filled(400, 200, 80, 40, arcade.color.GREEN)

    def update(self, delta_time):
        self.camera.target_x = self.player_x - SCREEN_WIDTH // 2
        self.camera.target_y = self.player_y - SCREEN_HEIGHT // 2

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= MOVEMENT_SPEED
            self.camera.camera_x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_x += MOVEMENT_SPEED
            self.camera.camera_x += MOVEMENT_SPEED
            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            self.camera.camera_x -= dx
            self.camera.camera_y -= dy

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.camera.zoom += scroll_y * 0.1


class Camera:
    def __init__(self):
        self.camera_x = 0
        self.camera_y = 0
        self.zoom = 1.0

if __name__ == "__main__":
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
