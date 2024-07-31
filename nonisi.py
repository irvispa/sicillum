import matplotlib.pyplot as plt

# Create a simple plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Example Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Save the figure with tight bounding box
plt.savefig('example_plot.png', bbox_inches='tight')

# Show the plot
plt.show()
