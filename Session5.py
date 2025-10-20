import numpy as np

def generate_sine_table(start_x, end_x, num_entries):
    
    table_data = []
    step = (end_x - start_x) / (num_entries - 1) if num_entries > 1 else 0

    for i in range(num_entries):
        x = start_x + i * step
        sin_x = np.sin(x)
        table_data.append((x, sin_x))
    return table_data

def print_table(table_data):
    
    print(f"{'x':<10} | {'sin(x)':<15}")
    print("-" * 27)
    for x, sin_x in table_data:
        print(f"{x:<10.6f} | {sin_x:<15.6f}")

def main():
    
    start_value = 0.0
    end_value = 2 * np.pi
    number_of_entries = 1000
    sine_table = generate_sine_table(start_value, end_value, number_of_entries)
    print_table(sine_table)

if __name__ == "__main__":
    main()