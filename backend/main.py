from fastapi import FastAPI, HTTPException
from backend.database import get_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="The Haunted Escape API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "The Haunted House API is running..."}

@app.get("/api/scenes/{scene_id}")
def get_scene(scene_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scenes WHERE id = ?", (scene_id,))
    scene = cursor.fetchone()

    if not scene:
        conn.close()
        raise HTTPException(status_code=404, detail="Scene not found")

    cursor.execute("SELECT * FROM choices WHERE scene_id = ?", (scene_id,))
    choices = cursor.fetchall()
    conn.close()

    scene_data = dict(scene)
    scene_data["choices"] = [dict(c) for c in choices]

    return scene_data
