stan={'chleb':
          {'quantity':10, 'price':5},
      'jajka':
          {'quantity':10, 'price':3},
      'woda':
          {'quantity':10, 'price':1.5}}

def update_quantity(product,value):
    stan[product]['quantity'] -= value