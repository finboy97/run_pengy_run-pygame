import pygame

class Icicle():


    def __init__(self, position: [int,int], screen: pygame.display):
        self.icicle_surface = pygame.image.load("graphics/custom/icicle-cropped.png").convert_alpha()
        self.icicle_vector = position
        self.icicle_rect = self.icicle_surface.get_rect(midbottom=(self.icicle_vector[0], self.icicle_vector[1]))
        self.screen = screen


    # Class methods

    def move_left(self):
        """
            Class for transforming icicle on the screen.
        """
        self.icicle_rect.left -= 5
        return

    def destroy_icicle(self):
        """
        When icicle leaves the screen, then it is destroyed.
        This results in increasing the score by 1.
        :return: None
        """
        return

    def spawn_icicle(self):
        return

    def is_rect_off_edge(self):
        """
        Check if the icicle is off the screen edge.
        :return: True if right side of rectangle has an x coordinate of less than zero.
        """
        return self.icicle_rect.right < 0


    def draw_icicle(self):
        pygame.draw.rect(self.screen,"white",self.icicle_rect)
        self.screen.blit(self.icicle_surface,self.icicle_rect)


    def update_icicle(self):
        """
        Method for telling the icicle to move and for checking if it is off the edge of the screen or not.
        :return:
        """
        self.move_left()
        return self.is_rect_off_edge()

    def get_rect(self):
        return self.icicle_rect