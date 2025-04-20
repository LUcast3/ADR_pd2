from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/check')
def check_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({"error": "Nieprawidłowe dane wejściowe"}), 400

    if a > 0 and b > 0 and (a * b) > 25:
        decision = 1
    else:
        decision = 0

    return jsonify({
        "result": decision,
        "description": "Iloczyn większy niż 25 i oba dodatnie",
        "inputs": {
            "a": a,
            "b": b
        }
    })

if __name__ == '__main__':
    app.run(port=5050)
