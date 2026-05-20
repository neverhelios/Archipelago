from BaseClasses import ItemClassification
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .subclasses import ItemDict

base_id = 50173000

useful_skip_balancing: ItemClassification = ItemClassification(
    ItemClassification.useful + ItemClassification.skip_balancing
)
useful_progression: ItemClassification = ItemClassification(ItemClassification.progression + ItemClassification.useful)

# Todo: Add beats


# TODO: Progressive / Countable ?
treasure_stocks_items: List["ItemDict"] = [
    {"name": "[Stock] Increase 1 (Tonewood01Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Tonewood06Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Claire06Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Claire07Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Claire05Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (ClaireLower02Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (ClaireLower04Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Basement03Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Basement06Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Basement03Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Basement02Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (TheBus05Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (TheBus08Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (TheBus08Treasure03)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Lab01Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Lab04Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Lab07Treasure02)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Pokalyps01Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Pokalyps07Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Dream04Treasure01)", "count": 1, "classification": useful_skip_balancing},
    {"name": "[Stock] Increase 1 (Dream04Treasure03)", "count": 1, "classification": useful_skip_balancing},
]


treasure_legendary_beats_items: List["ItemDict"] = [
    {"name": "[Beat] Bansheebash", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Beat] Absolute Belter", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Beat] Cuttlebuddy", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Beat] Makeshift Beat", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Beat] Starstrike", "count": 1, "classification": ItemClassification.progression},
]


treasure_patches_items: List["ItemDict"] = [
    {"name": "[Patch] God Brain", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] HELF", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Fat Punch Five", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Beauty in Suffering", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Luminous Kid", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Jen & The Regens", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] DJ Beatseek", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Barry Club", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] BotB Patch", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Mega Def", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Chuckridge Cuttlebrander", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] The NOW NOW NOWs", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] WELF", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] U WANT SUM", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Purple Lightning", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] THREE BEAT MIX PATCH", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Recently Hatched", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Pokalyps", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Patch] Savant", "count": 1, "classification": ItemClassification.useful},
]


treasure_merch_items: List["ItemDict"] = [
    {"name": "[Merch] Emergency Horn", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] Clearbuds", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] Flipped Cap", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] Silenceblaster", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] The Y'almighty", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] Diva Music Box", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] Audio Greeting Card", "count": 1, "classification": ItemClassification.useful},
]


treasure_mod_items: List["ItemDict"] = [
    {"name": "[Mod] Beefcake Bassquake", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Crowdsurf", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Reckless Shredding", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Heartwarmer", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Intimidate", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] The Great Unjoying", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Fresh Twist", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Everybody Broken Bones", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Erasure", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] GONG", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Zero Hertz", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Beefy Double", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Heart Kickstart", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Crashy Crescendo", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Bloody Hell", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Whale Music", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Upbeat", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Dazzling Shred", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Let Me Try Something", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Big Angry Riff of Fury", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Weaver of Darkness", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Surging Sorrow", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Shred of the Dead", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Good Vibe Preservation", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Power Slide", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Osculate in 7/8", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Robin Hunk Special", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Pyrotechnics", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] ugh", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] REMIX Briff", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Beam Team", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Axe of Righteousness", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Hypercussion", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] ALT_FX", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Palm Destroyer", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Colossal Cuss Out", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Vicious Sacrifice", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] BOOM.WAV", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] The Power of Friendship", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Graveyard Shuffle", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Dr. Tonebone", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Eruptive Damnation", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Mod] Total Reinterpretation", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Merch] SIDD X-TR3M3", "count": 1, "classification": ItemClassification.useful},
]


# TODO: Progressive / Countable ?
treasure_old_prize_draw_ticket_items: List["ItemDict"] = [
    {"name": "[Key Merch] Old Prize Draw Ticket 1", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 2", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 3", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 4", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 5", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 6", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 7", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 8", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 9", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Old Prize Draw Ticket 10", "count": 1, "classification": ItemClassification.progression},
]

treasure_progression_items: List["ItemDict"] = [
    {"name": "[Key Merch] Your Inner Boot", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] 16th Deck Keycard", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] 13th Deck Keycard", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] 14th Deck Keycard", "count": 1, "classification": ItemClassification.progression},
    {"name": "[Key Merch] Class Changer", "count": 1, "classification": useful_progression},
]

real_fillers_items: List["ItemDict"] = [
    {"name": "Treasure Money", "count": 12, "classification": ItemClassification.filler},
]

treasure_misc_items: List["ItemDict"] = [
    {"name": "[Key Merch] Shiny Spiky Thing", "count": 1, "classification": ItemClassification.filler},
    {"name": "[Key Merch] Shiny Spiky Thing (Fork)", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Key Merch] Barry's Tea Party", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Key Merch] Glam Reader", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Beat] Rinna", "count": 1, "classification": ItemClassification.useful},
    {"name": "[Beat] RH", "count": 1, "classification": ItemClassification.useful},
] + real_fillers_items


all_treasure_items: List["ItemDict"] = (
    treasure_stocks_items
    + treasure_legendary_beats_items
    + treasure_patches_items
    + treasure_merch_items
    + treasure_mod_items
    + treasure_old_prize_draw_ticket_items
    + treasure_progression_items
    + treasure_misc_items
)

boss_lock_items: List["ItemDict"] = [
    {"name": "Basement Key", "count": 1, "classification": ItemClassification.progression},  # Beat KKwak
    {"name": "Babby's corpse", "count": 1, "classification": ItemClassification.progression},  # Beat Babby
    {"name": "Bus ticket", "count": 1, "classification": ItemClassification.progression},  # Beat Platinium Scrumptious
    {"name": "Pokalyps concert's invite", "count": 1, "classification": ItemClassification.progression},  # Beat Mutilla
    {"name": "Claire's comb", "count": 1, "classification": ItemClassification.progression},  # Beat Pokalyps
]


all_items: List["ItemDict"] = all_treasure_items
# Currently out of the global pool, but I will allow the items to be in the pool
# + boss_lock_items
