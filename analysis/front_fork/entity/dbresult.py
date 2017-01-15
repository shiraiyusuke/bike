# -*- coding: utf-8 -*-
class DBresult(object):
    def __init__(self, record):
        self.__image_id       = record[0]
        self.__direction      = record[1]
        self.__image_path     = record[2]
        self.__processed      = record[3]
        self.__left_top_x     = record[4]
        self.__left_top_y     = record[5]
        self.__right_top_x    = record[6]
        self.__right_top_y    = record[7]
        self.__left_middle_x  = record[8]
        self.__left_middle_y  = record[9]
        self.__right_middle_x = record[10]
        self.__right_middle_x = record[11]
        self.__left_middle_x  = record[12]
        self.__left_middle_y  = record[13]
        self.__right_middle_x = record[14]
        self.__right_middle_x = record[15]
        self.__update_at      = record[16]

    @property
    def image_id(self):
        return self.__image_id

    @property
    def direction(self):
       return self.__direction

    @property
    def image_path(self):
        return self.__image_path

    @property
    def processed(self):
        return self.__processed

    @property
    def left_top_x(self):
        return self.__left_top_x

    @property
    def left_top_y(self):
        return self.__left_top_y

    @property
    def right_top_x(self):
        return self.__right_top_x

    @property
    def right_top_y(self):
        return self.__right_top_y

    @property
    def left_middle_x(self):
        return self.__left_middle_x

    @property
    def left_middle_y(self):
        return self.__left_middle_y

    @property
    def right_middle_x(self):
        return self.__right_middle_x

    @property
    def right_middle_x(self):
       return self.__right_middle_x

    @property
    def left_middle_x(self):
       return self.__left_middle_x

    @property
    def left_middle_y(self):
       return self.__left_middle_y

    @property
    def right_middle_x(self):
       return self.__right_middle_x

    @property
    def right_middle_x(self):
       return self.__right_middle_x

    @property
    def update_at(self):
       return self.__update_at
