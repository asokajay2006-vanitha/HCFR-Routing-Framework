"""
HCFR Routing Framework
Main Execution Script
"""

import subprocess
import sys

steps = [
    ("Generate Network Topology", "generators/topology_gen.py"),
    ("Generate Traffic", "generators/traffic_gen.py"),
    ("Generate Attack Traffic", "generators/attack_gen.py"),
    ("Sparse Feature Selection", "core/feature_selection.py"),
    ("HSNN Inference", "core/snn_inference.py"),
    ("DAG Optimization", "core/dag_optimizer.py"),
    ("Packet Simulation", "simulators/packet_simulator.py"),
]

for title, script in steps:

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nError while running {script}")
        break

print("\nHCFR Execution Completed")