from PIL import Image
import numpy as np


def calculate_gray_cell(row, column):
    """
    Takes a cell in a photo and calculates the average gray value over it. \n
    :rtype: object
    :param row: cell row number.
    :param column: cell column number.
    :return: int gray value.

    >>> calculate_gray_cell(0, 0)
    70
    >>> calculate_gray_cell(5, 14)
    72
    """
    mosaic = pixels_matrix[row:min(row + cell_size, rows_count), column:min(column + cell_size, columns_count)]
    return int((np.sum(mosaic) // 3) // (cell_size ** 2))


def set_gray_in_cell(row, column):
    """
    Sets the gray value to all pixels in a cell. \n
    :param row: cell row number.
    :param column: cell column number.
    """
    mosaic = pixels_matrix[row:min(row + cell_size, rows_count), column:min(column + cell_size, columns_count)]
    np.place(mosaic[:, ], mosaic >= 0, int(gray // gradation) * gradation)


image = Image.open("test-img.jpg")
cell_size = 10
gradation = 255 // 50
pixels_matrix = np.array(image)
rows_count = len(pixels_matrix)
columns_count = len(pixels_matrix[1])

current_row = 0
while current_row < rows_count:
    current_column = 0
    while current_column < columns_count:
        gray = calculate_gray_cell(current_row, current_column)
        set_gray_in_cell(current_row, current_column)
        current_column = current_column + cell_size
    current_row = current_row + cell_size

Image.fromarray(pixels_matrix).save("res.jpg")
