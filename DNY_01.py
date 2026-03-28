def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
