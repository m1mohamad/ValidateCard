from flask import Flask, jsonify, request
import os

app = Flask(__name__)

def is_valid_credit_card(card_number):
    sum = 0
    parity = len(card_number) % 2
    
    for i in range(len(card_number) - 1, -1, -1):
        current_Digit = int(card_number[i])
        if (i + 1) % 2 == parity:
            sum += current_Digit
        elif current_Digit > 4:
            sum += 2 * current_Digit - 9
        else:
            sum += 2 * current_Digit

    return sum % 10 == 0

@app.route('/api/validate/<string:card_number>', methods=['GET'])
def validate_credit_card(card_number):
    card_number = os.environ.get('CREDIT_CARD_NUMBER', card_number)
    if not card_number:
        return jsonify(error="Credit card number not provided"), 400
    
    if not card_number.isdigit():
        return jsonify(error="Credit card number must be numeric"), 400
    
    is_valid = is_valid_credit_card(card_number)
    return jsonify(isValid=is_valid), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


