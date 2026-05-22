import sys
import csv


# Check command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

data = []

# Read input CSV
try:
    with open(input_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].strip().split(", ")
            data.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

# Write output CSV
with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(data)


