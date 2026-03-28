def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
        max_msg = True
    else:
        max_msg = False

    return fine, max_msg
    # -------- MAIN PROGRAM --------
data = input().split()
book_title = " ".join(data[:-1])   # default assumption
days_overdue = int(data[-1])
daily_rate = 5.0
max_fine = 150.0
