import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
from torchvision import models, transforms

# Function to load and preprocess the image
def load_image(image_path):
    image = Image.open(image_path).convert('RGB')
    return np.array(image)

# Function to estimate depth (placeholder)
def estimate_depth(image_array):
    # Here, we would normally use a deep learning model for depth estimation.
    # For simplicity, we create a dummy depth map based on the image's grayscale values.
    gray_image = np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140])  # Convert to grayscale
    depth_map = gray_image / 255.0  # Normalize to [0, 1]
    return depth_map

# Function to create a 3D mesh
def create_3d_mesh(image_array, depth_map):
    x = np.arange(image_array.shape[1])
    y = np.arange(image_array.shape[0])
    x, y = np.meshgrid(x, y)
    z = depth_map  # Use the depth map obtained earlier

    return x, y, z

# Function to plot the 3D surface
def plot_3d_surface(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='b', alpha=0.5)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Depth')
    plt.show()

# Main function
def main():
    # Load the high-resolution image
    high_res_image_path = 'High Resolution.jpg'
    high_res_image = load_image(high_res_image_path)

    # Load the low-resolution image
    low_res_image_path = 'Low Resolution.jpg'
    low_res_image = load_image(low_res_image_path)

    # Estimate depth for both images
    high_res_depth = estimate_depth(high_res_image)
    low_res_depth = estimate_depth(low_res_image)

    # Create 3D meshes
    high_res_x, high_res_y, high_res_z = create_3d_mesh(high_res_image, high_res_depth)
    low_res_x, low_res_y, low_res_z = create_3d_mesh(low_res_image, low_res_depth)

    # Plot the 3D surfaces
    print("Plotting high-resolution image...")
    plot_3d_surface(high_res_x, high_res_y, high_res_z)

    print("Plotting low-resolution image...")
    plot_3d_surface(low_res_x, low_res_y, low_res_z)

if __name__ == "__main__":
    main()