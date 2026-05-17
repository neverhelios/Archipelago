from . import DeathbulgeWorld

from typing import Dict, Callable
from BaseClasses import CollectionState


class DeathbulgeRules:
    player: int
    world: DeathbulgeWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    # def __init__(self, world: DeathbulgeWorld) -> None:
    #     self.player = world.player
    #     self.world = world

    #     self.region_rules = {
    #         "Act 2": self.has_act2_requirements,
    #         "Act 3": self.has_act3_requirements,
    #         "Epilogue": self.has_epilogue_requirements,
    #     }
