# aspose_ocr_cloud.DjVu2PDFApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_dj_vu2_pdf**](DjVu2PDFApi.md#cancel_dj_vu2_pdf) | **DELETE** /v5.0/ocr/DjVu2PDF | CancelDjVu2PDF
[**get_dj_vu2_pdf**](DjVu2PDFApi.md#get_dj_vu2_pdf) | **GET** /v5.0/ocr/DjVu2PDF | GetDjVu2PDF
[**post_dj_vu2_pdf**](DjVu2PDFApi.md#post_dj_vu2_pdf) | **POST** /v5.0/ocr/DjVu2PDF | PostDjVu2PDF


# **cancel_dj_vu2_pdf**
> cancel_dj_vu2_pdf(id)

CancelDjVu2PDF

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aspose_ocr_cloud.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with aspose_ocr_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aspose_ocr_cloud.DjVu2PDFApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelDjVu2PDF
        api_instance.cancel_dj_vu2_pdf(id)
    except Exception as e:
        print("Exception when calling DjVu2PDFApi->cancel_dj_vu2_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dj_vu2_pdf**
> OCRResponse get_dj_vu2_pdf(id)

GetDjVu2PDF

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_response import OCRResponse
from aspose_ocr_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aspose_ocr_cloud.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with aspose_ocr_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aspose_ocr_cloud.DjVu2PDFApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetDjVu2PDF
        api_response = api_instance.get_dj_vu2_pdf(id)
        print("The response of DjVu2PDFApi->get_dj_vu2_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DjVu2PDFApi->get_dj_vu2_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task id to select the result | 

### Return type

[**OCRResponse**](OCRResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dj_vu2_pdf**
> str post_dj_vu2_pdf(ocrdj_vu2_pdf_body)

PostDjVu2PDF

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocrdj_vu2_pdf_body import OCRDjVu2PDFBody
from aspose_ocr_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aspose_ocr_cloud.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with aspose_ocr_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aspose_ocr_cloud.DjVu2PDFApi(api_client)
    ocrdj_vu2_pdf_body = aspose_ocr_cloud.OCRDjVu2PDFBody() # OCRDjVu2PDFBody | 

    try:
        # PostDjVu2PDF
        api_response = api_instance.post_dj_vu2_pdf(ocrdj_vu2_pdf_body)
        print("The response of DjVu2PDFApi->post_dj_vu2_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DjVu2PDFApi->post_dj_vu2_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrdj_vu2_pdf_body** | [**OCRDjVu2PDFBody**](OCRDjVu2PDFBody.md)|  | 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

