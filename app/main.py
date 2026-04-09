from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/discount', methods=['GET'])
def calculate_discount():
    price_str = request.args.get('price', '0')
    
    try:
        price = float(price_str)
    except ValueError:
        return jsonify({"error": "Invalid price format"}), 400

    if price < 0:
        return jsonify({"error": "Price cannot be negative"}), 400

    # BUG: The logic is supposed to calculate a 10% discount. 
    # Instead, it simply subtracts $10 from the price.
    discounted_price = price - 10 
    
    # Secondary BUG: Does not handle negative results if price is less than $10
    
    return jsonify({"original_price": price, "discounted_price": discounted_price}), 200

if __name__ == "__main__":
    # Security flaw: running with debug=True in an exposed state
    app.run(host="0.0.0.0", port=5000, debug=True)