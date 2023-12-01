<a name="__pageTop"></a>
# aspose_ocr_cloud.apis.tags.convert_text_to_speech_trial_api.ConvertTextToSpeechTrialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_convert_text_to_speech_trial**](#cancel_convert_text_to_speech_trial) | **delete** /v5.0/ocr/ConvertTextToSpeechTrial | CancelConvertTextToSpeechTrial
[**get_convert_text_to_speech_trial**](#get_convert_text_to_speech_trial) | **get** /v5.0/ocr/ConvertTextToSpeechTrial | GetConvertTextToSpeechTrial
[**post_convert_text_to_speech_trial**](#post_convert_text_to_speech_trial) | **post** /v5.0/ocr/ConvertTextToSpeechTrial | PostConvertTextToSpeechTrial

# **cancel_convert_text_to_speech_trial**
<a name="cancel_convert_text_to_speech_trial"></a>
> cancel_convert_text_to_speech_trial(id)

CancelConvertTextToSpeechTrial

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import convert_text_to_speech_trial_api
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

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_ocr_cloud.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with aspose_ocr_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = convert_text_to_speech_trial_api.ConvertTextToSpeechTrialApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'id': "id_example",
    }
    try:
        # CancelConvertTextToSpeechTrial
        api_response = api_instance.cancel_convert_text_to_speech_trial(
            query_params=query_params,
        )
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling ConvertTextToSpeechTrialApi->cancel_convert_text_to_speech_trial: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cancel_convert_text_to_speech_trial.ApiResponseFor200) | Success

#### cancel_convert_text_to_speech_trial.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_convert_text_to_speech_trial**
<a name="get_convert_text_to_speech_trial"></a>
> TTSResponse get_convert_text_to_speech_trial(id)

GetConvertTextToSpeechTrial

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import convert_text_to_speech_trial_api
from aspose_ocr_cloud.model.tts_response import TTSResponse
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

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_ocr_cloud.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with aspose_ocr_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = convert_text_to_speech_trial_api.ConvertTextToSpeechTrialApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'id': "id_example",
    }
    try:
        # GetConvertTextToSpeechTrial
        api_response = api_instance.get_convert_text_to_speech_trial(
            query_params=query_params,
        )
        pprint(api_response)
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling ConvertTextToSpeechTrialApi->get_convert_text_to_speech_trial: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_convert_text_to_speech_trial.ApiResponseFor200) | Success

#### get_convert_text_to_speech_trial.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TTSResponse**](../../models/TTSResponse.md) |  | 


### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_convert_text_to_speech_trial**
<a name="post_convert_text_to_speech_trial"></a>
> str post_convert_text_to_speech_trial(tts_body)

PostConvertTextToSpeechTrial

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import convert_text_to_speech_trial_api
from aspose_ocr_cloud.model.tts_body import TTSBody
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

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_ocr_cloud.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with aspose_ocr_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = convert_text_to_speech_trial_api.ConvertTextToSpeechTrialApi(api_client)

    # example passing only required values which don't have defaults set
    body = TTSBody(
        text="text_example",
        settings=TTSSettings(
            language=LanguageTTS("English"),
            result_type=ResultTypeTTS("Wav"),
        ),
    )
    try:
        # PostConvertTextToSpeechTrial
        api_response = api_instance.post_convert_text_to_speech_trial(
            body=body,
        )
        pprint(api_response)
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling ConvertTextToSpeechTrialApi->post_convert_text_to_speech_trial: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TTSBody**](../../models/TTSBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_convert_text_to_speech_trial.ApiResponseFor200) | Task unique ID

#### post_convert_text_to_speech_trial.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

