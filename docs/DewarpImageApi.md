# aspose_ocr_cloud.DewarpImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_dewarp_image**](DewarpImageApi.md#cancel_dewarp_image) | **DELETE** /v5.0/ocr/DewarpImage | CancelDewarpImage
[**get_dewarp_image**](DewarpImageApi.md#get_dewarp_image) | **GET** /v5.0/ocr/DewarpImage | GetDewarpImage
[**post_dewarp_image**](DewarpImageApi.md#post_dewarp_image) | **POST** /v5.0/ocr/DewarpImage | PostDewarpImage


# **cancel_dewarp_image**
> cancel_dewarp_image(id)

CancelDewarpImage

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
    api_instance = aspose_ocr_cloud.DewarpImageApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelDewarpImage
        api_instance.cancel_dewarp_image(id)
    except Exception as e:
        print("Exception when calling DewarpImageApi->cancel_dewarp_image: %s\n" % e)
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

# **get_dewarp_image**
> OCRResponse get_dewarp_image(id)

GetDewarpImage

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
    api_instance = aspose_ocr_cloud.DewarpImageApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetDewarpImage
        api_response = api_instance.get_dewarp_image(id)
        print("The response of DewarpImageApi->get_dewarp_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DewarpImageApi->get_dewarp_image: %s\n" % e)
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

# **post_dewarp_image**
> str post_dewarp_image(ocr_dewarp_image_body)

PostDewarpImage

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_dewarp_image_body import OCRDewarpImageBody
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
    api_instance = aspose_ocr_cloud.DewarpImageApi(api_client)
    ocr_dewarp_image_body = aspose_ocr_cloud.OCRDewarpImageBody() # OCRDewarpImageBody | 

    try:
        # PostDewarpImage
        api_response = api_instance.post_dewarp_image(ocr_dewarp_image_body)
        print("The response of DewarpImageApi->post_dewarp_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DewarpImageApi->post_dewarp_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_dewarp_image_body** | [**OCRDewarpImageBody**](OCRDewarpImageBody.md)|  | 

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

