from datetime import datetime

def final_balance(A, D):
    # Initialize the balance and card payments for each month
    balances = {}
    card_payments = {}
    total_card_fee = 0  # Initialize total card fee

    # Process each transaction
    for amount, date in zip(A, D):
        date = datetime.strptime(date, '%Y-%m-%d')
        year, month = date.year, date.month

        # Ignore transactions not in 2020
        if year != 2020:
            continue

        # Update the balance and card payments for the month
        if month not in balances:
            balances[month] = 0
        balances[month] += amount

        if amount < 0:
            if month not in card_payments:
                card_payments[month] = []
            card_payments[month].append(amount)

    # Iterate over the months of 2020 after processing all transactions
    for month in range(1, 13):
        # Subtract the card fee if necessary
        if month not in card_payments or len(card_payments[month]) < 3 or sum(card_payments[month]) > -100:
            balances[month] = balances.get(month, 0) - 5
            total_card_fee += 5

    # the final balance
    return sum(balances.values())

