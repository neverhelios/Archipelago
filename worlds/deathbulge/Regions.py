from typing import Dict, List, TYPE_CHECKING

from .locations import regions_to_locations

if TYPE_CHECKING:
    from . import DeathbulgeWorld

from BaseClasses import Region


class DeathbugeRegion(Region):
    parent: str | None

    def __init__(self, name: str, world: "DeathbulgeWorld", parent: str | None = None) -> None:
        super().__init__(name, world.player, world.multiworld)
        self.parent = parent
        locations = []
        if parent in regions_to_locations:
            subregions_to_locations = regions_to_locations[parent]
            region_name = name.removeprefix(f"{parent} - ")
            if region_name in subregions_to_locations:
                locations = [location for location in subregions_to_locations[region_name]]
        loc_dict = {location: world.location_name_to_id.get(location, None) for location in locations}
        self.add_locations(loc_dict)

        print(f"Add region {name} ( {len(locations)} Locations)")
        self.multiworld.regions.append(self)


all_regions: dict[str, list[str]] = {
    "Dream": [
        "Intro01",
        "Dream02",
        "Dream03",
        "Dream04",
        "Dream05",
        "Dream06",
        "DreamUbers",
    ],
    "Bopstead": [
        "Bopstead01",
        "Bopstead02",
        "Bopstead03",
        "Bopstead04",
        "Bopstead05",
    ],
    "Tonewood": [
        "Tonewood01",
        "Tonewood02",
        "Tonewood03",
        "Tonewood04",
        "Tonewood05",
        "Tonewood06",
        "Tonewood07",
        "Tonewood07-01",
        "Tonewood07-02",
        "Tonewood07-03",
        "Tonewood07-04",
        "Tonewood07-05",
        "Tonewood08",
    ],
    "ClaireHair": [
        "ClaireHair01",
        "ClaireHair02",
        "ClaireHair03",
        "ClaireHair04Lower",
        "ClaireHair04Upper",
        "ClaireHair05",
        "ClaireHair06",
        "ClaireHair07",
        "ClaireHair08",
    ],
    "Basement": [
        "Basement01",
        "Basement02",
        "Basement03",
        "Basement04",
        "Basement05",
        "Basement06",
        "Basement07",
        "BasementEndingStudio",
    ],
    "TheBus": [
        "TheBus01",
        "TheBus02",
        "TheBus03",
        "TheBus04",
        "TheBus05",
        "TheBus06",
        "TheBus07",
        "TheBus08",
        "TheBus09",
        "TheBus10",
        "TheBus11",
        "TheBusElevator",
    ],
    "Hoho": [
        "Hoho01Lower",
        "Hoho01Observatory",
        "Hoho01-Bus",
        "Hoho02",
    ],
    "Lab": [
        "Lab01",
        "Lab02",
        "Lab03",
        "Lab04",
        "Lab05",
        "Lab06",
        "Lab07",
        "Lab08",
        "Lab09",
        "Lab10",
        "Lab11",
        "Lab12",
    ],
    "Pokalyps": [
        "Pokalyps01",
        "Pokalyps02Lower",
        "Pokalyps02Upper",
        "Pokalyps03",
        "Pokalyps04Middle",
        "Pokalyps04Lower",
        "Pokalyps04Upper",
        "Pokalyps04EvenUpper",
        "Pokalyps05",
        "Pokalyps06",
        "Pokalyps07",
        "Pokalyps08",
        "Pokalyps09",
        "Pokalyps10",
        "Pokalyps11",
    ],
    "ClaireLower": [
        "ClaireLower01",
        "ClaireLower02",
        "ClaireLower03",
        "ClaireLower04",
        "TobbyCabin",
    ],
    "BattleOfTheBands": [
        "BOTBLobby",
    ],
}
