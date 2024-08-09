# aspose_ocr_cloud.RecognizeRegionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_regions**](RecognizeRegionsApi.md#cancel_recognize_regions) | **DELETE** /v5.0/ocr/RecognizeRegions | CancelRecognizeRegions
[**get_recognize_regions**](RecognizeRegionsApi.md#get_recognize_regions) | **GET** /v5.0/ocr/RecognizeRegions | GetRecognizeRegions
[**post_recognize_regions**](RecognizeRegionsApi.md#post_recognize_regions) | **POST** /v5.0/ocr/RecognizeRegions | PostRecognizeRegions


# **cancel_recognize_regions**
> cancel_recognize_regions(id)

CancelRecognizeRegions

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
    api_instance = aspose_ocr_cloud.RecognizeRegionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelRecognizeRegions
        api_instance.cancel_recognize_regions(id)
    except Exception as e:
        print("Exception when calling RecognizeRegionsApi->cancel_recognize_regions: %s\n" % e)
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

# **get_recognize_regions**
> OCRResponse get_recognize_regions(id)

GetRecognizeRegions

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
    api_instance = aspose_ocr_cloud.RecognizeRegionsApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetRecognizeRegions
        api_response = api_instance.get_recognize_regions(id)
        print("The response of RecognizeRegionsApi->get_recognize_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeRegionsApi->get_recognize_regions: %s\n" % e)
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

# **post_recognize_regions**
> str post_recognize_regions(ocr_recognize_regions_body)

PostRecognizeRegions

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_regions_body import OCRRecognizeRegionsBody
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
    api_instance = aspose_ocr_cloud.RecognizeRegionsApi(api_client)
    ocr_recognize_regions_body = aspose_ocr_cloud.OCRRecognizeRegionsBody() # OCRRecognizeRegionsBody | 

    try:
        # PostRecognizeRegions
        api_response = api_instance.post_recognize_regions(ocr_recognize_regions_body)
        print("The response of RecognizeRegionsApi->post_recognize_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeRegionsApi->post_recognize_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_regions_body** | [**OCRRecognizeRegionsBody**](OCRRecognizeRegionsBody.md)|  | 

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

