from django.db import models

'''
Transaction stores an occurance of an exchange for one currency to another, such as BTC -> USD$
'''
class Transaction(models.Model):
    from_symbol = models.CharField(max_length=20)
    to_symbol = models.CharField(max_length=20)
    from_amount = models.FloatField()
    to_amount = models.FloatField()
    fee_amount = models.FloatField(default=0.0)
    tx_date = models.DateTimeField('transaction date')

    def __str__(self):
        return "{0} {1} for {2} {3} on {4}; fee={5}".format(self.from_amount,
        self.from_symbol, self.to_amount, self.to_symbol, self.tx_date, self.fee_amount)

