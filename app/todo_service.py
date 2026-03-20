from app.database import get_db_connection

def create_todo(task):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO todos (task, done) VALUES (%s, %s) RETURNING id, task, done",
        (task, False)
    )
    todo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"id": todo[0], "task": todo[1], "done": todo[2]}

def get_all_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, task, done FROM todos")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "task": r[1], "done": r[2]} for r in rows]

def update_todo(id, done):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE todos SET done = %s WHERE id = %s RETURNING id, task, done",
        (done, id)
    )
    todo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"id": todo[0], "task": todo[1], "done": todo[2]} if todo else None

def delete_todo(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s RETURNING id", (id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return deleted is not None
