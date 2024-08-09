# aspose_ocr_cloud.ConvertTextToSpeechTrialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_convert_text_to_speech_trial**](ConvertTextToSpeechTrialApi.md#cancel_convert_text_to_speech_trial) | **DELETE** /v5.0/ocr/ConvertTextToSpeechTrial | CancelConvertTextToSpeechTrial
[**get_convert_text_to_speech_trial**](ConvertTextToSpeechTrialApi.md#get_convert_text_to_speech_trial) | **GET** /v5.0/ocr/ConvertTextToSpeechTrial | GetConvertTextToSpeechTrial
[**post_convert_text_to_speech_trial**](ConvertTextToSpeechTrialApi.md#post_convert_text_to_speech_trial) | **POST** /v5.0/ocr/ConvertTextToSpeechTrial | PostConvertTextToSpeechTrial


# **cancel_convert_text_to_speech_trial**
> cancel_convert_text_to_speech_trial(id)

CancelConvertTextToSpeechTrial

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
    api_instance = aspose_ocr_cloud.ConvertTextToSpeechTrialApi(api_client)
    id = 'id_example' # str | 

    try:
        # CancelConvertTextToSpeechTrial
        api_instance.cancel_convert_text_to_speech_trial(id)
    except Exception as e:
        print("Exception when calling ConvertTextToSpeechTrialApi->cancel_convert_text_to_speech_trial: %s\n" % e)
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

# **get_convert_text_to_speech_trial**
> TTSResponse get_convert_text_to_speech_trial(id)

GetConvertTextToSpeechTrial

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
    api_instance = aspose_ocr_cloud.ConvertTextToSpeechTrialApi(api_client)
    id = 'id_example' # str | Task id to select the result

    try:
        # GetConvertTextToSpeechTrial
        api_response = api_instance.get_convert_text_to_speech_trial(id)
        print("The response of ConvertTextToSpeechTrialApi->get_convert_text_to_speech_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertTextToSpeechTrialApi->get_convert_text_to_speech_trial: %s\n" % e)
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

# **post_convert_text_to_speech_trial**
> str post_convert_text_to_speech_trial(tts_body)

PostConvertTextToSpeechTrial

### Example

* OAuth Authentication (JWT):

```python
import aspose_ocr_cloud
from aspose_ocr_cloud.models.tts_body import TTSBody
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
    api_instance = aspose_ocr_cloud.ConvertTextToSpeechTrialApi(api_client)
    tts_body = aspose_ocr_cloud.TTSBody() # TTSBody | 

    try:
        # PostConvertTextToSpeechTrial
        api_response = api_instance.post_convert_text_to_speech_trial(tts_body)
        print("The response of ConvertTextToSpeechTrialApi->post_convert_text_to_speech_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertTextToSpeechTrialApi->post_convert_text_to_speech_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tts_body** | [**TTSBody**](TTSBody.md)|  | 

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

