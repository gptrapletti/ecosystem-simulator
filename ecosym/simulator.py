import sys
import pygame

from ecosym.world import World


SCALING = 8
FPS = 10


class Simulator:
    """
    Class used just to represent the World object on the interface and running the simulation.
    """
    def __init__(
        self,
        world: World,
    ):
        self.world = world
        self.scaling = SCALING
        self.fps = FPS
        self._setup_simulation()
        self.running = None
        self.epoch = 1
        

    def run(self):
        self.running = True
        while self.running:
            print(f"Epoch {self.epoch}")
            self._handle_events()
            self.world.next_epoch()
            self.draw_world()
            self.clock.tick(self.fps)
            self.epoch += 1
        
        pygame.quit()

    def _setup_simulation(self) -> None:
        pygame.init()
        # Off-screen surface where set the actual simulation
        self.arena = pygame.Surface((self.world.size, self.world.size))
        # Window where watch the simulation
        self.screen = pygame.display.set_mode(
            size=(self.world.size * self.scaling, self.world.size * self.scaling)
        )
        pygame.display.set_caption('ecosym')
        self.clock = pygame.time.Clock()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def draw_world(self) -> None:
        self.arena.fill((0, 0, 0)) # NOTE: try to update just the pixels that actually changed, for computational efficiency
        for position, entity in self.world.layers[1].items(): # TODO: deal with different layers
            pygame.draw.rect(
                surface=self.arena, 
                color=entity.color,
                rect=(position.x, position.y, 1, 1) 
            )
        scaled_arena = pygame.transform.scale(self.arena, self.screen.get_size())
        self.screen.blit(scaled_arena, (0, 0))
        pygame.display.flip()