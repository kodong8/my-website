
from flask import Flask, render_template, request, jsonify
from lotto_utils import generate_lotto_numbers, check_winning, reset_totals

app = Flask(__name__)

# 누적 금액 저장용 전역 변수
total_cost_accumulated = 0
total_prize_accumulated = 0

# 홈 페이지 라우트
@app.route("/")
def index():
    return render_template("index.html")

# 로또 시뮬레이션 API
@app.route("/simulate", methods=["POST"])
def simulate():
    global total_cost_accumulated, total_prize_accumulated

    try:
        data = request.json
        count = int(data.get("count", 0))
        if count <= 0:
            return jsonify({"error": "Invalid count"}), 400
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    lottos = [generate_lotto_numbers() for _ in range(count)]
    total_cost = count * 1000
    total_cost_accumulated += total_cost

    winning_numbers = generate_lotto_numbers()
    bonus_number = generate_lotto_numbers()[0]

    results = check_winning(lottos, winning_numbers, bonus_number)
    total_prize = sum(result[1] for result in results)
    total_prize_accumulated += total_prize

    # 등수 정렬
    sorted_results = sorted(zip(lottos, results), key=lambda x: (x[1][0] if x[1][0] > 0 else float('inf')))

    return jsonify({
        "winning_numbers": winning_numbers,
        "bonus_number": bonus_number,
        "sorted_results": [{"lotto": lotto, "rank": rank, "prize": prize} for lotto, (rank, prize, _) in sorted_results],
        "total_cost": total_cost,
        "total_prize": total_prize,
        "accumulated_cost": total_cost_accumulated,
        "accumulated_prize": total_prize_accumulated
    })


# 초기화 API
@app.route("/reset", methods=["POST"])
def reset():
    global total_cost_accumulated, total_prize_accumulated
    total_cost_accumulated = 0
    total_prize_accumulated = 0
    return jsonify({
        "message": "Reset successful",
        "accumulated_cost": total_cost_accumulated,
        "accumulated_prize": total_prize_accumulated
    })


if __name__ == "__main__":
    app.run(debug=True)
