class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.data = dict()

    def get(self, key: str) -> str:
        if key in self.data:
            val = self.data[key][:]
            del self.data[key]
            self.data[key] = val
            return val
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            del self.data[key]
            self.data[key] = value
        else:
            if len(self.data) >= self.capacity:
                del self.data[next(iter(self.data.keys()))]
            self.data[key] = value

    def rem(self, key: str) -> None:
        if key in self.data:
            del self.data[key]

    def __str__(self):
        return f'{self.data}'
