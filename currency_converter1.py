class Money:

        def __init__(self, value, currency):
            self.value = value
            self.currency = currency

        def __add__(self, other):
            return self.converted_value() + other.converted_value()

        def __sub__(self, other):
            return self.converted_value() - other.converted_value()

        def __mul__(self, other):
            return self.converted_value() * other.converted_value()

        def __gt__(self, other):
            return self.converted_value() * other.converted_value()

        def __ge__(self, other):
            return self.converted_value() * other.converted_value()

        def __le__(self, other):
            return self.converted_value() * other.converted_value()

        def __lt__(self, other):
            return self.converted_value() * other.converted_value()

        def __str__(self):
            return ("{} {}'s".format(self.value, self.currency)
                      +  " equals {} USD.".format(self.converted_value))

        def converted_value(self):
            if self.currency == "XTC":
                return self.value * 530.696
            elif self.currency == "EUR":
                return self.value * 1.11315
            elif self.currency == "JPY":
                return self.value * .00905
            else:
                return self.value * 1

instance_1 = Money(25, "USD")
#print(instance_1.value)
#print(instance_1.currency)
print(instance_1.converted_value())
instance_2 = Money(8, "EUR")
#print(instance_2.value)
instance_3 = instance_1 + instance_2
print(instance_3)
print(instance_1 - instance_2)
print(instance_1 * instance_2)
print(instance_1 >= instance_2)
print(instance_1 <= instance_2)


