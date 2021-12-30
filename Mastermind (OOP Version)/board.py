class Board:
    def __init__(self):
        self.__solution = []
        self.__attempt_num = 1
        self.__row_dict = {"ans": self.__solution,
                           1: Row(0, 0, 0),
                           2: Row(0, 0, 0),
                           3: Row(0, 0, 0),
                           4: Row(0, 0, 0),
                           5: Row(0, 0, 0),
                           6: Row(0, 0, 0),
                           7: Row(0, 0, 0),
                           8: Row(0, 0, 0),
                           9: Row(0, 0, 0)}

    def __str__(self):
        return f"attempt 1: {self.__row_dict[1]} \n" \
               f"attempt 2: {self.__row_dict[2]} \n" \
               f"attempt 3: {self.__row_dict[3]} \n" \
               f"attempt 4: {self.__row_dict[4]} \n" \
               f"attempt 5: {self.__row_dict[5]} \n" \
               f"attempt 6: {self.__row_dict[6]} \n" \
               f"attempt 7: {self.__row_dict[7]} \n" \
               f"attempt 8: {self.__row_dict[8]} \n" \
               f"attempt 9: {self.__row_dict[9]}"

    def set_row(self, pins, reds, whites):
        for i in range(1, len(self.__row_dict) + 1):
            if self.__row_dict[i].get_pins() == 0:
                self.__row_dict[i] = Row(pins, reds, whites)

    def get_row(self, row_num):
        return self.__row_dict.get(row_num)

    def get_row_num(self, row):
        return self.__row_dict.get(row)


class Row:
    def __init__(self, pins, reds, whites):
        self.__pins = pins
        self.__reds = reds
        self.__whites = whites

    def __str__(self):
        return f"{''.join(self.__pins)} red: {self.__reds} white: {self.__whites}"

    def get_pins(self):
        return self.__pins
