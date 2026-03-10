import random
import numpy as np

def augmentation_by_color(x, colors):
    x = np.array(x)
    #return np.array([colors[xi] for xi in x.flatten()]).reshape(x.shape)
    return colors[x.flatten()].reshape(x.shape)


def rotate_matrix_90(matrix):
    return np.rot90(matrix, -1)  # Rotate 90 degrees clockwise

def rotate_matrix_180(matrix):
    return np.rot90(matrix, 2)  # Rotate 180 degrees

def rotate_matrix_270(matrix):
    return np.rot90(matrix, 1)  # Rotate 270 degrees clockwise

def rotate_matrix_360(matrix):
    return matrix.copy()  # 360 degrees rotation results in the same matrix


def reflect_matrix_horizontal(matrix):
    return np.fliplr(matrix)  # Reflect horizontally

def reflect_matrix_vertical(matrix):
    return np.flipud(matrix)  # Reflect vertically

def reflect_matrix_id(matrix):
    return matrix.copy()  # Identity reflection results in the same matrix



def sample_transformations():
    # Sample transformations
    colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotation_functions = [rotate_matrix_90, rotate_matrix_180, rotate_matrix_270, rotate_matrix_360]
    reflection_functions = [reflect_matrix_horizontal, reflect_matrix_vertical, reflect_matrix_id]

    # Select random transformations
    colors1 = np.random.permutation(colors)
    selected_rotation = random.choice(rotation_functions)
    selected_reflection = random.choice(reflection_functions)

    # Create a transformation chain
    transformations_chain = [
        lambda x: augmentation_by_color(x, colors1),
        selected_rotation,
        selected_reflection
    ]

    def apply_transformations(data, transformations):
        for transform in transformations:
            data = transform(data)
        return data

    return lambda x: apply_transformations(x, transformations_chain)



# ----

import random
import numpy as np

def augmentation_by_color(x, colors):
    x = np.array(x)
    return colors[x.flatten().astype(int)].reshape(x.shape)

def reverse_augmentation_by_color(x, colors):
    reverse_colors = np.argsort(colors)
    return reverse_colors[x.flatten().astype(int)].reshape(x.shape)


def reverse_augmentation_by_color(x, colors):
    """
    Create a dictionary mapping from color_value -> original_index.
    For each value in x, if it exists in our dictionary, map it back; otherwise, leave it as-is.
    """
    x = np.array(x)
    flat_x = x.flatten().astype(int)

    # Build a mapping { color_value : original_index } for the colors array
    color_to_idx = {c: i for i, c in enumerate(colors)}

    out_flat = np.copy(flat_x)

    # If a color is in our dictionary, revert it, otherwise keep it
    for i in range(len(flat_x)):
        val = flat_x[i]
        if val in color_to_idx:
            out_flat[i] = color_to_idx[val]
        else:
            out_flat[i] = val

    return out_flat.reshape(x.shape)


def rotate_matrix_90(matrix):
    return np.rot90(matrix, -1)  # Rotate 90 degrees clockwise

def rotate_matrix_180(matrix):
    return np.rot90(matrix, 2)  # Rotate 180 degrees

def rotate_matrix_270(matrix):
    return np.rot90(matrix, 1)  # Rotate 270 degrees clockwise

def rotate_matrix_360(matrix):
    return matrix.copy()  # 360 degrees rotation results in the same matrix

def reverse_rotate_matrix_90(matrix):
    return np.rot90(matrix, 1)  # Reverse of 90 degrees clockwise is 270 degrees clockwise

def reverse_rotate_matrix_180(matrix):
    return np.rot90(matrix, 2)  # Reverse of 180 degrees is 180 degrees

def reverse_rotate_matrix_270(matrix):
    return np.rot90(matrix, -1)  # Reverse of 270 degrees clockwise is 90 degrees clockwise

def reverse_rotate_matrix_360(matrix):
    return matrix.copy()  # Reverse of 360 degrees is the same matrix

def reflect_matrix_horizontal(matrix):
    return np.fliplr(matrix)  # Reflect horizontally

def reflect_matrix_vertical(matrix):
    return np.flipud(matrix)  # Reflect vertically

def reflect_matrix_id(matrix):
    return matrix.copy()  # Identity reflection results in the same matrix

def reverse_reflect_matrix_horizontal(matrix):
    return np.fliplr(matrix)  # Reverse of horizontal reflection is horizontal reflection

def reverse_reflect_matrix_vertical(matrix):
    return np.flipud(matrix)  # Reverse of vertical reflection is vertical reflection

def reverse_reflect_matrix_id(matrix):
    return matrix.copy()  # Reverse of identity reflection is the same matrix

def sample_transformations_with_revert():
    # Sample transformations
    colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotation_functions = [rotate_matrix_90, rotate_matrix_180, rotate_matrix_270, rotate_matrix_360]
    reverse_rotation_functions = [reverse_rotate_matrix_90, reverse_rotate_matrix_180, reverse_rotate_matrix_270, reverse_rotate_matrix_360]
    
    reflection_functions = [reflect_matrix_horizontal, reflect_matrix_vertical, reflect_matrix_id]
    reverse_reflection_functions = [reverse_reflect_matrix_horizontal, reverse_reflect_matrix_vertical, reverse_reflect_matrix_id]

    # Select random transformations
    colors1 = np.random.permutation(colors)
    selected_rotation = random.choice(list(zip(rotation_functions, reverse_rotation_functions)))
    selected_reflection = random.choice(list(zip(reflection_functions, reverse_reflection_functions)))

    # Create a transformation chain
    transformations_chain = [
        (lambda x: augmentation_by_color(x, colors1), lambda x: reverse_augmentation_by_color(x, colors1)),
        selected_rotation,
        selected_reflection
    ]

    def apply_transformations(data, transformations):
        for transform, _ in transformations:
            data = transform(data)
        return data

    def revert_transformations(data, transformations):
        for _, reverse_transform in reversed(transformations):
            data = reverse_transform(data)
        return data

    return (
        lambda x: apply_transformations(x, transformations_chain),
        lambda x: revert_transformations(x, transformations_chain)
    )

# # Example usage:
# apply, revert = sample_transformations()
# original_data = np.array([[1, 2], [3, 4]])
# transformed_data = apply(original_data)
# reverted_data = revert(transformed_data)

# print("Original Data:")
# print(original_data)
# print("Transformed Data:")
# print(transformed_data)
# print("Reverted Data:")
# print(reverted_data)

# # Additional tests
# def test_reversible_transformations():
#     test_data = [
#         np.array([[0, 1], [2, 3]]),
#         np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]]),
#         np.array([[9, 8], [7, 6], [5, 4]]),
#         np.zeros((3, 3)),
#         np.ones((2, 2)) * 7
#     ]

#     for idx, data in enumerate(test_data):
#         print(f"\nTest {idx + 1}:")
#         apply, revert = sample_transformations()
#         transformed = apply(data)
#         reverted = revert(transformed)

#         print("Original:")
#         print(data)
#         print("Transformed:")
#         print(transformed)
#         print("Reverted:")
#         print(reverted)

#         assert np.array_equal(data, reverted), f"Test {idx + 1} failed: Data mismatch after revert"

#     print("All tests passed.")

# # Run additional tests
# test_reversible_transformations()


def drop_rows_and_columns(matrix, value=10):
    """
    Removes rows and columns from the given matrix where all elements are equal to `value`.

    Parameters:
        matrix (numpy.ndarray): Input matrix.
        value (int or float): The value to check against. Defaults to 10.

    Returns:
        numpy.ndarray: The filtered matrix.
    """
    # Identify rows where not all elements are `value`
    row_mask = ~np.all(matrix == value, axis=1)

    # Identify columns where not all elements are `value`
    col_mask = ~np.all(matrix == value, axis=0)

    # Apply the masks to the matrix
    filtered_matrix = matrix[row_mask][:, col_mask]

    return filtered_matrix


# def drop_rows_and_columns(matrix, value=10, max_count=30):
#     """
#     Removes rows and columns from the given matrix where either:
#       - All elements are equal to `value`.
#       - More than `max_count` elements are equal to `value`.

#     Parameters:
#         matrix (numpy.ndarray): Input matrix.
#         value (int or float): The value to check against. Defaults to 10.
#         max_count (int): The maximum allowed count of `value` in a row or column. Defaults to 4.

#     Returns:
#         numpy.ndarray: The filtered matrix.
#     """
#     # Identify rows that do not meet the conditions for removal
#     row_mask = ~(
#         np.all(matrix == value, axis=1) | (np.sum(matrix == value, axis=1) > max_count)
#     )

#     # Identify columns that do not meet the conditions for removal
#     col_mask = ~(
#         np.all(matrix == value, axis=0) | (np.sum(matrix == value, axis=0) > max_count)
#     )

#     # Apply the masks to the matrix
#     filtered_matrix = matrix[row_mask][:, col_mask]

#     return filtered_matrix

# # Example usage
# matrix = np.array([
#     [10, 10, 10],
#     [10, 5, 10],
#     [10, 10, 10]
# ])

# result = drop_rows_and_columns(img)
# print("Original Matrix:")
# print(matrix)
# print("Filtered Matrix:")
# print(result)

# plt.imshow(result, cmap='viridis')
# plt.axis('off')


def merge_binary_matrices(matrices):
    """
    Merge a list of binary matrices by taking the most popular (majority) value
    for each element across the matrices.

    Args:
        matrices (list of np.ndarray): List of binary matrices (2D arrays) with 0s and 1s.

    Returns:
        np.ndarray: A single binary matrix (2D array) with majority vote for each element.
    """
    # Stack matrices into a 3D array
    stacked = np.stack(matrices, axis=2)
    
    # Compute the majority vote (most popular value for each element)
    majority_vote = (stacked.sum(axis=2) > (len(matrices) / 2)).astype(int)
    
    return majority_vote


def merge_binary_matrices_proportion(matrices):
    """
    Merge a list of binary matrices by calculating the proportion of 1s for each element.

    Args:
        matrices (list of np.ndarray): List of binary matrices (2D arrays) with 0s and 1s.

    Returns:
        np.ndarray: A single matrix (2D array) with the proportion of 1s for each element.
    """
    # Stack matrices into a 3D array
    stacked = np.stack(matrices, axis=2)

    # Calculate the proportion of 1s for each element
    proportion_of_ones = stacked.sum(axis=2) / stacked.shape[2]

    return proportion_of_ones
