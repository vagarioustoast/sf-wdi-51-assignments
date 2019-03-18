from app import db, marshmallow
from flask import jsonify


class Todo(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    completed = db.Column(db.Boolean())

    def __init__(self, body, completed):
        self.body = body
        self.completed = completed

    # Get all todos
    @classmethod
    def get_todos(cls):
        todos = Todo.query.all()
        return todos_schema.jsonify(todos)

    # Create a todo
    @classmethod
    def create_todo(cls, body, completed):
        new_todo = Todo(body, completed)
        try:
            db.session.add(new_todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return todo_schema.jsonify(new_todo)

    # Delete a todo
    @classmethod
    def delete_todo(cls, todo_id):
        todo = Todo.query.get(todo_id)
        try:
            db.session.remove(todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return 'Todo deleted'


class TodoSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'body', 'completed')


# Init Schema
todo_schema = TodoSchema(strict=True)
todos_schema = TodoSchema(many=True, strict=True)


if __name__ == 'models':
    db.create_all()
