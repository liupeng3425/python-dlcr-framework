from pathlib import Path


def path_to_package(path):
    path = Path(path).as_posix()
    path = path.replace('/', '.')
    if path.endswith('.py'):
        path = path.replace('.py', '')
    return path