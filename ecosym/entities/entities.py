from pydantic import BaseModel
from pydantic import BaseModel, Field
from enum import Enum
from uuid import uuid4
from abc import abstractmethod
import random


from ecosym.domain.position import Position
from ecosym.utils import shuffle_list
from ecosym.world import World


class AgentType(str, Enum):
    GENERIC = 'generic'
    HERBIVORE = 'herbivore'
    CARNIVORE = 'carnivore'
    
    
class Entity(BaseModel):
    pass


class Agent(Entity):
    id: uuid4 = Field(default_factory=uuid4)
    type: AgentType = AgentType.GENERIC
    position: Position = Field(default_factory=Position)
    
    @abstractmethod
    def act(self, world: World) -> None:
        raise NotImplementedError
    
    def __repr__(self):
        return f"{self.type}, {self.position.__repr__()}, {self.id}"


class Herbivore(Agent):
    type: AgentType = AgentType.HERBIVORE
    
    def act(self, world: World) -> None:
        self.move(world)
    
    def move(self, world: World) -> None:
        possible_new_positions = self.generate_new_positions(
            old_position=self.position,
            world=world
        )
        possible_new_positions = shuffle_list(possible_new_positions)
        for new_position in possible_new_positions:
            if world._position_is_free(layer=1, position=new_position):
                world.layers[1].pop(self.position)
                world.layers[1][new_position] = self
                self.position = new_position    

    @staticmethod
    def generate_new_positions(old_position: Position, world: World) -> list[Position]:
        """
        Generate n new positions
        """
        new_positions = []
        for i in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                new_position = Position(
                    x=old_position.x + i,
                    y=old_position.y + y,
                )
                if new_position.x < world.size and new_position.y < world.size:
                    new_positions.append(new_position)
                    
        return new_positions
    

class Carnivore(Agent):
    type: AgentType = AgentType.CARNIVORE  

