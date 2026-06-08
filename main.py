import matplotlib.pyplot as plt

# Data
age_groups = ['0-14', '15-64', '65+']
population = [25.3, 67.8, 6.9]

# Colors (Red, Green, Blue)
colors = ['red', 'green', 'blue']

# Bigger figure
plt.figure(figsize=(10, 6))

# Bar chart
bars = plt.bar(age_groups, population, color=colors)

# Title and labels
plt.title("India Population Distribution by Age (2022)", fontsize=16)
plt.xlabel("Age Group", fontsize=14)
plt.ylabel("Percentage (%)", fontsize=14)

# Add values above bars (with spacing)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 2,   # extra space above bar
        f'{height}%',
        ha='center',
        fontsize=12
    )

# Remove grid (IMPORTANT)
plt.grid(False)

# Add top space so labels don't touch border
plt.ylim(0, 80)

# Show chart
plt.show()
