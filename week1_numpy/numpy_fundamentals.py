# 1D array.....
import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50])

print("1D Array:", arr_1d)
print("Shape:", arr_1d.shape)


# 2D array.....
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)


# 3D array.....
arr_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3D Array:")
print(arr_3d)
print("Shape:", arr_3d.shape)

# Broadcasting....
arr = np.array([10, 20, 30])

result = arr + 5

print("Original Array:", arr)
print("After Broadcasting:", result)



# Vectorised operations
prices = np.array([100, 200, 300, 400])

discounted_prices = prices * 0.9

print("Original Prices:", prices)
print("Discounted Prices:", discounted_prices)



# Matrix multiplication
matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

result = matrix_a @ matrix_b

print("Matrix A:")
print(matrix_a)

print("Matrix B:")
print(matrix_b)

print("Matrix Multiplication:")
print(result)



# Load the CSV dataset
data = np.genfromtxt(
    "week1_numpy/aiml_training_data.csv",
    delimiter=",",
    dtype=None,
    encoding="utf-8",
    names=True
)

print("Column names:")
print(data.dtype.names)
price = data["price_inr"]

print("Mean Price:", np.mean(price))
print("Standard Deviation of Price:", np.std(price))


# Correlation
duration = data["duration_minutes"]

correlation = np.corrcoef(price, duration)[0, 1]

print("Correlation between Price and Duration:", correlation)