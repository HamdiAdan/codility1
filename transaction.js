function solution(A, D, N) {
    let balance = 0;
    let monthlyFee = 0;
    let cardPayments = 0;
    let currentMonth = new Date('2020-01-01');

    for (let i = 0; i < N; i++) {
        let transactionDate = new Date(D[i]);

        if (transactionDate.getFullYear() > currentMonth.getFullYear() ||
            transactionDate.getMonth() > currentMonth.getMonth()) {
            currentMonth.setMonth(currentMonth.getMonth() + 1);
            cardPayments = 0;
            if (currentMonth.getMonth() !== 0) { // Apply monthly fee for all months except January
                monthlyFee += 5;
            }
        }

        if (A[i] >= 0) {
            balance += A[i];
        } else {
            balance -= A[i];
            cardPayments++;

            if (cardPayments >= 3 && -A[i] >= 100) {
                monthlyFee -= 5;
            }
        }
    }

    balance -= monthlyFee * 12; // Deduct total monthly fee for the year

    return balance;
}


