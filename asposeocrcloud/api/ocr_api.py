# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="ocr_api.py">
# Copyright (c) 2019 Aspose.OCR for Cloud
# </copyright>
# <summary>
#
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

from __future__ import absolute_import

from typing import List, Tuple

from asposeocrcloud.models import OCRRect, OCRRegion, OCRRequestData, OCRRequestDataStorage, OcrResponse, LanguageGroup
from asposeocrcloud.api_client import ApiClient

# python 2 and python 3 compatibility library
import six


class OcrApi(object):

    def __init__(self, config=None):
        if config is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(config)
        self.api_client = api_client

    ##########################################################
    #                  OCR Text Page Recognition API
    ##########################################################

    def post_recognize_from_url(self, url, params, **kwargs):
        """  Recognize image text from some url - give us file URL and we will download it and recognize.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str url: WEB URL to image file to recognize
        :return: OCRResponse . If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_recognize_from_url(url, params, **kwargs)
        else:
            (data) = self.__post_recognize_from_url(url, params, **kwargs)
            return data

    def __post_recognize_from_url(self, url, query_params, **kwargs):
        assert url is not None
        """ TBD Recognize image text from some url if provided or from the request body content

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str url: The image file url
        :return: OCRResponse . If the method is called asynchronously, returns the request thread.
        """

        all_params = ['async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}  # uri params #

        url_param = {'url': url}  # content query params
        query_params = query_params.__dict__
        query_params = {**url_param, **query_params}

        header_params = {}
        form_params = {}
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        # header_params['Accept'] = self.api_client.select_header_accept(
        #     ['multipart/form-data'])
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/ocr/recognize', 'POST', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='OcrResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def post_recognize_from_content(self, file_path, query_params, **kwargs):
        """  Recognize image text from content - provide local filepath to send it in Aspose.OCR Cloud directly

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str file_path: Local file path to send on recognition
        :return: OCRResponse . If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_recognize_from_content(file_path, query_params, **kwargs)
        else:
            (data) = self.__post_recognize_from_content(file_path, query_params, **kwargs)
            return data

    def __post_recognize_from_content(self, file_path, query_params, **kwargs):
        assert file_path is not None
        """ Recognize image text from content - provide local filepath to send it in Aspose.OCR Cloud directly

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str file_path: Local file path to send on recognition
        :return: OCRResponse . If the method is called asynchronously, returns the request thread.
        """

        all_params = ['async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}  # uri params #

        query_params = query_params.__dict__
        print(query_params)
        # query_params = {"skewCorrect": False}  # content query params

        header_params = {}
        form_params = {}
        local_var_files = {}
        # local_var_files = {"File": file_path}
        body_params = []

        with open(file_path, 'rb') as f:
            data = f.read()
            body_params = data

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/octet-stream'])

        return self.api_client.call_api('/ocr/recognize', 'POST', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='OcrResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def get_recognize_from_storage(self, query_params, file, folder="", storage="",  **kwargs):
        """  Recognize image text from the Aspose.Storage. Put your file in storage and give us path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param str storage: Optional: Aspose Storage name
        :param str folder: Optional: The directory path, that contains file
        :param str file: The name of file in storage
        :return: OCRResponse . If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_recognize_from_storage(file, folder, storage, query_params, **kwargs)
        else:
            (data) = self.__get_recognize_from_storage(file, folder, storage, query_params, **kwargs)
            return data

    def __get_recognize_from_storage(self, file, folder, storage, query_params, **kwargs):
        assert file is not None
        """ Recognize image text from the Aspose.Storage. Put your file in storage and give us path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str storage: Optional: Aspose Storage name
        :param str folder: Optional: The directory path, that contains file
        :param str file: The name of file in storage
        :return: OCRResponse . If the method is called asynchronously, returns the request thread.
        """

        all_params = ['async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {'name': file}  # uri params #

        storage_params = {'storage': storage,
                          'folder': folder}  # content query params

        query_params = query_params.__dict__
        query_params = {**storage_params, **query_params}

        header_params = {}
        form_params = {}
        local_var_files = {}
        body_params = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/ocr/{name}/recognize', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='OcrResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def post_recognize_regions_from_url(self, request_data, url, **kwargs):
        """Recognize image text from some url - give us file URL and we will download it and recognize.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param str url: WEB URL to image file to recognize
        :param OCRRequestData request_data: Data structure with recognition options
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_recognize_regions_from_url(request_data, url, **kwargs)
        else:
            (data) = self.__post_recognize_regions_from_url(request_data, url, **kwargs)
            return data

    def __post_recognize_regions_from_url(self, request_data, url, **kwargs):
        all_params = ['request_data', 'url', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_merge_ocr_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = {"requestData": request_data, "url": url}
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api('/ocr/recognize-regions-url', 'POST', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='OcrResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        _serialize_if_object=True)

    def post_recognize_regions_from_storage(self, request_data, **kwargs):
        """Recognize recognize specific regions of image located in Aspose.Storage. Put your file in storage and give us path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        :param OCRRequestDataStorage request_data: Data structure with Aspose.Storage file path and recognition options: Language, Regions, Image Corrections
        """

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_recognize_regions_from_storage(request_data, **kwargs)
        else:
            (data) = self.__post_recognize_regions_from_storage(request_data, **kwargs)
            return data

    def __post_recognize_regions_from_storage(self, request_data, **kwargs):
        all_params = ['request_data', 'async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_merge_ocr_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = {"requestData": request_data}
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api('/ocr/recognize-regions-storage', 'POST', path_params, query_params,
                                        header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='OcrResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        _serialize_if_object=True)

    def post_recognize_regions_from_content(self, request_data, file_path, **kwargs):
        """ Recognize recognize specific regions of image - provide local filepath to send it in Aspose.OCR Cloud directly

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        :param str file_path: Local file path to send on recognition
        :param OCRRequestData request_data: Data structure with recognition options: Language, Regions, Image Corrections

        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_recognize_regions_from_content(request_data, file_path, **kwargs)
        else:
            (data) = self.__post_recognize_regions_from_content(request_data, file_path, **kwargs)
            return data

    def __post_recognize_regions_from_content(self, request_data, file_path, **kwargs):
        all_params = ['request_data', 'file_path', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_merge_ocr_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = [("requestData", request_data)]
        body_params = {}
        local_var_files = {"File": file_path}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api('/ocr/recognize-regions-content', 'POST', path_params, query_params,
                                        header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='OcrResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        _serialize_if_object=True)
