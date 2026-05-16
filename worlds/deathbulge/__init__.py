from BaseClasses import Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, CollectionState, WebWorld
from .items import (
    DeathbulgeItem,
    all_treasure_items,
    base_id,
    treasure_stocks_items,
    treasure_legendary_beats_items,
    treasure_patches_items,
    treasure_merch_items,
    treasure_mod_items,
    treasure_old_prize_draw_ticket_items,
    treasure_progression_items,
    real_fillers_items,
)
from .locations import (
    regions_to_locations,
    dream_locations,
    bopstead_locations,
    tonewood_locations,
    claire_hair_locations,
    basement_locations,
    the_bus_locations,
    hoho_locations,
    lab_locations,
    pokalyps_locations,
    claire_lower_locations,
)
from .regions import deathbulge_regions_all
from .options import DeathbulgeOptions


class DeathbulgeWeb(WebWorld):
    theme = "jungle"

    bug_report_page = "https://github.com/neverhelios/DeathbulgeArchipelago/issues"

    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up Deathbulge for Archipelago. "
            "This guide covers single-player, multiworld, and related software.",
            "English",
            "setup_en.md",
            "setup/en",
            ["NeverHeliOS"],
        )
    ]


class DeathbulgeWorld(World):
    """
    The party-based RPG where you kick down doors and fight with music as a 3-piece band of idiots.
    You play as Faye, Ian and Briff, a 3-piece band of dysfunctional friends who unknowingly stumble into a cursed battle of the bands contest,
    where all entrants can attack with music and must fight to the death.
    """

    game = "Deathbulge"
    options_dataclass = DeathbulgeOptions  # options the player can set
    options: DeathbulgeOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler

    # The following two dicts are required for the generation to know which items exist.
    # They can be generated with arbitrary code during world load, but keep in mind that
    # anything expensive (e.g. parsing non-python data files) will delay world loading.
    # They can include events, but don't have to since events will be placed manually.

    all_items = all_treasure_items
    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}

    all_locations = (
        dream_locations
        + bopstead_locations
        + tonewood_locations
        + claire_hair_locations
        + basement_locations
        + the_bus_locations
        + hoho_locations
        + lab_locations
        + pokalyps_locations
        + claire_lower_locations
    )

    location_name_to_id = {name: id for id, name in enumerate(all_locations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        # TODO: Add shop stocks
        "stocks": {item["name"] for item in treasure_stocks_items + []},
        # TODO: Add last legendary beat
        "legendary_beats": {item["name"] for item in treasure_legendary_beats_items + []},
        # TODO: Add shop patches
        "patches": {item["name"] for item in treasure_patches_items + []},
        # TODO: Add shop merch
        "merch": {item["name"] for item in treasure_merch_items + []},
        # TODO: Add shop mods
        "mods": {item["name"] for item in treasure_mod_items + []},
        "old_prize_draw_tickets": {item["name"] for item in treasure_old_prize_draw_ticket_items},
        "key_progression_merch": {item["name"] for item in treasure_progression_items},
    }

    def get_filler_item_name(self) -> str:
        return self.random.choice(real_fillers_items)["name"]

    def create_item(self, name: str) -> DeathbulgeItem:
        item_id = self.item_name_to_id[name]
        item_data = self.all_items[item_id - base_id]
        return DeathbulgeItem(name, item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        nb_items_added = 0
        useful_items = self.all_items.copy()

        useful_items = [item for item in useful_items if item["classification"] != ItemClassification.filler]

        for item in useful_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)
                nb_items_added += 1

        filler_count = len(self.all_locations)
        filler_count -= nb_items_added

        for i in range(filler_count):
            index = i % len(real_fillers_items)
            filler_item = real_fillers_items[index]
            new_item = self.create_item(filler_item["name"])
            self.multiworld.itempool.append(new_item)

    def create_regions(self) -> None:
        used_regions = deathbulge_regions_all
        for region_name in used_regions.keys():
            self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))

        for region_name, region_connections in used_regions.items():
            region = self.get_region(region_name)
            region.add_exits(region_connections)
            region.add_locations(
                {location: self.location_name_to_id[location] for location in regions_to_locations[region_name]}
            )
