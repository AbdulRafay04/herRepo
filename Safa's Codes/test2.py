import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure
fig, ax = plt.subplots(figsize=(10, 8))

# Create a dictionary for positions of the text boxes
positions = {
    "start": (0.5, 0.9),
    "import": (0.5, 0.8),
    "flag": (0.5, 0.7),
    "loop_start": (0.5, 0.6),
    "message": (0.5, 0.5),
    "wait": (0.4, 0.4),
    "check": (0.6, 0.4),
    "give_up": (0.6, 0.3),
    "repeat": (0.4, 0.3),
    "end": (0.5, 0.1),
}

# Add the text boxes
ax.text(*positions["start"], "Start", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"))
ax.text(*positions["import"], "import time", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen"))
ax.text(*positions["flag"], "dormammu_gives_up = False", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen"))
ax.text(*positions["loop_start"], "while not dormammu_gives_up:", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightyellow"))
ax.text(*positions["message"], 'print("Dormammu, I\'ve come to bargain!")', ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen"))
ax.text(*positions["wait"], "time.sleep(1)", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen"))
ax.text(*positions["check"], "if i == 3:", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightyellow"))
ax.text(*positions["give_up"], "dormammu_gives_up = True", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen"))
ax.text(*positions["repeat"], "Increment i\n(repeat loop)", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightyellow"))
ax.text(*positions["end"], "End", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"))

# Draw the arrows
arrowprops = dict(arrowstyle="->", color="black", linewidth=2)

ax.annotate("", xy=positions["start"], xytext=positions["import"], arrowprops=arrowprops)
ax.annotate("", xy=positions["import"], xytext=positions["flag"], arrowprops=arrowprops)
ax.annotate("", xy=positions["flag"], xytext=positions["loop_start"], arrowprops=arrowprops)
ax.annotate("", xy=positions["loop_start"], xytext=positions["message"], arrowprops=arrowprops)
ax.annotate("", xy=positions["message"], xytext=positions["wait"], arrowprops=arrowprops)
ax.annotate("", xy=positions["wait"], xytext=positions["check"], arrowprops=arrowprops)
ax.annotate("", xy=positions["check"], xytext=positions["give_up"], arrowprops=arrowprops)
ax.annotate("", xy=positions["check"], xytext=positions["repeat"], arrowprops=arrowprops)
ax.annotate("", xy=positions["repeat"], xytext=positions["loop_start"], arrowprops=arrowprops)
ax.annotate("", xy=positions["give_up"], xytext=positions["end"], arrowprops=arrowprops)

# Set the plot limits and remove the axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Show the plot
plt.show()
