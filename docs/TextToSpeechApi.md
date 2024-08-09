# aspose_ocr_cloud.TextToSpeechApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_text_to_speech_result**](TextToSpeechApi.md#get_text_to_speech_result) | **GET** /v5.0/ocr/TextToSpeech/GetTextToSpeechResult | GetTextToSpeechResult
[**get_text_to_speech_result_file**](TextToSpeechApi.md#get_text_to_speech_result_file) | **GET** /v5.0/ocr/TextToSpeech/GetTextToSpeechResultFile | GetTextToSpeechResultFile
[**post_text_to_speech**](TextToSpeechApi.md#post_text_to_speech) | **POST** /v5.0/ocr/TextToSpeech/PostTextToSpeech | PostTextToSpeech


# **get_text_to_speech_result**
> TTSResponse get_text_to_speech_result(id)

GetTextToSpeechResult

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.tts_response import TTSResponse
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
    api_instance = aspose_ocr_cloud.TextToSpeechApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetTextToSpeechResult
        api_response = api_instance.get_text_to_speech_result(id)
        print("The response of TextToSpeechApi->get_text_to_speech_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextToSpeechApi->get_text_to_speech_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task id to select the result | 

### Return type

[**TTSResponse**](TTSResponse.md)

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

# **get_text_to_speech_result_file**
> object get_text_to_speech_result_file(id)

GetTextToSpeechResultFile

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
    api_instance = aspose_ocr_cloud.TextToSpeechApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetTextToSpeechResultFile
        api_response = api_instance.get_text_to_speech_result_file(id)
        print("The response of TextToSpeechApi->get_text_to_speech_result_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextToSpeechApi->get_text_to_speech_result_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task id to select the result | 

### Return type

**object**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Results expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_text_to_speech**
> str post_text_to_speech(tts_body_deprecated)

PostTextToSpeech

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.tts_body_deprecated import TTSBodyDeprecated
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
    api_instance = aspose_ocr_cloud.TextToSpeechApi(api_client)
    tts_body_deprecated = aspose_ocr_cloud.TTSBodyDeprecated() # TTSBodyDeprecated | 

    try:
        # PostTextToSpeech
        api_response = api_instance.post_text_to_speech(tts_body_deprecated)
        print("The response of TextToSpeechApi->post_text_to_speech:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextToSpeechApi->post_text_to_speech: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tts_body_deprecated** | [**TTSBodyDeprecated**](TTSBodyDeprecated.md)|  | 

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

