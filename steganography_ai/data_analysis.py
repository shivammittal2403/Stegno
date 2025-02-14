import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(file_path):
    # Example: Load data from a CSV file and analyze it
    try:
        data = pd.read_csv(file_path)
        print(data.describe())
        data.hist()
        plt.show()
    except Exception as e:
        print(f"Error analyzing data: {e}")
