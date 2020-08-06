# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="ocr_response.py">
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

from asposeocrcloud.models import BaseModel


class OcrResponse(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'code': 'int',
        'text': 'str'
    }

    attribute_map = {
        'code': 'code',
        'text': 'text'
    }

    def __init__(self, code=-1, text="None"):
        """

        :type text: str
        :type code: int
        """
        self._code = code  # type: int
        self._text = text  # type: str

    @property
    def code(self):
        """Operation status code
        :return: Operation status code.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Operation status code
        :param code: Operation status code.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def text(self):
        """Gets the The text from Image.
        Recognized Text
        :return: The text from Image.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets text from Image.
        Recognized Text
        :param text: The text from Image.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text
