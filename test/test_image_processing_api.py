# coding: utf-8

"""
    Aspose OCR Cloud 5.0 API

    Aspose OCR Cloud 5.0 API  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import absolute_import

import unittest

import aspose_ocr_cloud
from aspose_ocr_cloud.api.image_processing_api import ImageProcessingApi  # noqa: E501
from aspose_ocr_cloud.rest import ApiException


class TestImageProcessingApi(unittest.TestCase):
    """ImageProcessingApi unit test stubs"""

    def setUp(self):
        self.api = aspose_ocr_cloud.api.image_processing_api.ImageProcessingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_result_file(self):
        """Test case for get_result_file

        GetResultFile  # noqa: E501
        """
        pass

    def test_get_result_task(self):
        """Test case for get_result_task

        GetResultTask  # noqa: E501
        """
        pass

    def test_post_binarization_file(self):
        """Test case for post_binarization_file

        PostBinarizationFile  # noqa: E501
        """
        pass

    def test_post_dewarping_file(self):
        """Test case for post_dewarping_file

        PostDewarpingFile  # noqa: E501
        """
        pass

    def test_post_skew_correction_file(self):
        """Test case for post_skew_correction_file

        PostSkewCorrectionFile  # noqa: E501
        """
        pass

    def test_post_upsampling_file(self):
        """Test case for post_upsampling_file

        PostUpsamplingImageFile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
