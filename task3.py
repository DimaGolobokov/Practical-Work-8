class KgToPounds:

    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self._kg * 2.205

weight = KgToPounds(10)
print(weight.kg)

weight.kg = 15
print(weight.to_pounds())
