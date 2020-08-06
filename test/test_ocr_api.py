# coding: utf-8

# """
# --------------------------------------------------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_ocr_api.py">
#    Copyright (c) 2019 Aspose.OCR for Cloud
#  </copyright>
#  <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

from __future__ import absolute_import

import os
import unittest

import asposeocrcloud.models
from asposeocrcloud.models import OCRRect, OCRRegion, OCRRequestData, OCRRequestDataStorage, LanguageGroup
from asposeocrcloud.rest import ApiException
from test.test_helper import TestHelper


class TestOcrApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.ocr
        cls.storageApi = TestHelper.storage

    ###############################################################
    #                          Simple
    ###############################################################

    def test_post_recognize_from_url(self):
        url = "https://upload.wikimedia.org/wikipedia/commons/2/2f/Book_of_Abraham_FirstPage.png"
        try:

            res = self.api.post_recognize_from_url(url)  # type: asposeocrcloud.models.OcrResponse
            self.assertTrue(isinstance(res, asposeocrcloud.models.OcrResponse), "Error recognize image from URL")
            print(res.text)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_recognize_from_content(self):
        file_name = "5.png"
        src = os.path.join(TestHelper.get_local_folder(), file_name)
        try:

            res = self.api.post_recognize_from_content(src)  # type: asposeocrcloud.models.OcrResponse
            self.assertTrue(isinstance(res, asposeocrcloud.models.OcrResponse), "Error recognize image from Content")
            print(res.text)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_recognize_from_storage(self):
        file_name = "5.png"
        src = os.path.join(TestHelper.get_local_folder(), file_name)
        dst = "5.png"
        result = self.storageApi.upload_file(dst, src)
        self.assertTrue(len(result.uploaded) == 1)
        self.assertTrue(len(result.errors) == 0)

        try:
            res = self.api.get_recognize_from_storage(file_name)  # type: asposeocrcloud.models.OcrResponse
            self.assertTrue(isinstance(res, asposeocrcloud.models.OcrResponse),
                            "Error recognize image from Content")
            print(res.text)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    ###############################################################
    #                          Regions
    ###############################################################

    def test_post_recognize_regions_from_url(self):
        url = "https://iili.io/JP2HFf.png"
        regions = [
            OCRRegion(OCRRect(243, 308, 2095, 964), 0),
            OCRRegion(OCRRect(240, 1045, 2108, 1826), 1),
            OCRRegion(OCRRect(237, 1916, 2083, 3180), 2)
        ]
        request_data = OCRRequestData(regions, LanguageGroup.ENGLISH, False)
        try:
            res = self.api.post_recognize_regions_from_url(request_data, url)  # type: asposeocrcloud.models.OcrResponse
            self.assertTrue(isinstance(res, asposeocrcloud.models.OcrResponse),
                            "Error recognize image regions from Url")
            print(res.text)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_recognize_regions_from_storage(self):
        # Upload image file to Aspose Storage
        file_name = "5.png"
        src = os.path.join(TestHelper.get_local_folder(), file_name)
        dst = "5.png"
        result = self.storageApi.upload_file(dst, src)
        self.assertTrue(len(result.uploaded) == 1)
        self.assertTrue(len(result.errors) == 0)

        regions = [
            OCRRegion(OCRRect(243, 308, 2095, 964), 0),
            OCRRegion(OCRRect(240, 1045, 2108, 1826), 1),
            OCRRegion(OCRRect(237, 1916, 2083, 3180), 2),
        ]
        request_data = OCRRequestDataStorage(regions, LanguageGroup.ENGLISH, False,
                                             file_name)  # OCRRequestData(regions, 1, False)
        try:
            res = self.api.post_recognize_regions_from_storage(request_data)  # type: asposeocrcloud.models.OcrResponse
            self.assertTrue(isinstance(res, asposeocrcloud.models.OcrResponse),
                            "Error recognize image regions from Storage")
            print(res.text)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_recognize_regions_from_content(self):
        file_name = "5.png"
        src = os.path.join(TestHelper.get_local_folder(), file_name)
        regions = [
            OCRRegion(OCRRect(243, 308, 2095, 964), 0),
            OCRRegion(OCRRect(240, 1045, 2108, 1826), 1),
            OCRRegion(OCRRect(237, 1916, 2083, 3180), 2),
        ]

        request_data = OCRRequestData(regions, LanguageGroup.FRENCH, False)
        try:
            res = self.api.post_recognize_regions_from_content(request_data,
                                                               src)  # type: asposeocrcloud.models.OcrResponse
            self.assertTrue(isinstance(res, asposeocrcloud.models.OcrResponse),
                            "Error recognize image regions from Storage")
            print(res.text)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
