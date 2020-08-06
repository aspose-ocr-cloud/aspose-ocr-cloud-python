# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="ocr_rect.py">
# Copyright (c) 2019 Aspose.OCR for Cloud
# </copyright>
# <summary>
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

"""
 * Represents a rectangle: Left-Top (X1-Y1) to Right-Bottom (X2-Y2)
"""


class OCRRect:
    """
        Attributes:
          model_types (dict):   The key is attribute name
                                and the value is attribute type.
          attribute_map (dict): The key is attribute name
                                and the value is json key in definition.
        """
    model_types = {
        'TopLeftX': 'int',
        'TopLeftY': 'int',
        'BottomRightX': 'int',
        'BottomRightY': 'int'
    }

    attribute_map = {
        'TopLeftX': 'TopLeftX',
        'TopLeftY': 'TopLeftY',
        'BottomRightX': 'BottomRightX',
        'BottomRightY': 'BottomRightY'
    }

    def __init__(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        """
        :param int topLeftX: X-Coordinate of top left corner
        :param int topLeftY: Y-Coordinate of top left corner
        :param int bottomRightX: X-Coordinate of bottom right corner
        :param int bottomRightY: Y-Coordinate of bottom right corner
        """
        self.TopLeftX = topLeftX            # X-Coordinate of top left corner
        self.TopLeftY = topLeftY            # Y-Coordinate of top left corner
        self.BottomRightX = bottomRightX    # X-Coordinate of bottom right corner
        self.BottomRightY = bottomRightY    # Y-Coordinate of bottom right corner

    def to_array(self):
        return [self.TopLeftX, self.TopLeftY, self.BottomRightX, self.BottomRightY]
