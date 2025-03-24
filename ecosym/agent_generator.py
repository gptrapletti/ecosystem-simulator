import random
from typing import List
from ecosym.domain.position import Position
from ecosym.entities.entities import Agent, AgentType, Carnivore, Herbivore


# NOTE: limited for Agents at the moment. Use it also for grass and others?
class AgentGenerator:
    mapping: dict[AgentType, type[Agent]] = {
        AgentType.HERBIVORE: Herbivore,
        AgentType.CARNIVORE: Carnivore,
    }
    
    def __init__(
        self,
        data: dict[AgentType, int],
        world_size: int,
    ) -> None:
        self.data = data
        self.world_size = world_size
        
        self.positions: List[Position] = []
    
    def execute(self) -> List[Agent]: 
        agents = []
        for agent_type, n in self.data.items():
            agents.extend([self.mapping[agent_type]() for _ in range(n)])
            
        self._find_positions(len(agents))
        
        for agent, position in zip(agents, self.positions):
            agent.position = position

        return agents
        
                        
    def _find_positions(self, n: int) -> List[Position]:
        found_positions = 0
        while found_positions < n:
            position = Position(
                x=random.randint(0, self.world_size - 1), 
                y=random.randint(0, self.world_size - 1),
            )
            if position not in self.positions:
                self.positions.append(position)
                found_positions += 1