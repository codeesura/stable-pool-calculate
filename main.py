from sympy import symbols, Eq, solve

# Initial amounts of WETH and USDC
x = 1.34  # WETH
y = 7468.1  # USDC

# Constant product (k) 
k = x**3 * y + y**3 * x

# Amount of USDC to swap
usdc_to_swap = 20000

# New amount of USDC after the swap
y_new = y + usdc_to_swap

# Define the equation to solve
x_new = symbols('x_new')
equation = Eq(x_new**3 * y_new + y_new**3 * x_new, k)

# Solve the equation for the new amount of WETH
solution = solve(equation, x_new)
x_new_value = [sol.evalf() for sol in solution if sol.is_real and sol > 0][0]

# Print the new amounts of WETH and USDC in the pool
print(f"New WETH amount in the pool: {x_new_value}")
print(f"New USDC amount in the pool: {y_new}")

# The solution is a list of roots, we want the real positive root
weth_received = [sol.evalf() for sol in solution if sol.is_real and sol > 0][0] - x
print(f"You will receive approximately {weth_received} WETH for {usdc_to_swap} USDC.")
