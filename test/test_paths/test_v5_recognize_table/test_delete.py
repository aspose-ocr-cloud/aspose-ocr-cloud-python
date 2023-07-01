# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import aspose_ocr_cloud
from aspose_ocr_cloud.paths.v5_recognize_table import delete  # noqa: E501
from aspose_ocr_cloud import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV5RecognizeTable(ApiTestMixin, unittest.TestCase):
    """
    V5RecognizeTable unit test stubs
        CancelRecognizeTable  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
