# aspose_ocr_cloud.BinarizeImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_binarize_image**](BinarizeImageApi.md#cancel_binarize_image) | **DELETE** /v5.0/ocr/BinarizeImage | CancelBinarizeImage
[**get_binarize_image**](BinarizeImageApi.md#get_binarize_image) | **GET** /v5.0/ocr/BinarizeImage | GetBinarizeImage
[**post_binarize_image**](BinarizeImageApi.md#post_binarize_image) | **POST** /v5.0/ocr/BinarizeImage | PostBinarizeImage


# **cancel_binarize_image**
> cancel_binarize_image(id)

CancelBinarizeImage

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
    api_instance = aspose_ocr_cloud.BinarizeImageApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelBinarizeImage
        api_instance.cancel_binarize_image(id)
    except Exception as e:
        print("Exception when calling BinarizeImageApi->cancel_binarize_image: %s\n" % e)
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

# **get_binarize_image**
> OCRResponse get_binarize_image(id)

GetBinarizeImage

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
    api_instance = aspose_ocr_cloud.BinarizeImageApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetBinarizeImage
        api_response = api_instance.get_binarize_image(id)
        print("The response of BinarizeImageApi->get_binarize_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinarizeImageApi->get_binarize_image: %s\n" % e)
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

# **post_binarize_image**
> str post_binarize_image(ocr_binarize_image_body)

PostBinarizeImage

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_binarize_image_body import OCRBinarizeImageBody
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
    api_instance = aspose_ocr_cloud.BinarizeImageApi(api_client)
    ocr_binarize_image_body = aspose_ocr_cloud.OCRBinarizeImageBody() # OCRBinarizeImageBody | 

    try:
        # PostBinarizeImage
        api_response = api_instance.post_binarize_image(ocr_binarize_image_body)
        print("The response of BinarizeImageApi->post_binarize_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinarizeImageApi->post_binarize_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_binarize_image_body** | [**OCRBinarizeImageBody**](OCRBinarizeImageBody.md)|  | 

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

