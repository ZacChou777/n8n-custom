#!/usr/bin/env python3

def calculate_fibonacci(n):
    """
    Calculate the nth number in the Fibonacci sequence.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

def process_data(data):
    """
    Process a list of numbers and return statistics.
    """
    if not data:
        return None
    
    stats = {
        'sum': sum(data),
        'average': sum(data) / len(data),
        'max': max(data),
        'min': min(data)
    }
    return stats

def main():
    # Example usage of the functions
    try:
        # Calculate Fibonacci numbers
        print("Fibonacci sequence demo:")
        for i in range(1, 6):
            print(f"Fibonacci({i}) = {calculate_fibonacci(i)}")
        
        # Process some sample data
        print("\nData processing demo:")
        sample_data = [10, 20, 30, 40, 50]
        stats = process_data(sample_data)
        print(f"Sample data: {sample_data}")
        print(f"Statistics: {stats}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
