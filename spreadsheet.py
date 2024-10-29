
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._visited = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        elif value.startswith("="):
            if value[1:].startswith("'") and value.endswith("'"):
                return value[2:-1]
            elif value[1:].startswith("'") and not value.endswith("'"):
                return "#Error"
            else:
                try:
                    if value[1:].isnumeric():
                        return int(value[1:])
                    elif value[1:] in self._cells:
                        if value[1:] in self._visited:
                            return "#Circular"
                        self._visited.add(value[1:])
                        result = self.evaluate(value[1:])
                        self._visited.remove(value[1:])
                        if isinstance(result, str) and result != "#Circular":
                            return "#Error"
                        return result
                    else:
                        if any(char.isdigit() and char2 == '.' for char, char2 in zip(value, value[1:])):
                            return "#Error"
                        # Replace eval with a safer alternative
                        try:
                            return int(eval(value[1:]))
                        except (SyntaxError, TypeError, ZeroDivisionError):
                            return "#Error"
                except ValueError:
                    return "#Error"
        else:
            try:
                return int(value)
            except ValueError:
                return "#Error"

