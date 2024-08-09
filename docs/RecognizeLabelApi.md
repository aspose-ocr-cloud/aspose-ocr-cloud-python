# aspose_ocr_cloud.RecognizeLabelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_label**](RecognizeLabelApi.md#cancel_recognize_label) | **DELETE** /v5.0/ocr/RecognizeLabel | CancelRecognizeLabel
[**get_recognize_label**](RecognizeLabelApi.md#get_recognize_label) | **GET** /v5.0/ocr/RecognizeLabel | GetRecognizeLabel
[**post_recognize_label**](RecognizeLabelApi.md#post_recognize_label) | **POST** /v5.0/ocr/RecognizeLabel | PostRecognizeLabel


# **cancel_recognize_label**
> cancel_recognize_label(id)

CancelRecognizeLabel

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
    api_instance = aspose_ocr_cloud.RecognizeLabelApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelRecognizeLabel
        api_instance.cancel_recognize_label(id)
    except Exception as e:
        print("Exception when calling RecognizeLabelApi->cancel_recognize_label: %s\n" % e)
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

# **get_recognize_label**
> OCRResponse get_recognize_label(id)

GetRecognizeLabel

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
    api_instance = aspose_ocr_cloud.RecognizeLabelApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetRecognizeLabel
        api_response = api_instance.get_recognize_label(id)
        print("The response of RecognizeLabelApi->get_recognize_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeLabelApi->get_recognize_label: %s\n" % e)
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

# **post_recognize_label**
> str post_recognize_label(ocr_recognize_label_body)

PostRecognizeLabel

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_label_body import OCRRecognizeLabelBody
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
    api_instance = aspose_ocr_cloud.RecognizeLabelApi(api_client)
    ocr_recognize_label_body = aspose_ocr_cloud.OCRRecognizeLabelBody() # OCRRecognizeLabelBody | 

    try:
        # PostRecognizeLabel
        api_response = api_instance.post_recognize_label(ocr_recognize_label_body)
        print("The response of RecognizeLabelApi->post_recognize_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeLabelApi->post_recognize_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_label_body** | [**OCRRecognizeLabelBody**](OCRRecognizeLabelBody.md)|  | 

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

