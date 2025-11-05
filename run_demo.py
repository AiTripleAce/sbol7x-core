import matplotlib.pyplot as plt

runs = {
    "Fear Cycle": 32,
    "Guidance Loop": 100
}

plt.bar(runs.keys(), runs.values())
plt.title("SBOL Test Runs")
plt.ylabel("Signal Output (pts)")
plt.grid(True, axis="y")
plt.show()

for k,v in runs.items():
    print(f"{k}: {v} pts")
