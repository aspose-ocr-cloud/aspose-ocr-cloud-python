# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="ocr_request_data_storage.py">
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

import six
from typing import List

from asposeocrcloud.models.language_group import LanguageGroup
from asposeocrcloud.models.ocr_region import OCRRegion
from asposeocrcloud.models.ocr_request_data import OCRRequestData

"""
* Request data to recognize specific regions on image.
"""


class OCRRequestDataStorage(OCRRequestData):
    """
        Attributes:
          model_types (dict):   The key is attribute name
                                and the value is attribute type.
          attribute_map (dict): The key is attribute name
                                and the value is json key in definition.
        """
    model_types = {
        'Regions': 'OCRRegion',
        'Language': 'Language',
        'MakeSkewCorrect': 'bool',
        'FileName': 'str',
        'Storage': 'str',
        "Folder": 'str'
    }

    attribute_map = {
        'Regions': 'Regions',
        'Language': 'Language',
        'MakeSkewCorrect': 'MakeSkewCorrect',
        'FileName': 'FileName',
        'Storage': 'Storage',
        "Folder": 'Folder'
    }

    def __init__(self, regions, language, make_skew_correct, file_name, folder="", storage=""):
        """
        :param List[OCRRegion] regions: Region on image to recognize in specific format. OCRRegion
        :param LanguageGroup language: Recognition language. English by default.
        :param bool make_skew_correct: Option to enable skew correction algorithm. False bt default
        :param str file_name: File name in Aspose.Storage
        :param str folder: Folder name in Aspose.Storage
        :param str storage: Your storage name (configured in Aspose.Dashboard) Usually is empty if you have only one storage
        """
        OCRRequestData.__init__(self, regions, language, make_skew_correct)
        # super().__init__(regions, language, make_skew_correct)
        self.FileName = file_name
        self.Storage = storage
        self.Folder = folder
