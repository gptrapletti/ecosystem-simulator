# Ecosym: Ecosystem Simulator

### Next steps

- Agents initialization and adding to world.
- Think whether removing position attribute for agents, since they exist in the World at a given position, or don't exist at all.
- Use a new class as a adapter between world and agents? In modo che `entities.py` non import `World`. Ha senso che world import entities, dato che le conterra', ma entities meglio che rimangano agnostiche al mondo.
- Metodo `move` di Herbivor e' tutt'altro che agnostico al mondo!!!

### Roadmap

- Add energy-size mechanic.
- Add age/death (make color fading?).
- Add asexual reproduction for herbivores.
- Add carnivore, with basic eating mechanic (if adjacent).
- Add preying mechanic for carnivores (if it sees a herbivore near, goes for it).
- Add grass, with add asexual reproduction for grass.
- Add herbivor grazing.


### Dev

- Use argparsing to run program with something like `python main.py --herbivores 100 --carnivores 40`.


## WIP

- class Spawner
- takes world size
- takes agent types and number.
- inits N agents with random position, ensuring:
    - they are N
    - within world borders
    - unique position
- returns a list
- world object takes the list and adds agents to itself.