def hill_climbing(func, start, step=0.01, max_iter=1000): 
    x = start
    for _ in range(max_iter):
        fx = func(x)
        fx_positive = func(x + step)
        fx_negative = func(x - step)

        if fx_positive > fx and fx_positive >= fx_negative:
            x += step
        elif fx_negative > fx and fx_negative > fx_positive:
            x -= step
        else:
            break
    return x, func(x)

func_str = input("Enter a function of x (e.g., -(x-2)**2 + 4): ")
func = eval(f"lambda x: {func_str}")  # Convert string to function
func(0)  # Test the function with x = 0
start = float(input("Enter the starting value (e.g., 0): "))
max_x, max_val = hill_climbing(func, start)
print(f"Maxima found at x = {max_x}")
print(f"Maximum value = {max_val}")
