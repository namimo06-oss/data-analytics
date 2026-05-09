# LAB 2
balance = 2500 #bank balance
savings_goal = 500
weekly_savings_amount = 50

# WHILE LOOP
while balance < savings_goal:
    # Add weekly savings
    balance += weekly_savings_amount
    # 75% check (must come first because it's highest level)
    if balance >= savings_goal * 0.75:
        balance -= 50  # treat yourself
        print(f"So close! After treating myself, my balance is up to {balance}.")
    # More than halfway to goal
    elif balance >= savings_goal / 2:
        print(f"Almost there! This week my balance is up to {balance}.")
    # Normal progress message
    else:
        print(f"This week my balance increased to {balance}.")


# FINAL MESSAGE

print(f"Goal met! My current balance is {balance}.")



