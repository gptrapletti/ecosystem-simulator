from collections import defaultdict
import random

from ecosym.domain.position import Position
from ecosym.utils import shuffle_list


WORLD_SIZE = 100


class World:
    def __init__(self):
        self.size = WORLD_SIZE
        self.layers = {
            0: defaultdict(lambda: None),
            1: defaultdict(lambda: None),
        }
        
    def next_epoch(self) -> None:
        for layer_num, layer_dict in self.layers.items():
            entities = list(layer_dict.values())
            shuffle_list(entities)
            
            for entity in entities:
                entity.act(world=self)
        
        
    def add(self, entity, layer: int, position: Position) -> None:
        """
        Add entity to world.
        """
        if position.x >= self.size or position.y >= self.size:
            raise ValueError("Position coordinates beyond world ends.")
        
        if not self._position_is_free(layer=layer, position=position):
            raise ValueError("Position already occupied.")
        
        self.layers[layer][position] = entity

    
    def _position_is_free(self, layer: int, position: Position) -> bool:
        return False if self.layers[layer].get(position) else True