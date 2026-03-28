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
# Handle optional inputs
if len(data) >= 3:
    try:
        days_overdue = int(data[-3])
        daily_rate = float(data[-2])
        max_fine = float(data[-1])
        book_title = " ".join(data[:-3])
    except:
        try:
            days_overdue = int(data[-2])
            daily_rate = float(data[-1])
            book_title = " ".join(data[:-2])
        except:
            pass
            fine, max_msg = calculate_fine(book_title, days_overdue, daily_rate, max_fine)

print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")

if max_msg:
    print(f"You have accumulated the maximum fine of INR: {max_fine}")
