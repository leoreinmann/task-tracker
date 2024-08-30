import json
import os.path
import calendar
import time
import datetime


class Todo:
    def __init__(self):
        self.todo_filepath = "todos.json"

    def add_todo(self, args):
        description = args.description
        if not os.path.exists(self.todo_filepath):
            data = {
                "id_count": 1,
                "tasks": []
            }
            with open(self.todo_filepath, 'w') as f:
                json.dump(data, f)

        with open(self.todo_filepath, 'r') as f:
            data = json.load(f)

            # Timestamp
            time_tuple = time.gmtime()
            timestamp = calendar.timegm(time_tuple)
            datetime_object = datetime.datetime.fromtimestamp(timestamp)

            id_count = data['id_count']

            todo = {
                "id": id_count,
                "description": description,
                "status": "todo",
                "createdAt": datetime_object.__str__(),
                "updatedAt": datetime_object.__str__()
            }

            data['id_count'] = id_count + 1
            data['tasks'].append(todo)

            print(f"Task added successfully (ID:{id_count})")

        with open("todos.json", 'w') as f:
            json.dump(data, f, indent=4)

    def delete_todo(self, args):
        todo_id = args.todo_id

        data = self.load_file()

        data['tasks'] = [task for task in data['tasks'] if task['id'] != todo_id]

        self.dump_data(data)

    def update_todo(self, args):
        todo_id = args.todo_id
        description = args.description

        data = self.load_file()

        for task in data['tasks']:
            if task['id'] == todo_id:
                # Timestamp
                time_tuple = time.gmtime()
                timestamp = calendar.timegm(time_tuple)
                datetime_object = datetime.datetime.fromtimestamp(timestamp)

                task['description'] = description
                task['updatedAt'] = datetime_object.__str__()

        self.dump_data(data)

    def mark_todo(self, args):
        todo_id = args.todo_id
        choice = args.choice

        data = self.load_file()

        for task in data['tasks']:
            if task['id'] == todo_id:
                # Timestamp
                time_tuple = time.gmtime()
                timestamp = calendar.timegm(time_tuple)
                datetime_object = datetime.datetime.fromtimestamp(timestamp)

                task['status'] = choice
                task['updatedAt'] = datetime_object.__str__()

        self.dump_data(data)

    def list_todos(self, args):
        choice = args.choice

        data = self.load_file()

        for task in data["tasks"]:
            if task["status"] == choice:
                print(task)
            if choice is None:
                print(task)

    def load_file(self):
        if not os.path.exists(self.todo_filepath):
            raise FileNotFoundError("todos.json not found")
        with open(self.todo_filepath, 'r') as f:
            data = json.load(f)
        return data

    @staticmethod
    def dump_data(data):
        with open('todos.json', 'w') as f:
            json.dump(data, f, indent=4)
