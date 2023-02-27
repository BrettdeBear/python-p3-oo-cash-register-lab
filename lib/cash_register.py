#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []
    

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.transactions.append(price * quantity)
    for item in range(quantity):
      self.items.append(title)
    # self.items.append(title * quantity)
    
    
    # apply_discount = total_price * self.discount /100
    # self.total += apply_discount

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = self.total * self.discount / 100
      self.total -= discount_amount
    # the 2 lines above may be easier to read
    # self.total -= self.total * self.discount / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= self.transactions.pop()