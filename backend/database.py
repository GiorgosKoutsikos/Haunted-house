from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parent / "game.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS scenes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    sanity_impact INTEGER DEFAULT 0
                  )
                """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS choices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    scene_id INTEGER NOT NULL,
                    choice_text NOT NULL,
                    target_scene_id INTEGER NOT NULL,
                    FOREIGN KEY (scene_id) REFERENCES scenes(id),
                    FOREIGN KEY (target_scene_id) REFERENCES scenes (id)
                  )
                """)

    conn.commit()
    conn.close()

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM scenes")
    count = cursor.fetchone()[0]
    if count == 0:

        # 1.Rooms / Scenes
        scenes = [
            (1, "The Entrance Hall", "The heavy oak door is locked tight. Dust particles float in pale moonlight, while three corridors stretch into darkness.", 0),
            (2, "The Grand Library", "Towering shelves hold cursed tomes. Whispers echo through the tall rows of books.", -10),
            (3, "The Dining Hall", "A long banquet table set with silver plates covered in cobwebs. A cold breeze blows from the terrace.", -5),
            (4, "The Damp Basement", "Stagnant water reaches your knees. Distant chains clatter deeper in the subterranean vault.", -25),
            (5, "The Secret Study", "A warm lantern still burns softly. Old maps cover the mahogany desk, offering a moment of calm.", 15),
            (6, "The Sunken Conservatory", "Shattered glass ceilings expose dark clouds. Tangled, thorny vines grip the cracked marble statues.", -10),
            (7, "The Wine Cellar", "Rows of shattered barrels line the room. Behind an iron grate, you notice a low maintenance tunnel.", -15),
            (8, "The Ritual Chamber", "Runes blaze with violet fire. Horrors from beyond tear into your thoughts. Madness consumes you.", -100),
            (9, "The Collapsed Tunnel", "You crawl into the narrow opening, but the ceiling gives way under immense weight. You are trapped forever.", -100),
            (10, "The Garden of Dawn", "You push through the rusted outer gate and step onto fresh grass. Morning light breaks on the horizon. You escaped alive!", 0)
        ]

        cursor.executemany(
            "INSERT INTO scenes (id, title, description, sanity_impact) VALUES (?, ?, ?, ?)",
            scenes,
        )

        # 2.Choices for each scene
        choices = [
            #Choices from Scene 1: Entrance Hall
            (1, "Search the archives in the Grand Library", 2),
            (1, "Walk towards the Dining Hall", 3),
            (1, "Descend into the dark Basement", 4),

            #Choices from Scene 2: Grand Library
            (2, "Inspect the carved bookshelf for a hidden mechanism", 5),
            (2, "Follow the narrow side door towards the Conservatory", 6),
            (2, "Return to the Entrance Hall", 1),

            #Choices from Scene 3: Dining Hall
            (3, "Head out through the French doors into the Conservatory", 6),
            (3, "Open the service hatch leading down to the Wine Cellar", 7),
            (3, "Walk back into the Entrance Hall", 1),

            #Choices from Scene 4: Damp Basement
            (4, "Wade toward the iron gate leading to the Wine Cellar", 7),
            (4, "Step toward the glowing purple archway", 8),
            (4, "Climb the stairs back to the Entrance Hall", 1),

            #Choices from Scene 5: Secret Study (Safe spot)
            (5, "Unlock the heavy iron trapdoor with the brass key", 10),
            (5, "Inspect the ventilation shaft behind the tapestry", 9),
            (5, "Walk back into the Library", 2),

            #Choices from Scene 6: Conservatory
            (6, "Climb over the cracked stone balcony toward freedom", 10),
            (6, "Investigate the dark root-covered opening in the floor", 8),
            (6, "Retreat back to the Dining Hall", 3),

            #Choices from Scene 7: Wine Cellar
            (7, "Squeeze through the narrow maintenance duct", 9),
            (7, "Pry open the wooden cellar door leading upward", 5),
            (7, "Retreat toward the wet basement stairs", 4)

            #Scenes 8, 9, 10 have no choices (terminal / end-game rooms)
]
        cursor.executemany(
            "INSERT INTO choices (scene_id, choice_text, target_scene_id) VALUES (?, ?, ?)",
            choices,
        )

    conn.commit()
    conn.close()



if __name__ == "__main__":
    init_db()
    seed_data()
