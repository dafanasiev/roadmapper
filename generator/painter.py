# Painter class - Wrapper for PyCairo library
# MIT License

# Copyright (c) 2022 Cheng Soon Goh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cairo
from colour import Color


class Painter:
    __VSPACER, __HSPACER = 12, 2
    width = 0
    height = 0
    last_drawn_y_pos = 0

    left_margin = 20
    right_margin = 20
    group_box_width_percentage = 0.2
    timeline_width_percentage = 1 - group_box_width_percentage
    gap_between_group_box_and_timeline = 20
    gap_between_timeline_and_title = 20

    timeline_height = 20

    # initialise code
    def __init__(self, width, height, output_file_name):
        self.width = width
        self.height = height
        self.last_drawn_y_pos = 0
        if output_file_name == "":
            output_file_name = "roadmap"

        if output_file_name.split(".")[-1].upper() == "PNG":
            output_type = "PNG"
        elif output_file_name.split(".")[-1].upper() == "PDF":
            output_type = "PDF"
        else:
            # Default file format
            output_type = "PNG"
            output_file_name.join(".png")

        if output_type == "PNG":
            self.__surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        if output_type == "PDF":
            self.__surface = cairo.PDFSurface(output_file_name, width, height)

        self.__cr = cairo.Context(self.__surface)
        self.__output_type = output_type
        self.__output_file_name = output_file_name

    def set_colour(self, colour):
        c = Color(colour)
        self.__cr.set_source_rgb(*c.get_rgb())

    def set_font(self, font, font_size, font_colour):
        self.__cr.select_font_face(font)
        self.__cr.set_font_size(font_size)
        self.set_colour(font_colour)

    def draw_box(self, x, y, width, height):
        # print(f"Drawing box at {x}, {y} with width {width} and height {height}")
        self.__cr.rectangle(x, y, width, height)
        self.__cr.fill()

    def draw_box_with_text(
        self,
        x,
        y,
        width,
        height,
        text,
        text_alignment: str,
        font_colour: str,
        fill_colour: str,
    ):
        self.set_colour(fill_colour)
        self.__cr.rectangle(x, y, width, height)
        self.__cr.fill()
        self.set_colour(font_colour)
        text_x, text_y = self.get_display_text_position(
            x, y, width, height, text, text_alignment
        )
        self.draw_text(text_x, text_y, text)

    def draw_diamond(self, x, y, width, height):
        self.__cr.set_source_rgb(1, 0, 0)
        self.__cr.move_to(x + width / 2, y)
        self.__cr.line_to(x + width, y + height / 2)
        self.__cr.line_to(x + width / 2, y + height)
        self.__cr.line_to(x, y + height / 2)
        self.__cr.close_path()
        self.__cr.fill()

    def draw_text(self, x, y, text):
        self.__cr.move_to(x, y)
        self.__cr.show_text(text)

    def get_text_dimension(self, text):
        (
            _,
            _,
            text_width,
            text_height,
            _,
            _,
        ) = self.__cr.text_extents(text)
        return text_width, text_height

    def set_background_colour(self, colour):
        self.set_colour(colour)
        self.__cr.paint()

    def get_display_text_position(self, x, y, width, height, text, alignment):
        ### to remove
        # self.set_colour("yellow")
        # self.draw_box(x, y, width, height)
        text_width, text_height = self.get_text_dimension(text)

        if alignment == "centre":
            text_x_pos = (width / 2) - (text_width / 2)
        elif alignment == "right":
            text_x_pos = width - text_width
        elif alignment == "left":
            text_x_pos = x + 10

        text_y_pos = (height / 2) + (text_height / 2)

        return x + text_x_pos, y + text_y_pos

    def save_surface(self):
        if self.__output_type == "PNG":
            self.__surface.write_to_png(self.__output_file_name)
        if self.__output_type == "PDF":
            self.__surface.show_page()