class Settings():
    """A class to store all settings for Alien Conqueror."""

    def __init__(self):
        """Initialize the game's settings."""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2.0
        self.bullet_speed_factor = 1
        self.bullet_width = 4
        self.bullet_height = 17
        self.bullet_color = 60, 60, 60