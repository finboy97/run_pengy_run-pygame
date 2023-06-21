import pygame
import random
from source import icicle
pygame.init()

class IcicleSpawner():

    def __init__(self):

        self.ms_since_last_icicle = 0
        self.max_icicle_interval = 8000

    def spawn_icicle(self):
        pass

    def tick(self, clock_tick:int):
        self.ms_since_last_icicle += clock_tick

    def should_icicle_spawn(self):
        """
        Method checking if an icicle should spawn or not.
        :return: Boolean
        """
        new_random_number = random.Randint(900,9000)
        if self.ms_since_last_icicle < self.max_icicle_interval:
            print(True)
            return new_random_number < self.ms_since_last_icicle

        new_random_number < self.max_icicle_interval
        print(True)


    def spawn_icicle(self):
        """
        Instantiates a new icicle object.
        :return: None
        """


    def reset_timer(self):
        self.ms_since_last_icicle=0



def main():
    test_icicle_spawner = IcicleSpawner()
    test_clock = pygame.time.Clock

    while True:
        test_clock.tick(60)
        test_icicle_spawner.tick(test_clock.get_time())

main()