from flask import Flask, request, jsonify
from app.coupons import get_final_price  

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def calculate():
    data = request.get_json()
    base_price = data.get("price")              # Original price
    coupon_code = data.get("coupon")            # Discount coupon
    tax_rate = data.get("tax", 0.19)            # Default to 19% if not specified

    final_price = get_final_price(base_price, coupon_code, tax_rate)
    return jsonify({"Final_price": final_price})