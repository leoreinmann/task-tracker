import argparse
from src import todo


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    todo_list = todo.Todo()

    parser_add = subparsers.add_parser("add", help="Add a todo to the todo list")
    parser_add.add_argument('description', type=str)
    parser_add.set_defaults(func=todo_list.add_todo)

    parser_update = subparsers.add_parser("update", help="Update a todo in the todo list")
    parser_update.add_argument('todo_id', type=int)
    parser_update.add_argument("description", type=str)
    parser_update.set_defaults(func=todo_list.update_todo)

    parser_delete = subparsers.add_parser("delete", help="Delete a todo from the todo list")
    parser_delete.add_argument('todo_id', type=int)
    parser_delete.set_defaults(func=todo_list.delete_todo)

    parser_mark = subparsers.add_parser("mark", help="Mark task in the todo list")
    parser_mark.add_argument('todo_id', type=int)
    parser_mark.add_argument("choice", choices=["done", "in-progress"])
    parser_mark.set_defaults(func=todo_list.mark_todo)

    parser_list = subparsers.add_parser("list", help="List tasks in the todo list")
    parser_list.add_argument("choice", type=str, choices=["done", "todo", "in-progress"], nargs='?')
    parser_list.set_defaults(func=todo_list.list_todos)

    args = parser.parse_args()

    args.func(args)


if __name__ == '__main__':
    main()
