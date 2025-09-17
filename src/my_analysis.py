# src/my_analysis.py
import matplotlib.pyplot as plt
import numpy as np


def generate_data(n_samples: int = 1000) -> np.ndarray:
    """Generate synthetic data for analysis."""
    np.random.seed(42)
    return np.random.normal(0, 1, n_samples)


def plot_distribution(data: np.ndarray) -> None:
    """Plot the distribution of the data."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=50, alpha=0.7, edgecolor="black")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Data Distribution")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    data = generate_data()
    plot_distribution(data)
    print(f"Generated {len(data)} samples")
