#include <stdio.h>

#define ROWS 3
#define COLS 3

// Function to initialize the matrix with user input
void initializeMatrix(int matrix[][COLS], int rows, int cols) {
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
}

// Function to print the matrix
void printMatrix(int matrix[][COLS], int rows, int cols) {
    printf("Matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// Function to calculate the sum of all elements in the matrix
int calculateSum(int matrix[][COLS], int rows, int cols) {
    int sum = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            sum += matrix[i][j];
        }
    }
    return sum;
}

int main() {
    int matrix[ROWS][COLS];

    // Initialize the matrix
    initializeMatrix(matrix, ROWS, COLS);

    // Print the matrix
    printMatrix(matrix, ROWS, COLS);

    // Calculate the sum of all elements in the matrix
    int sum = calculateSum(matrix, ROWS, COLS);
    printf("Sum of all elements: %d\n", sum);

    return 0;
}
