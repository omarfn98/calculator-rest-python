from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/add')
def add():
    operands = request.args.get('operands', '')
    try:
        if operands.strip() == '':
            total = 0.0
        else:
            total = sum(float(x.strip()) for x in operands.split(','))
        return jsonify({"sum": total})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400


# Entry point
if __name__ == '__main__':
    app.run(debug=True)
