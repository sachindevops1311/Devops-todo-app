from flask import jsonify, request
from app.todo_service import get_all_todos, create_todo, update_todo, delete_todo
from app.cache import get_redis_connection
import json
import os

def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to devops-todo-app"})

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy", "message": "App is running"})

    @app.route("/todos", methods=["GET"])
    def get_todos():
        r = get_redis_connection()
        cached = r.get("todos")
        if cached:
            return jsonify({"todos": json.loads(cached), "source": "cache"})
        todos = get_all_todos()
        r.setex("todos", 60, json.dumps(todos))
        return jsonify({"todos": todos, "source": "database"})

    @app.route("/todos", methods=["POST"])
    def add_todo():
        data = request.get_json()
        todo = create_todo(data["task"])
        r = get_redis_connection()
        r.delete("todos")
        return jsonify(todo), 201

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Route not found", "status": 404}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error", "status": 500}), 500
