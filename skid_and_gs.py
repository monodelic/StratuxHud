import pygame

from lib.display import *
from lib.task_timer import TaskTimer


class SkidAndGs(object):
    def __init__(self, degrees_of_pitch, pixels_per_degree_y, font, framebuffer_size):
        self.task_timer = TaskTimer('SkidAndGs')
        self.__font__ = font
        center_y = framebuffer_size[1] >> 2
        text_half_height = int(font.get_height()) >> 1
        self.__text_y_pos__ = (text_half_height << 2) + \
            center_y - text_half_height
        self.__rhs__ = int(0.9 * framebuffer_size[0])

    def render(self, framebuffer, orientation):
        self.task_timer.start()
        g_load_text = "{0:.1f}Gs".format(orientation.g_load)
        texture = self.__font__.render(
            g_load_text, True, WHITE, BLACK)
        text_width, text_height = texture.get_size()

        framebuffer.blit(
            texture, (self.__rhs__ - text_width, self.__text_y_pos__))
        self.task_timer.stop()


if __name__ == '__main__':
    import hud_elements
    hud_elements.run_ahrs_hud_element(SkidAndGs)
