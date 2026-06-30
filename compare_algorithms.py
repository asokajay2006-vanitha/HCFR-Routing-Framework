"""
HCFR Routing Framework
Compare All Routing Algorithms
"""

import os
import pandas as pd

OUTPUT_DIR = "outputs"

# Files to compare
files = {
    "SPR": "spr_results.csv",
    "LAR": "lar_results.csv",
    "ML-IDS": "mlids_results.csv",
    "AAR": "aar_results.csv",
    "HCFR": "simulation_results.csv"
}

comparison = []

# ----------------------------
# Read Baseline Results
# ----------------------------

for method, filename in files.items():

    filepath = os.path.join(OUTPUT_DIR, filename)

    if not os.path.exists(filepath):
        print(f"[WARNING] {filename} not found. Skipping {method}.")
        continue

    df = pd.read_csv(filepath)

    # HCFR simulator output
    if filename == "simulation_results.csv":

        row = {
            "Method": "HCFR",
            "Throughput": df.loc[0, "Throughput"],
            "PDR": df.loc[0, "Packet_Delivery_Ratio"] * 100,
            "PacketLoss": df.loc[0, "Packet_Loss"] * 100,
            "Delay": df.loc[0, "Average_Delay(ms)"]
        }

    # Baseline output
    else:

        row = {
            "Method": df.loc[0, "Method"],
            "Throughput": df.loc[0, "Throughput"],
            "PDR": df.loc[0, "PDR"],
            "PacketLoss": df.loc[0, "PacketLoss"],
            "Delay": df.loc[0, "Delay"]
        }

    comparison.append(row)

# ----------------------------
# Save Comparison
# ----------------------------

if len(comparison) == 0:

    print("\nERROR: No result files were found!")
    print("Run the baseline scripts first.")
    exit()

comparison_df = pd.DataFrame(comparison)

comparison_df.to_csv(
    os.path.join(OUTPUT_DIR, "comparison_results.csv"),
    index=False
)

print("\nComparison Results\n")
print(comparison_df)

print("\nSaved Successfully")
print("outputs/comparison_results.csv")