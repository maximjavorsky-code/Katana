import hashlib

# -----------------------------
# HEX generator
# -----------------------------
def name_to_hex(name: str) -> str:
    h = hashlib.md5(name.encode()).hexdigest()
    return "#" + h[:6]

# -----------------------------
# lighten / darken
# -----------------------------
def clamp(x):
    return max(0, min(255, int(x)))

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def lighten(hex_color, amount=30):
    r, g, b = hex_to_rgb(hex_color)
    return rgb_to_hex((clamp(r + amount), clamp(g + amount), clamp(b + amount)))

def darken(hex_color, amount=30):
    r, g, b = hex_to_rgb(hex_color)
    return rgb_to_hex((clamp(r - amount), clamp(g - amount), clamp(b - amount)))

# -----------------------------
# FULL COLOR DATA
# -----------------------------
colors_raw = """
RED
Crimson
Scarlet
Ruby
Cherry
Firebrick
Blood red
Cardinal red
Carmine
Burgundy
Maroon
Wine red
Brick red
Rose red
Candy apple red
Ferrari red
Indian red
Salmon red
Coral red
Tomato red
Dark red
Light red
Soft red
Deep red
Bright red
Neon red
Vermilion
Rust red
Mahogany
Mulberry
Berry red
Raspberry red
Strawberry red
Poppy red
Apple red
Claret
Sangria
Oxblood
Garnet
Oxide red
Terra cotta red
Blush red
Hot red
Pure red
Signal red
Traffic red
Lipstick red
Rosewood red
Persian red
Alizarin crimson
Venetian red
English red
Spanish red
Chinese red
Oxide crimson
BLUE
Azure
Baby blue
Sky blue
Light blue
Deep blue
Dark blue
Royal blue
Navy blue
Midnight blue
Ocean blue
Sea blue
Teal blue
Turquoise blue
Cyan blue
Electric blue
Neon blue
Ice blue
Steel blue
Powder blue
Cornflower blue
Periwinkle
Denim blue
Indigo
Ultramarine
Sapphire blue
Cobalt blue
Prussian blue
Egyptian blue
French blue
Persian blue
Majorelle blue
Yale blue
Oxford blue
Dodger blue
Capri blue
Cerulean
Robin egg blue
Bondi blue
Arctic blue
Glacier blue
Fog blue
Smoke blue
Slate blue
Blue-gray
Blue steel
Steel teal
Storm blue
Ink blue
Marine blue
Deep sea blue
Atlantic blue
Pacific blue
Lagoon blue
Carolina blue
Maya blue
Vivid blue
Bright blue
Pastel blue
Soft blue
Muted blue
Dusty blue
YELLOW
Yellow
Light yellow
Pale yellow
Dark yellow
Golden yellow
Gold
Amber
Mustard
Lemon yellow
Canary yellow
Sunflower yellow
Banana yellow
Butter yellow
Cream yellow
Ivory yellow
Honey yellow
Daffodil yellow
Flaxen yellow
Straw yellow
Wheat yellow
Maize yellow
Corn yellow
Saffron
Marigold
Amber yellow
Ochre yellow
Sand yellow
Beige yellow
Champagne yellow
Vanilla yellow
Lime yellow
Chartreuse yellow
Neon yellow
Electric yellow
Fluorescent yellow
Highlighter yellow
Taxi yellow
School bus yellow
Acid yellow
Brass yellow
Old gold
Antique gold
Burnished gold
Rich yellow
Warm yellow
Cool yellow
Muted yellow
Pastel yellow
Soft yellow
Bright yellow
Deep yellow
Goldenrod
Dandelion yellow
Sunshine yellow
GREEN
Green
Light green
Dark green
Deep green
Forest green
Emerald green
Jade green
Mint green
Lime green
Neon green
Electric green
Fluorescent green
Olive green
Army green
Moss green
Fern green
Pine green
Bottle green
Hunter green
Swamp green
Jungle green
Grass green
Meadow green
Leaf green
Spring green
Sea green
Aquamarine green
Teal green
Blue-green
Chartreuse green
Apple green
Pear green
Avocado green
Pistachio green
Matcha green
Sage green
Celadon green
Khaki green
Camo green
Military green
Malachite green
Viridian
Shamrock green
Irish green
Kelly green
Olive drab
Amazon green
Tropical green
Deep forest green
Night green
Soft green
Pastel green
Muted green
Bright green
PURPLE
Purple
Light purple
Dark purple
Deep purple
Violet
Lavender
Lilac
Mauve
Plum
Eggplant
Amethyst
Orchid
Heliotrope
Magenta
Fuchsia
Neon purple
Electric purple
Royal purple
Byzantium
Grape purple
Berry purple
Indigo purple
Ultraviolet
Cosmic purple
Midnight purple
Shadow purple
Twilight purple
Mystic purple
Candy purple
BLACK
Black
Jet black
Charcoal
Graphite black
Ash black
Smoke black
Ink black
Midnight black
Pure black
Matte black
Carbon black
Obsidian
Space black
WHITE
White
Pure white
Snow white
Ivory
Cream
Off-white
Soft white
Pearl white
Arctic white
Milk white
Porcelain white
Ghost white
GRAY
Gray
Light gray
Dark gray
Steel gray
Silver gray
Charcoal gray
Slate gray
Concrete gray
Fog gray
Cloud gray
Storm gray
Black gray
ORANGE
Orange
Light orange
Dark orange
Burnt orange
Tangerine
Apricot
Peach
Amber
Pumpkin
Carrot orange
Neon orange
Sunset orange
PINK
Pink
Light pink
Hot pink
Neon pink
Rose pink
Baby pink
Bubblegum pink
Fuchsia pink
Dusty pink
Rose quartz
WHITE
White
"""

# -----------------------------
# BUILD PALETTE
# -----------------------------
palette = {}
current_group = None

for line in colors_raw.splitlines():
    line = line.strip()
    if not line:
        continue

    if line.isupper() and len(line.split()) == 1:
        current_group = line
        continue

    full_name = f"{current_group} - {line}"
    hex_code = name_to_hex(full_name)

    palette[full_name.lower()] = hex_code

# -----------------------------
# SEARCH
# -----------------------------
def search_color(query: str):
    query = query.lower()
    results = []

    for name, hex_code in palette.items():
        if query in name:
            results.append((name, hex_code))

    if not results:
        print("Nenalezeno")
        return

    for name, hex_code in results:
        print(f"{name:40} {hex_code} | +{lighten(hex_code)} | -{darken(hex_code)}")

# -----------------------------
# RUN
# -----------------------------
while True:
    q = input("\nHledat barvu (exit = konec): ")
    if q.lower() == "exit":
        break
    search_color(q)