async function simulate() {
    const count = document.getElementById("count").value;
    const response = await fetch("/simulate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ count: parseInt(count) }),
    });

    const data = await response.json();
    if (response.ok) {
        displayResults(data);
        displayLottoHistory(data.lottos); // 구매한 로또 번호 표시
    } else {
        alert(data.error);
    }
}

function displayResults(data) {
    const resultsDiv = document.getElementById("results");

    function getBallColor(num) {
        if (num <= 10) return "#ffcc00";
        if (num <= 20) return "#ff6666";
        if (num <= 30) return "#66ccff";
        if (num <= 40) return "#99ff99";
        return "#ff99ff";
    }
    

    
    // 로또 번호 표시
    // const lottoBalls = data.winning_numbers
    // .map(num => `<span class="lotto-ball">${num}</span>`)
    // .join(" ");
    const lottoBalls = data.winning_numbers.map(num => 
        `<span class="lotto-ball" style="background-color: ${getBallColor(num)};">${num}</span>`
    ).join("");
    const bonusBall = `<span class="lotto-ball">${data.bonus_number}</span>`;


        resultsDiv.innerHTML = `
            <p>당첨 번호: ${lottoBalls} (보너스: ${bonusBall})</p>
            <p>이번 구매 금액: ${data.total_cost}원</p>
            <p>이번 당첨 금액: ${data.total_prize}원</p>
            <p>누적 구매 금액: ${data.accumulated_cost}원</p>
            <p>누적 당첨 금액: ${data.accumulated_prize}원</p>
        `;
    }

//     resultsDiv.innerHTML = `<p>당첨 번호:</p>${lottoBalls}`;

//     // 보너스 번호 표시
//     const bonusBall = `<span class="lotto-ball" style="background-color: #ff5733;">${data.bonus_number}</span>`;
//     bonusDiv.innerHTML = `<p>보너스 번호:</p>${bonusBall}`;
// }


function displayLottoHistory(sortedResults) {
    const lottoList = document.getElementById("lotto-list");
    lottoList.innerHTML = ""; // 기존 내용을 초기화

    sortedResults.forEach(({ lotto, rank, prize }, index) => {
        const listItem = document.createElement("li");

        if (rank > 0) {
            listItem.textContent = `로또 ${index + 1}: ${lotto} → ${rank}등 (${prize}원 당첨)`;
        } else {
            listItem.textContent = `로또 ${index + 1}: ${lotto} → 꽝`;
        }

        lottoList.appendChild(listItem);
    });
}

async function simulate() {
    const count = document.getElementById("count").value;

    const response = await fetch("/simulate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ count: parseInt(count) }),
    });

    const data = await response.json();
    if (response.ok) {
        displayResults(data);
        displayLottoHistory(data.sorted_results); // 구매 내역 표시
    } else {
        alert(data.error);
    }
}




async function reset() {
    const response = await fetch("/reset", { method: "POST" });
    const data = await response.json();
    if (response.ok) {
        alert(data.message);
        document.getElementById("results").innerHTML = `
            <p>누적 구매 금액: ${data.accumulated_cost}원</p>
            <p>누적 당첨 금액: ${data.accumulated_prize}원</p>
        `;
        document.getElementById("lotto-list").innerHTML = ""; // 구매 내역 초기화
    }
}


