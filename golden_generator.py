import random
import csv

# -----------------------------
# Configuration
# -----------------------------
N = 5            # Vector length
BITSIZE = 15     # Bits per element
NUM_SAMPLES = 100 #Number of tests

OUTPUT_INPUT_FILE = "golden_inputs.csv"
OUTPUT_REF_FILE   = "golden_references.csv"

# -----------------------------
# Helper functions
# -----------------------------
def rand_value(bits):
    """Generate a random integer within the allowed bit range."""
    # Range: 0 ... (2^bits - 1)
    return random.randint(0, (1 << bits) - 1)


# -----------------------------
# Generate samples
# -----------------------------
all_inputs = []
all_refs = []

for _ in range(NUM_SAMPLES):
    a = [rand_value(BITSIZE) for _ in range(N)]
    b = [rand_value(BITSIZE) for _ in range(N)]
    d = sum(a) + sum(b)

    # Save inputs to list
    all_inputs.append(a + b)

    # Mask result to available bits
    d = d & ((1 << BITSIZE) -1)

    # Save result to list
    all_refs.append(d)

# -----------------------------
# Write files
# -----------------------------

# Write inputs to csv
with open(OUTPUT_INPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    # Add identifiers in the first row
    writer.writerow([f"A{i}" for i in range(N)] + [f"B{i}" for i in range(N)])
    for row in all_inputs:
        writer.writerow(row)

# Write outputs to csv
with open(OUTPUT_REF_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    # Add identifiers in the first row
    writer.writerow(["DISTANCE"])
    for distance in all_refs:
        writer.writerow([distance])

# Simple finish message
print("Golden input and reference files generated.")

