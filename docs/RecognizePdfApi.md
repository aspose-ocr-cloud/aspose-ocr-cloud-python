# aspose_ocr_cloud.RecognizePdfApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_pdf**](RecognizePdfApi.md#cancel_recognize_pdf) | **DELETE** /v5.0/ocr/RecognizePdf | CancelRecognizePdf
[**get_recognize_pdf**](RecognizePdfApi.md#get_recognize_pdf) | **GET** /v5.0/ocr/RecognizePdf | GetRecognizePdf
[**post_recognize_pdf**](RecognizePdfApi.md#post_recognize_pdf) | **POST** /v5.0/ocr/RecognizePdf | PostRecognizePdf


# **cancel_recognize_pdf**
> cancel_recognize_pdf(id)

CancelRecognizePdf

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
    api_instance = aspose_ocr_cloud.RecognizePdfApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelRecognizePdf
        api_instance.cancel_recognize_pdf(id)
    except Exception as e:
        print("Exception when calling RecognizePdfApi->cancel_recognize_pdf: %s\n" % e)
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

# **get_recognize_pdf**
> OCRResponse get_recognize_pdf(id)

GetRecognizePdf

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
    api_instance = aspose_ocr_cloud.RecognizePdfApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetRecognizePdf
        api_response = api_instance.get_recognize_pdf(id)
        print("The response of RecognizePdfApi->get_recognize_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizePdfApi->get_recognize_pdf: %s\n" % e)
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

# **post_recognize_pdf**
> str post_recognize_pdf(ocr_recognize_pdf_body)

PostRecognizePdf

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_pdf_body import OCRRecognizePdfBody
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
    api_instance = aspose_ocr_cloud.RecognizePdfApi(api_client)
    ocr_recognize_pdf_body = aspose_ocr_cloud.OCRRecognizePdfBody() # OCRRecognizePdfBody | 

    try:
        # PostRecognizePdf
        api_response = api_instance.post_recognize_pdf(ocr_recognize_pdf_body)
        print("The response of RecognizePdfApi->post_recognize_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizePdfApi->post_recognize_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_pdf_body** | [**OCRRecognizePdfBody**](OCRRecognizePdfBody.md)|  | 

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

