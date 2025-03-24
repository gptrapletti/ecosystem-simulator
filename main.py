import random
from ecosym.domain.position import Position
from ecosym.entities.entities import Herbivore
from ecosym.simulator import Simulator
from ecosym.world import World


def main():
    world = World()
    
    n_agents = 100
    agents = [
        Herbivore(position=Position(
            x=random.randint(0, world.size - 1), 
            y=random.randint(0, world.size - 1),
        ))
        for _ in range(n_agents)
    ]
    for agent in agents:
        try: # since agents may have the same position at this point
            world.add(agent, layer=1, position=agent.position)
        except:
            continue
    
    simulator = Simulator(world=world)
    simulator.run()
    
if __name__ == '__main__':
    main()