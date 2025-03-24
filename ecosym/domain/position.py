from pydantic import BaseModel


class Position(BaseModel, frozen=True):
    x: int | None = None
    y: int | None = None
    
    def __repr__(self):
        return f"(x={self.x}, y={self.y})"