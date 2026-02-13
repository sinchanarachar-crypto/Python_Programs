# Simulate a robotic arm transformation using matrix multiplication.
# Multiply a matrix of joint positions (coordinates) with a transformation matrix and print the new coordinates.

# Function for matrix multiplication
def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):           # rows of A
        for j in range(len(B[0])):    # columns of B
            for k in range(len(B)):   # columns of A / rows of B
                result[i][j] += A[i][k] * B[k][j]
    return result


# Define joint positions (homogeneous coordinates: [x, y, z, 1])
joints = [
    [0, 0, 0, 1],   # Base
    [2, 0, 0, 1],   # Joint 1
    [4, 1, 0, 1],   # Joint 2
    [6, 1, 0, 1]    # End-effector
]

print("Original Joint Coordinates:")
for row in joints:
    print(row)


# Transformation matrix: rotate 90° around Z-axis + translate (1, 2, 0)
theta = 90 * 3.14159 / 180    # Convert degrees to radians
# cos_t = round(3.14159/2 - (3.14159/2 - 0), 5)   # Approx cos(90°) = 0
cos_t = 0
sin_t = 1

transformation_matrix = [
    [cos_t, -sin_t, 0, 1],
    [sin_t,  cos_t, 0, 2],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

print("\nTransformation Matrix:")
for row in transformation_matrix:
    print(row)


# Apply transformation: Joints × Transformation^T
# (We'll transpose transformation matrix for correct multiplication)
transposed_T = [[transformation_matrix[j][i] for j in range(4)] for i in range(4)]

new_joints = multiply_matrices(joints, transposed_T)

print("\nNew Joint Coordinates after Transformation:")
for row in new_joints:
    print(row)
