import random

from ecosym.agent_generator import AgentGenerator
from ecosym.domain.position import Position
from ecosym.entities.entities import Herbivore
from ecosym.simulator import Simulator
from ecosym.world import World


def main():    
    world = World()
    
    data = {'herbivore': 100, 'carnivore': 10}
    agent_generator = AgentGenerator(data=data, world_size=world.size)
    agents = agent_generator.execute()
    
    world.spawn(agents)  
    
    simulator = Simulator(world=world)
    simulator.run()
    
if __name__ == '__main__':
    main()