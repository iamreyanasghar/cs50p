from tabulate import tabulate

tasks = []


def add():
    do = input("Add new task: ").title()
    tasks.append(do)
    return f"Added: {do}"


def view():
    if not tasks:
        return "No tasks available. Add some tasks first!"

    table = tabulate(
        enumerate(tasks, start=1),
        tablefmt="plain"
    )

    return table


def remove():
    if not tasks:
        return "No tasks to remove!"

    r = input("What to remove? [By index / name] ").strip()

    if r.isdigit():
        idx = int(r) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            return f"Removed: {removed}"
        else:
            return f"Invalid index! Use 1-{len(tasks)}"

    if r in tasks:
        n = tasks.index(r)
        del tasks[n]
        return f"Removed: {r}"

    else:
        return "Please select or enter the appropriate task for removal."

