# aspose_ocr_cloud.IdentifyFontApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_identify_font**](IdentifyFontApi.md#cancel_identify_font) | **DELETE** /v5.0/ocr/IdentifyFont | CancelIdentifyFont
[**get_identify_font**](IdentifyFontApi.md#get_identify_font) | **GET** /v5.0/ocr/IdentifyFont | GetIdentifyFont
[**post_identify_font**](IdentifyFontApi.md#post_identify_font) | **POST** /v5.0/ocr/IdentifyFont | PostIdentifyFont


# **cancel_identify_font**
> cancel_identify_font(id)

CancelIdentifyFont

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
    api_instance = aspose_ocr_cloud.IdentifyFontApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelIdentifyFont
        api_instance.cancel_identify_font(id)
    except Exception as e:
        print("Exception when calling IdentifyFontApi->cancel_identify_font: %s\n" % e)
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

# **get_identify_font**
> OCRResponse get_identify_font(id)

GetIdentifyFont

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
    api_instance = aspose_ocr_cloud.IdentifyFontApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetIdentifyFont
        api_response = api_instance.get_identify_font(id)
        print("The response of IdentifyFontApi->get_identify_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentifyFontApi->get_identify_font: %s\n" % e)
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

# **post_identify_font**
> str post_identify_font(ocr_recognize_font_body)

PostIdentifyFont

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_font_body import OCRRecognizeFontBody
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
    api_instance = aspose_ocr_cloud.IdentifyFontApi(api_client)
    ocr_recognize_font_body = aspose_ocr_cloud.OCRRecognizeFontBody() # OCRRecognizeFontBody | 

    try:
        # PostIdentifyFont
        api_response = api_instance.post_identify_font(ocr_recognize_font_body)
        print("The response of IdentifyFontApi->post_identify_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentifyFontApi->post_identify_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_font_body** | [**OCRRecognizeFontBody**](OCRRecognizeFontBody.md)|  | 

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

