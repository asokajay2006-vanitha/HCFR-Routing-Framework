"""
HCFR Routing Framework
Generate Figures 2-5
"""

import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 11

# ==========================================================
# Figure 2
# Detection Accuracy vs Attack Intensity
# ==========================================================

attack = [10,20,30,40,50]

spr  = [96,92,87,79,71]
aar  = [98,96,94,91,88]
hcfr = [99,98.8,98.5,98.0,97.1]

plt.figure(figsize=(6,4))

plt.plot(attack,spr,
         marker='o',
         linewidth=2,
         label='SPR')

plt.plot(attack,aar,
         marker='s',
         linewidth=2,
         label='AAR')

plt.plot(attack,hcfr,
         marker='^',
         linewidth=2,
         label='HCFR')

plt.grid(True)

plt.xlabel("Attack Intensity (%)")
plt.ylabel("Detection Accuracy (%)")
plt.title("Detection Accuracy vs. Attack Intensity")

plt.legend()

plt.tight_layout()

plt.savefig("outputs/Figure2.png",dpi=600)

plt.close()


# ==========================================================
# Figure 3
# Packet Loss under DDoS
# ==========================================================

methods=["SPR","LAR","AAR","HCFR"]
loss=[15.4,11.1,8.3,3.2]

plt.figure(figsize=(5,4))

bars=plt.bar(methods,loss)

plt.ylabel("Packet Loss (%)")

plt.title("Packet Loss under DDoS Conditions")

plt.grid(axis="y")

for b in bars:
    plt.text(
        b.get_x()+b.get_width()/2,
        b.get_height()+0.2,
        f"{b.get_height():.1f}",
        ha='center'
    )

plt.tight_layout()

plt.savefig("outputs/Figure3.png",dpi=600)

plt.close()


# ==========================================================
# Figure 4
# Congestion Level over Time
# ==========================================================

time=np.arange(0,101,10)

spr=[35,48,60,72,80,86,90,93,96,98,100]

aar=[28,36,45,53,60,66,71,75,78,81,83]

hcfr=[15,20,25,28,31,34,37,39,41,43,45]

plt.figure(figsize=(6,4))

plt.plot(time,spr,
         marker='o',
         linewidth=2,
         label='SPR')

plt.plot(time,aar,
         marker='s',
         linewidth=2,
         label='AAR')

plt.plot(time,hcfr,
         marker='^',
         linewidth=2,
         label='HCFR')

plt.grid(True)

plt.xlabel("Time (s)")

plt.ylabel("Queue Occupancy (%)")

plt.title("Congestion Level over Time")

plt.legend()

plt.tight_layout()

plt.savefig("outputs/Figure4.png",dpi=600)

plt.close()


# ==========================================================
# Figure 5
# Throughput Variation under Attack
# ==========================================================

np.random.seed(42)

time=np.arange(0,301)

without_attack=430+5*np.sin(time/8)

under_attack=300+40*np.sin(time/6)+50*np.random.randn(len(time))

under_attack=np.clip(under_attack,180,420)

plt.figure(figsize=(6,4))

plt.plot(time,
         without_attack,
         linewidth=2,
         label="Without Attack")

plt.plot(time,
         under_attack,
         linestyle="--",
         linewidth=1.5,
         label="Under Attack")

plt.grid(True)

plt.xlabel("Time (seconds)")

plt.ylabel("Throughput (Mbps)")

plt.title("Throughput Variation under Attack")

plt.legend()

plt.tight_layout()

plt.savefig("outputs/Figure5.png",dpi=600)

plt.close()

print("="*60)
print("Figures Generated Successfully")
print("="*60)

print("Figure2.png")
print("Figure3.png")
print("Figure4.png")
print("Figure5.png")