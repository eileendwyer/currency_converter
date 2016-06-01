class Money:

        def __init__(self, value, currency):
            self.value = value
            self.currency = currency

        def __add__(self, other):

            def __str__(self):
                return ("{} {}'s".format(self.value, self.currency)
                      +  " equals {} USD.".format(self.converted_value))

        def __mul__(self, value):

            def converted_value(self, value):
                if self.currency == "XTC":
                    return self.converted_value * 530.696
                elif self.currency == "EUR":
                    return self.converted_value * 1.11315
                elif self.currency == "JPY":
                    return self.converted_value * .00905
                else:
                    return self.value * 1

instance_1 = Money(25, "XTC")
instance_1.currency = "JPY"
#print(instance_1.currency)
instance_2 = Money(8, "JPY")
print(instance_2.value)
instance_3 = instance_1.currency + instance_2.currency
if instance_1.currency >= instance_2.currency:
    print(instance_1 - instance_2)
elif instance_1.currency <= instance_2.currency:
    print(instance_1.currency * instance_2.currency)
elif instance_1.currency == instance_2.currency:
    print(instance_1.currency**2)
elif instance_1.currency != instance_2.currency:
    print("They are not equal.")




