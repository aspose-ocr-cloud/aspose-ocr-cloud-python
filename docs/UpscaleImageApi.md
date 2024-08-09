# aspose_ocr_cloud.UpscaleImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_upscale_image**](UpscaleImageApi.md#cancel_upscale_image) | **DELETE** /v5.0/ocr/UpscaleImage | CancelUpscaleImage
[**get_upscale_image**](UpscaleImageApi.md#get_upscale_image) | **GET** /v5.0/ocr/UpscaleImage | GetUpscaleImage
[**post_upscale_image**](UpscaleImageApi.md#post_upscale_image) | **POST** /v5.0/ocr/UpscaleImage | PostUpscaleImage


# **cancel_upscale_image**
> cancel_upscale_image(id)

CancelUpscaleImage

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
    api_instance = aspose_ocr_cloud.UpscaleImageApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelUpscaleImage
        api_instance.cancel_upscale_image(id)
    except Exception as e:
        print("Exception when calling UpscaleImageApi->cancel_upscale_image: %s\n" % e)
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

# **get_upscale_image**
> OCRResponse get_upscale_image(id)

GetUpscaleImage

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
    api_instance = aspose_ocr_cloud.UpscaleImageApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetUpscaleImage
        api_response = api_instance.get_upscale_image(id)
        print("The response of UpscaleImageApi->get_upscale_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpscaleImageApi->get_upscale_image: %s\n" % e)
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

# **post_upscale_image**
> str post_upscale_image(ocr_upscale_image_body)

PostUpscaleImage

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_upscale_image_body import OCRUpscaleImageBody
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
    api_instance = aspose_ocr_cloud.UpscaleImageApi(api_client)
    ocr_upscale_image_body = aspose_ocr_cloud.OCRUpscaleImageBody() # OCRUpscaleImageBody | 

    try:
        # PostUpscaleImage
        api_response = api_instance.post_upscale_image(ocr_upscale_image_body)
        print("The response of UpscaleImageApi->post_upscale_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpscaleImageApi->post_upscale_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_upscale_image_body** | [**OCRUpscaleImageBody**](OCRUpscaleImageBody.md)|  | 

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

