# Import packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from scipy.interpolate import griddata

# Import data, remove index and percentage sign
df = pd.read_csv("./School/SocialChoiceSystemsFL23/data.csv")
df['has_winner'] = df['has_winner'].str.rstrip('%').astype(float) / 100.0

# Create X, Y, and Z coordinates
X = df['num_voters']
Y = df['num_alternatives']
Z = df['has_winner']

# Define the regular grid for the 3D surface plot
X_interp = np.linspace(X.min(), X.max(), 100)
Y_interp = np.linspace(Y.min(), Y.max(), 100)
X_interp, Y_interp = np.meshgrid(X_interp, Y_interp)

# Interpolate the Z values onto the regular grid
Z_interp = griddata((X, Y), Z, (X_interp, Y_interp), method='cubic')

# Create the 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(X_interp, Y_interp, Z_interp, cmap='viridis')

# Add labels and a color bar
ax.set_title("Percentage of Times a Condorcet Winner Occured with Variable\nVoters and Alternatives Over 100,000 Simulations")
ax.set_xlabel('Number of Voters')
ax.set_ylabel('Number of Alternatives')
ax.set_zlabel('Condorcet Winner Percentage')
fig.colorbar(surface, label='Percentage')

# Show the plot
plt.show()
