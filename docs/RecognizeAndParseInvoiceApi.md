# aspose_ocr_cloud.RecognizeAndParseInvoiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_and_parse_invoice**](RecognizeAndParseInvoiceApi.md#cancel_recognize_and_parse_invoice) | **DELETE** /v5.0/ocr/RecognizeAndParseInvoice | CancelRecognizeAndParseInvoice
[**get_recognize_and_parse_invoice**](RecognizeAndParseInvoiceApi.md#get_recognize_and_parse_invoice) | **GET** /v5.0/ocr/RecognizeAndParseInvoice | GetRecognizeAndParseInvoice
[**post_recognize_and_parse_invoice**](RecognizeAndParseInvoiceApi.md#post_recognize_and_parse_invoice) | **POST** /v5.0/ocr/RecognizeAndParseInvoice | PostRecognizeAndParseInvoice


# **cancel_recognize_and_parse_invoice**
> cancel_recognize_and_parse_invoice(id)

CancelRecognizeAndParseInvoice

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
    api_instance = aspose_ocr_cloud.RecognizeAndParseInvoiceApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelRecognizeAndParseInvoice
        api_instance.cancel_recognize_and_parse_invoice(id)
    except Exception as e:
        print("Exception when calling RecognizeAndParseInvoiceApi->cancel_recognize_and_parse_invoice: %s\n" % e)
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

# **get_recognize_and_parse_invoice**
> OCRResponse get_recognize_and_parse_invoice(id)

GetRecognizeAndParseInvoice

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
    api_instance = aspose_ocr_cloud.RecognizeAndParseInvoiceApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetRecognizeAndParseInvoice
        api_response = api_instance.get_recognize_and_parse_invoice(id)
        print("The response of RecognizeAndParseInvoiceApi->get_recognize_and_parse_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeAndParseInvoiceApi->get_recognize_and_parse_invoice: %s\n" % e)
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

# **post_recognize_and_parse_invoice**
> str post_recognize_and_parse_invoice(ocr_recognize_and_parse_invoice_body)

PostRecognizeAndParseInvoice

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.ocr_recognize_and_parse_invoice_body import OCRRecognizeAndParseInvoiceBody
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
    api_instance = aspose_ocr_cloud.RecognizeAndParseInvoiceApi(api_client)
    ocr_recognize_and_parse_invoice_body = aspose_ocr_cloud.OCRRecognizeAndParseInvoiceBody() # OCRRecognizeAndParseInvoiceBody | 

    try:
        # PostRecognizeAndParseInvoice
        api_response = api_instance.post_recognize_and_parse_invoice(ocr_recognize_and_parse_invoice_body)
        print("The response of RecognizeAndParseInvoiceApi->post_recognize_and_parse_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognizeAndParseInvoiceApi->post_recognize_and_parse_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_recognize_and_parse_invoice_body** | [**OCRRecognizeAndParseInvoiceBody**](OCRRecognizeAndParseInvoiceBody.md)|  | 

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

