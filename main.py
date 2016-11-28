from cell import Cell

FIRST_ROW = [Cell(0, 0, 0, 10), Cell(0, 1, 0, 1.05), Cell(0, 2, 0, 1)]
SECOND_ROW = [Cell(1, 0, 0, 1.05), Cell(1, 1, 0, 1.5), Cell(1, 2, 0, 2)]
THIRD_ROW = [Cell(2, 0, 0, 3), Cell(2, 1, 0, 3), Cell(2, 2, 0, 3)]

MATRIX = [FIRST_ROW, SECOND_ROW, THIRD_ROW]

def main():
    examples= [
        MATRIX[0][0],
        MATRIX[0][1],
        MATRIX[0][2]
    ]
    examples[0].drain_water(MATRIX)
    examples[1].drain_water(MATRIX)
    # for example in examples:
    #     example.drain_water(MATRIX)
    #     print MATRIX, "\n\n"

if __name__ == "__main__":
    main()