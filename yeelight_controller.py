from time import sleep
from yeelight import Bulb


class YeelightController():
    """Controller Yeelight Bulb.
    """

    def __init__(self, host):
        self.bulb: Bulb = Bulb(host)
        self.bulb.start_music()

    def _get_rgb_from_int(rgb):
        blue =  rgb & 255
        green = (rgb >> 8) & 255
        red =   (rgb >> 16) & 255
        return red, green, blue

    def set_color(self, r, g, b, duration=1000):
        """Sets a new color.

        Args:
            r (int): The new red value.
            g (int): The new green value.
            b (int): The new blue value.
            duration (float): Duration in milisseconds of the color transition.

        """
        if r == 0 and g == 0 and b == 0:
            self.bulb.turn_off()
            return
        
        self.bulb.turn_on(effect='sudden')
        sleep(0.25)
        self.bulb.set_rgb(int(r), int(g), int(b), duration=duration)

    def get_color(self):
        """Returns the current color.

        Returns:
            tuple: (R, G, B). The current color.

        """
        rgb_int = int(self.bulb.get_properties(['rgb'])['rgb'])
        r, g, b = self._get_rgb_from_int(rgb_int)
        return r, g, b

    def __del__(self):
        """Stops the music mode."""
        self.bulb.stop_music()
