def calc_net_price(price, tax_rate=0.1, discount=0):
    taxed = price * (1 + tax_rate)
    net = taxed - discount
    return net

def eligibility(age, has_id):
    return age >= 18 and has_id

if __name__ == '__main__':
    print(calc_net_price(100, tax_rate=0.08, discount=5))
    print(eligibility(20, True))
