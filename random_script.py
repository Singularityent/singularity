#!/usr/bin/env python3
"""
Random Script Generator
A fun script that generates random data and performs various operations
"""

import random
import datetime
import json
import os

def generate_random_data():
    """Generate some random data"""
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "random_number": random.randint(1, 1000),
        "random_string": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)),
        "random_list": [random.randint(1, 100) for _ in range(5)],
        "random_float": round(random.uniform(0, 1), 4)
    }
    return data

def calculate_fibonacci(n):
    """Calculate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    print("🎲 Random Script Generator 🎲")
    print("=" * 40)
    
    # Generate random data
    random_data = generate_random_data()
    print("📊 Generated Random Data:")
    print(json.dumps(random_data, indent=2))
    
    # Calculate Fibonacci sequence
    fib_count = random.randint(5, 15)
    fibonacci = calculate_fibonacci(fib_count)
    print(f"\n🔢 Fibonacci sequence ({fib_count} terms):")
    print(fibonacci)
    
    # Random file operations
    filename = f"random_output_{random.randint(1000, 9999)}.txt"
    with open(filename, 'w') as f:
        f.write(f"Random Script Output\n")
        f.write(f"Generated at: {random_data['timestamp']}\n")
        f.write(f"Random number: {random_data['random_number']}\n")
        f.write(f"Random string: {random_data['random_string']}\n")
    
    print(f"\n📁 Created file: {filename}")
    print(f"📏 File size: {os.path.getsize(filename)} bytes")
    
    # Random color in terminal
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset_color = '\033[0m'
    random_color = random.choice(colors)
    
    print(f"\n{random_color}🌈 This script was randomly generated! 🌈{reset_color}")
    print("✨ Thanks for using the Random Script Generator! ✨")

if __name__ == "__main__":
    main()
