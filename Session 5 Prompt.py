import numpy as np

def tabulate_sin():
    x_values = np.linspace(0, 2, 1000)
    
    sin_values = np.sin(x_values)
    
    print(f"{'x':>10} {'sin(x)':>10}")
    print("-" * 22)
    
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x:>10.6f} {sin_x:>10.6f}")

def main():
    tabulate_sin()

main()