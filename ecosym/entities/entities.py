from typing import Tuple
from pydantic import BaseModel
from pydantic import BaseModel, Field
from enum import Enum
from uuid import uuid4
from abc import abstractmethod
import random


from ecosym.domain.position import Position
from ecosym.utils import shuffle_list


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
    layer: int # TODO: riordina attributi in modo sensato
    color: Tuple[int, int, int]
    
    @abstractmethod
    def act(self, world) -> None:
        raise NotImplementedError
    
    def __repr__(self):
        return f"{self.type}, {self.position.__repr__()}, {self.id}"


class Herbivore(Agent):
    type: AgentType = AgentType.HERBIVORE
    layer: int = 1
    color: Tuple[int, int, int] = (0, 255, 0)
    
    def act(self, world) -> None:
        self.move(world)
    
    def move(self, world) -> None:
        possible_new_positions = self.generate_new_positions(
            old_position=self.position,
            world=world
        )
        possible_new_positions = shuffle_list(possible_new_positions)
        for new_position in possible_new_positions:
            if world._position_is_free(layer=1, position=new_position):
                world.layers[self.layer].pop(self.position)
                world.layers[self.layer][new_position] = self
                self.position = new_position    

    @staticmethod
    def generate_new_positions(old_position: Position, world) -> list[Position]:
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
                if (
                    new_position.x >= 0 
                    and new_position.y >= 0
                    and new_position.x < world.size 
                    and new_position.y < world.size
                ):
                    new_positions.append(new_position)
                    
        return new_positions
    

class Carnivore(Agent):
    type: AgentType = AgentType.CARNIVORE
    layer: int = 1
    color: Tuple[int, int, int] = (255, 0, 0)

    def act(self, world) -> None:
        self.move(world)

    # TODO: temporary the same as for herbivores        
    def move(self, world) -> None:
        possible_new_positions = self.generate_new_positions(
            old_position=self.position,
            world=world
        )
        possible_new_positions = shuffle_list(possible_new_positions)
        for new_position in possible_new_positions:
            if world._position_is_free(layer=1, position=new_position):
                world.layers[self.layer].pop(self.position)
                world.layers[self.layer][new_position] = self
                self.position = new_position  
              
    # TODO: temporary the same as for herbivores         
    @staticmethod
    def generate_new_positions(old_position: Position, world) -> list[Position]:
        """
        Generate n new positions
        """
        new_positions = []
        for i in [-3, 0, 3]:
            for y in [-3, 0, 3]:
                new_position = Position(
                    x=old_position.x + i,
                    y=old_position.y + y,
                )
                if (
                    new_position.x >= 0 
                    and new_position.y >= 0
                    and new_position.x < world.size 
                    and new_position.y < world.size
                ):
                    new_positions.append(new_position)
                    
        return new_positions
