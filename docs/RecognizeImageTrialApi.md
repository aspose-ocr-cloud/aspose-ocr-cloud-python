# aspose_ocr_cloud.RecognizeImageTrialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_image_trial**](RecognizeImageTrialApi.md#cancel_recognize_image_trial) | **DELETE** /v5.0/ocr/RecognizeImageTrial | CancelRecognizeImageTrial
[**get_recognize_image_trial**](RecognizeImageTrialApi.md#get_recognize_image_trial) | **GET** /v5.0/ocr/RecognizeImageTrial | GetRecognizeImageTrial
[**post_recognize_image_trial**](RecognizeImageTrialApi.md#post_recognize_image_trial) | **POST** /v5.0/ocr/RecognizeImageTrial | PostRecognizeImageTrial


# **cancel_recognize_image_trial**
> cancel_recognize_image_trial(id)

CancelRecognizeImageTrial

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
    api_instance = aspose_ocr_cloud.RecognizeImageTrialApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelRecognizeImageTrial
        api_instance.cancel_recognize_image_trial(id)
    except Exception as e:
        print("Exception when calling RecognizeImageTrialApi->cancel_recognize_image_trial: %s\n" % e)
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

# **get_recognize_image_trial**
> OCRResponse get_recognize_image_trial(id)

GetRecognizeImageTrial

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
    api_instance = aspose_ocr_cloud.RecognizeImageTrialApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetRecognizeImageTrial
        api_response = api_instance.get_recognize_image_trial(id)
        print("The response of RecognizeImageTrialApi->get_recognize_image_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeImageTrialApi->get_recognize_image_trial: %s\n" % e)
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

# **post_recognize_image_trial**
> str post_recognize_image_trial(ocr_recognize_image_body)

PostRecognizeImageTrial

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_image_body import OCRRecognizeImageBody
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
    api_instance = aspose_ocr_cloud.RecognizeImageTrialApi(api_client)
    ocr_recognize_image_body = aspose_ocr_cloud.OCRRecognizeImageBody() # OCRRecognizeImageBody | 

    try:
        # PostRecognizeImageTrial
        api_response = api_instance.post_recognize_image_trial(ocr_recognize_image_body)
        print("The response of RecognizeImageTrialApi->post_recognize_image_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeImageTrialApi->post_recognize_image_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_image_body** | [**OCRRecognizeImageBody**](OCRRecognizeImageBody.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

