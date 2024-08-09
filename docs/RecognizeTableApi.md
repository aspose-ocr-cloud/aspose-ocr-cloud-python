# aspose_ocr_cloud.RecognizeTableApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_table**](RecognizeTableApi.md#cancel_recognize_table) | **DELETE** /v5.0/ocr/RecognizeTable | CancelRecognizeTable
[**get_recognize_table**](RecognizeTableApi.md#get_recognize_table) | **GET** /v5.0/ocr/RecognizeTable | GetRecognizeTable
[**post_recognize_table**](RecognizeTableApi.md#post_recognize_table) | **POST** /v5.0/ocr/RecognizeTable | PostRecognizeTable


# **cancel_recognize_table**
> cancel_recognize_table(id)

CancelRecognizeTable

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
    api_instance = aspose_ocr_cloud.RecognizeTableApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelRecognizeTable
        api_instance.cancel_recognize_table(id)
    except Exception as e:
        print("Exception when calling RecognizeTableApi->cancel_recognize_table: %s\n" % e)
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

# **get_recognize_table**
> OCRResponse get_recognize_table(id)

GetRecognizeTable

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
    api_instance = aspose_ocr_cloud.RecognizeTableApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetRecognizeTable
        api_response = api_instance.get_recognize_table(id)
        print("The response of RecognizeTableApi->get_recognize_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeTableApi->get_recognize_table: %s\n" % e)
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

# **post_recognize_table**
> str post_recognize_table(ocr_recognize_table_body)

PostRecognizeTable

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_table_body import OCRRecognizeTableBody
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
    api_instance = aspose_ocr_cloud.RecognizeTableApi(api_client)
    ocr_recognize_table_body = aspose_ocr_cloud.OCRRecognizeTableBody() # OCRRecognizeTableBody | 

    try:
        # PostRecognizeTable
        api_response = api_instance.post_recognize_table(ocr_recognize_table_body)
        print("The response of RecognizeTableApi->post_recognize_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeTableApi->post_recognize_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_table_body** | [**OCRRecognizeTableBody**](OCRRecognizeTableBody.md)|  | 

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
**200** | Task unique ID |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

