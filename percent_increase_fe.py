# Percent Increase Activity

# Formulas
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# @TODO: Create float variable for original_price
original_price = 198.87

# @TODO: Create float variable for current_price
current_price = 254.32

# @TODO: Calculate difference between current_price and original_price
increase = current_price - original_price

# @TODO: Calculate percent_increase
percent_increase = increase / original_price * 100

# Print original_price
print(f"Apple's original stock price was ${original_price}")

# Print current_price
print(f"Apples current stock price is ${current_price}")

# @TODO: Print percent_increase to 2 decimal places using f-string formatting
width = 4
precision = 4
print(f"Apple's stock price increased by {percent_increase:{width}.{precision}}%")
# print(f"Apple's stock price increased by {percent_increase:.2f}%")
# print(f"Apple's stock price increased by {round(percent_increase, 2)}%")