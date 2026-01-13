import sys

temps = sys.argv[1:]
if not temps:
    print("No temperatures provided.")
    sys.exit(1)

try:
    temps = [float(t) for t in temps]
    print(f"Max: {max(temps):.2f}")
    print(f"Min: {min(temps):.2f}")
    print(f"Mean: {sum(temps)/len(temps):.2f}")
except ValueError:
    print("Error: Please enter numbers only.")