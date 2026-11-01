import sqlite3


def get_connection():
    conn = sqlite3.connect("game.db")
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

        # 1. Rooms / Scenes
        scenes = [
            ("The Entrance Hall", "The heavy oak door slams shut behind you. The floorboards groan beneath your feet.", 0,
            ),
            ( "The Dusty Library", "Towering shelves filled with rotting grimoires. A draft makes the chandelier sway.", 0,
            ),
            ( "The Frozen Attic", "Complete darkness and biting cold. Shadows seem to twist just out of sight.", -10,
            ),
        ]
        cursor.executemany(
            "INSERT INTO scenes (title, description, sanity_impact) VALUES (?, ?, ?)",
            scenes,
        )

        # 2. Choices for each scene
        choices = [
            # (scene_id, choice_text, target_scene_id)
            (1, "Proceed into the Library", 2),
            (1, "Climb the creaking stairs to the Attic", 3),
            (2, "Return to the Entrance Hall", 1),
            (3, "Rush back down to the Entrance Hall", 1),
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
