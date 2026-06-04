from pathlib import Path

exclude = {
    '.venv',
    'venv',
    '__pycache__',
    '.git',
    'node_modules'
}

with open("structure.txt", "w", encoding="utf-8") as f:

    def tree(path, prefix=''):
        items = [
            p for p in sorted(path.iterdir())
            if p.name not in exclude
        ]

        for i, item in enumerate(items):
            connector = "├── " if i < len(items)-1 else "└── "
            f.write(prefix + connector + item.name + "\n")

            if item.is_dir():
                extension = "│   " if i < len(items)-1 else "    "
                tree(item, prefix + extension)

    tree(Path('.'))