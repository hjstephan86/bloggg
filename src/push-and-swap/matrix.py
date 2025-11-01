class Matrix:
    """
    A simple Matrix class supporting basic matrix operations
    (addition, subtraction, multiplication) and index access.
    """

    def __init__(self, data):
        """
        Initializes the Matrix with a list of lists.
        data: list of lists representing the matrix rows.
              All inner lists (rows) must have the same length.
        """
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Matrix data must be a list of lists.")
        if not data:
            self.rows = 0
            self.cols = 0
            self.data = []
            return

        self.rows = len(data)
        self.cols = len(data[0])

        if not all(len(row) == self.cols for row in data):
            raise ValueError("All rows in the matrix must have the same length.")

        # Deep copy the data to prevent external modifications
        self.data = [row[:] for row in data]

    def get_dimensions(self):
        """Returns (rows, cols) of the matrix."""
        return self.rows, self.cols

    def __getitem__(self, row_index):
        """
        Enables access using matrix[row_index].
        Returns the specified row as a list.
        """
        if not isinstance(row_index, int):
            raise TypeError("Row index must be an integer.")
        if not (0 <= row_index < self.rows):
            raise IndexError("Row index out of bounds.")
        return self.data[row_index]

    def __setitem__(self, row_index, new_row):
        """
        Enables setting a row using matrix[row_index] = new_row.
        new_row: A list representing the new row. Must have correct length.
        """
        if not isinstance(row_index, int):
            raise TypeError("Row index must be an integer.")
        if not (0 <= row_index < self.rows):
            raise IndexError("Row index out of bounds.")
        if not isinstance(new_row, list) or len(new_row) != self.cols:
            raise ValueError(f"New row must be a list of length {self.cols}.")
        self.data[row_index] = new_row[:]  # Deep copy the new row

    def __str__(self):
        """Returns a string representation of the matrix."""
        if not self.data:
            return "[]"
        s = []
        for row in self.data:
            s.append("\t".join(map(str, row)))
        return "\n".join(s)

    def __repr__(self):
        """Returns a developer-friendly representation."""
        return f"Matrix({self.data})"

    def __eq__(self, other):
        """Compares two matrices for equality."""
        if not isinstance(other, Matrix):
            return NotImplemented
        return (
            self.get_dimensions() == other.get_dimensions() and self.data == other.data
        )

    def __add__(self, other):
        """
        Defines matrix addition (self + other).
        Adds two matrices element-wise.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only add a Matrix object to a Matrix object.")

        if self.get_dimensions() != other.get_dimensions():
            raise ValueError("Matrices must have the same dimensions for addition.")

        result_data = []
        for r in range(self.rows):
            new_row = []
            for c in range(self.cols):
                new_row.append(self.data[r][c] + other.data[r][c])
            result_data.append(new_row)
        return Matrix(result_data)

    def __sub__(self, other):
        """
        Defines matrix subtraction (self - other).
        Subtracts two matrices element-wise.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract a Matrix object from a Matrix object.")

        if self.get_dimensions() != other.get_dimensions():
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result_data = []
        for r in range(self.rows):
            new_row = []
            for c in range(self.cols):
                new_row.append(self.data[r][c] - other.data[r][c])
            result_data.append(new_row)
        return Matrix(result_data)

    def __mul__(self, other):
        """
        Defines matrix multiplication (self * other).
        Supports scalar multiplication (Matrix * scalar) and
        standard matrix multiplication (Matrix * Matrix).
        """
        if isinstance(other, (int, float)):
            # Scalar multiplication
            result_data = []
            for r in range(self.rows):
                new_row = []
                for c in range(self.cols):
                    new_row.append(self.data[r][c] * other)
                result_data.append(new_row)
            return Matrix(result_data)
        elif isinstance(other, Matrix):
            # Standard Matrix multiplication
            if self.cols != other.rows:
                raise ValueError(
                    f"Number of columns in the first matrix ({self.cols}) "
                    f"must equal number of rows in the second matrix ({other.rows}) "
                    "for multiplication."
                )

            result_data = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result_data[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(result_data)
        else:
            raise TypeError(
                "Unsupported operand type for multiplication. "
                "Can only multiply by a scalar (int/float) or another Matrix object."
            )

    def __rmul__(self, other):
        """
        Defines reverse multiplication (scalar * Matrix).
        Allows scalar to be on the left side of the multiplication.
        """
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        else:
            return NotImplemented  # Let Python try other.mul(self)


# You can add basic tests here if matrix.py is run directly
if __name__ == "__main__":
    print("Running basic tests for Matrix class in matrix.py:")
    m_test1 = Matrix([[1, 2], [3, 4]])
    m_test2 = Matrix([[5, 6], [7, 8]])
    print(f"m_test1:\n{m_test1}")
    print(f"m_test2:\n{m_test2}")
    print(f"m_test1 + m_test2:\n{m_test1 + m_test2}")
    print(f"m_test1 * m_test2 (standard):\n{m_test1 * m_test2}")
    print(f"m_test1[0][1]: {m_test1[0][1]}")
    m_test1[0][1] = 99
    print(f"m_test1 after m_test1[0][1] = 99:\n{m_test1}")
