class ZeroQuantityException(Exception):
    """Класс исключения Нулевого Количества"""

    def __init__(self, *args, **kwargs):
        if args:
            self.message = args[0]
        else:
            self.message = "Нельзя добавлять нулевое количество"

    def __str__(self):
        return self.message
