from flask import Flask, jsonify, request
from storage import TaskStore
from validators import validate_task_title

app = Flask(__name__)
store = TaskStore()


@app.get("/")
def index():
    return jsonify({
        "application": "SecureTask API",
        "message": "API sederhana untuk mengelola daftar tugas",
        "endpoints": ["/tasks"]
    })


@app.get("/tasks")
def list_tasks():
    return jsonify({"tasks": store.list_tasks()})


@app.post("/tasks")
def create_task():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Body JSON wajib berupa object"}), 400

    title = payload.get("title")
    error = validate_task_title(title)
    if error:
        return jsonify({"error": error}), 400

    task = store.add_task(title.strip())
    return jsonify({"task": task}), 201


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    if not store.delete_task(task_id):
        return jsonify({"error": "Tugas tidak ditemukan"}), 404
    return jsonify({"message": "Tugas berhasil dihapus"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
