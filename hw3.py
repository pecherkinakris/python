class Worker:
    """
    Worker storage
    """
    name = str()
    surname = str()
    position = str()
    _income = {'wage': None, 'bonus': None}

    def __init__(self, name, surname, position, wage, bonus):
        """
        :param name: str
        :param surname: str
        :param position: str
        :param wage: wage
        :param bonus: bonus
        """
        self.position = position
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    """
    Position storage
    """
    def get_full_name(self):
        """
        Name plus surname
        return: str
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        Sum of wage and bonus
        return: number
        """
        return sum(self._income.values())


if __name__ == '__main__':
    pos = Position('John', 'Smith', 'student', 180000, 20000)

    print(pos.get_full_name())
    print(pos.get_total_income())