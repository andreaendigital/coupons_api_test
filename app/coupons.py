def apply_coupon(price, coupon_code):
    discounts = {
        "SALES10": 0.10,
        "SUPER20": 0.20,
       "WELCOME": 0.15  # lo comentamos para simular eliminación para prueba de regresión
    }

    if coupon_code in discounts:
        return round(price * (1 - discounts[coupon_code]), 2)
    
    return price


def get_final_price(base_price, coupon_code, tax_rate=0.19):
    discounted_price = apply_coupon(base_price, coupon_code)
    return round(discounted_price * (1 + tax_rate), 2)