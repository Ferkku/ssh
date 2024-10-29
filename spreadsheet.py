
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        elif value.startswith("=") and value[1:].startswith("'") and value.endswith("'"):
            return value[2:-1]
        elif value.startswith("="):
            try:
                if value[1:].isnumeric():
                    return int(value[1:])
                else:
                    return self.evaluate(value[1:])
            except ValueError:
                return "#Error"
        try:
            return int(value)
        except ValueError:
            try:
                float(value)
                return "#Error"
            except ValueError:
                return "#Error"

