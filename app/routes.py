from flask import jsonify

def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to devops-todo-app"})

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy", "message": "App is running"})

    @app.route("/todos")
    def get_todos():
        todos = [
            {"id": 1, "task": "Learn Docker", "done": False},
            {"id": 2, "task": "Learn Ansible", "done": False},
            {"id": 3, "task": "Learn Terraform", "done": False},
        ]
        return jsonify({"todos": todos, "count": len(todos)})

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Route not found", "status": 404}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error", "status": 500}), 500
