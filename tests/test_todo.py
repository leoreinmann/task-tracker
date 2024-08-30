import pytest
from unittest.mock import patch, mock_open
import json
from datetime import datetime
from src.todo import Todo


class Args:
    def __init__(self, description=None, todo_id=None, choice=None):
        self.description = description
        self.todo_id = todo_id
        self.choice = choice


@pytest.fixture
def todo():
    return Todo()


def test_add_todo_new_file(todo):
    args = Args(description="Test Task")
    mock_data = {"id_count": 1, "tasks": []}

    with patch("os.path.exists", return_value=False), \
         patch("builtins.open", mock_open()) as mocked_file, \
         patch("json.dump") as mock_json_dump, \
         patch("json.load", return_value=mock_data), \
         patch("time.gmtime", return_value=(2024, 8, 30, 12, 0, 0, 4, 242, 0)), \
         patch("calendar.timegm", return_value=1693392000), \
         patch("datetime.datetime") as mock_datetime:

        mock_datetime.fromtimestamp.return_value = datetime(2024, 8, 30, 12, 0, 0)
        todo.add_todo(args)

        mocked_file.assert_called_with(todo.todo_filepath, 'w')
        mock_json_dump.assert_called()
        assert mock_json_dump.call_args[0][0]["id_count"] == 2  # id_count should have incremented


def test_add_todo_existing_file(todo):
    args = Args(description="Test Task")
    mock_data = {"id_count": 2, "tasks": []}

    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mocked_file, \
         patch("json.load", return_value=mock_data), \
         patch("json.dump") as mock_json_dump, \
         patch("time.gmtime", return_value=(2024, 8, 30, 12, 0, 0, 4, 242, 0)), \
         patch("calendar.timegm", return_value=1693392000), \
         patch("datetime.datetime") as mock_datetime:

        mock_datetime.fromtimestamp.return_value = datetime(2024, 8, 30, 12, 0, 0)
        todo.add_todo(args)

        mocked_file.assert_called_with(todo.todo_filepath, 'w')
        mock_json_dump.assert_called()
        assert mock_json_dump.call_args[0][0]["id_count"] == 3
        assert len(mock_json_dump.call_args[0][0]["tasks"]) == 1


def test_delete_todo_existing_task(todo):
    args = Args(todo_id=1)
    mock_data = {"id_count": 2, "tasks": [{"id": 1, "description": "Test Task", "status": "todo"}]}

    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mocked_file, \
         patch("json.load", return_value=mock_data), \
         patch("json.dump") as mock_json_dump:

        todo.delete_todo(args)

        mocked_file.assert_called_with(todo.todo_filepath, 'w')
        mock_json_dump.assert_called()
        assert len(mock_json_dump.call_args[0][0]["tasks"]) == 0


def test_update_todo_existing_task(todo):
    args = Args(todo_id=1, description="Updated Task")
    mock_data = {"id_count": 2, "tasks": [{"id": 1, "description": "Test Task", "status": "todo"}]}

    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mocked_file, \
         patch("json.load", return_value=mock_data), \
         patch("json.dump") as mock_json_dump, \
         patch("time.gmtime", return_value=(2024, 8, 30, 12, 0, 0, 4, 242, 0)), \
         patch("calendar.timegm", return_value=1693392000), \
         patch("datetime.datetime") as mock_datetime:

        mock_datetime.fromtimestamp.return_value = datetime(2024, 8, 30, 12, 0, 0)
        todo.update_todo(args)

        mocked_file.assert_called_with(todo.todo_filepath, 'w')
        mock_json_dump.assert_called()
        assert mock_json_dump.call_args[0][0]["tasks"][0]["description"] == "Updated Task"


def test_mark_todo_existing_task(todo):
    args = Args(todo_id=1, choice="done")
    mock_data = {"id_count": 2, "tasks": [{"id": 1, "description": "Test Task", "status": "todo"}]}

    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mocked_file, \
         patch("json.load", return_value=mock_data), \
         patch("json.dump") as mock_json_dump, \
         patch("time.gmtime", return_value=(2024, 8, 30, 12, 0, 0, 4, 242, 0)), \
         patch("calendar.timegm", return_value=1693392000), \
         patch("datetime.datetime") as mock_datetime:

        mock_datetime.fromtimestamp.return_value = datetime(2024, 8, 30, 12, 0, 0)
        todo.mark_todo(args)

        mocked_file.assert_called_with(todo.todo_filepath, 'w')
        mock_json_dump.assert_called()
        assert mock_json_dump.call_args[0][0]["tasks"][0]["status"] == "done"


def test_list_todos(todo):
    args = Args(choice=None)
    mock_data = {
        "id_count": 2,
        "tasks": [
            {"id": 1, "description": "Task 1", "status": "todo"},
            {"id": 2, "description": "Task 2", "status": "done"},
        ],
    }

    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mocked_file, \
         patch("json.load", return_value=mock_data), \
         patch("builtins.print") as mock_print:

        todo.list_todos(args)

        mocked_file.assert_called_with(todo.todo_filepath, 'r')
        assert mock_print.call_count == 2


def test_load_file_not_found(todo):
    with patch("os.path.exists", return_value=False), \
         pytest.raises(FileNotFoundError):

        todo.load_file()


def test_load_file_success(todo):
    mock_data = {"id_count": 2, "tasks": [{"id": 1, "description": "Test Task", "status": "todo"}]}

    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mocked_file:

        result = todo.load_file()

        mocked_file.assert_called_with(todo.todo_filepath, 'r')
        assert result == mock_data


def test_dump_data(todo):
    data = {"id_count": 2, "tasks": [{"id": 1, "description": "Test Task", "status": "todo"}]}

    with patch("builtins.open", mock_open()) as mocked_file, \
         patch("json.dump") as mock_json_dump:

        todo.dump_data(data)

        mocked_file.assert_called_with(todo.todo_filepath, 'w')
        mock_json_dump.assert_called_with(data, mocked_file(), indent=4)
