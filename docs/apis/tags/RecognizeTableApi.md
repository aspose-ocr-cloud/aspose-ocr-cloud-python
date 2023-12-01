<a name="__pageTop"></a>
# aspose_ocr_cloud.apis.tags.recognize_table_api.RecognizeTableApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recognize_table**](#cancel_recognize_table) | **delete** /v5.0/ocr/RecognizeTable | CancelRecognizeTable
[**get_recognize_table**](#get_recognize_table) | **get** /v5.0/ocr/RecognizeTable | GetRecognizeTable
[**post_recognize_table**](#post_recognize_table) | **post** /v5.0/ocr/RecognizeTable | PostRecognizeTable

# **cancel_recognize_table**
<a name="cancel_recognize_table"></a>
> cancel_recognize_table(id)

CancelRecognizeTable

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import recognize_table_api
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
    api_instance = recognize_table_api.RecognizeTableApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'id': "id_example",
    }
    try:
        # CancelRecognizeTable
        api_response = api_instance.cancel_recognize_table(
            query_params=query_params,
        )
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling RecognizeTableApi->cancel_recognize_table: %s\n" % e)
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
200 | [ApiResponseFor200](#cancel_recognize_table.ApiResponseFor200) | Success

#### cancel_recognize_table.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_recognize_table**
<a name="get_recognize_table"></a>
> OCRResponse get_recognize_table(id)

GetRecognizeTable

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import recognize_table_api
from aspose_ocr_cloud.model.ocr_response import OCRResponse
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
    api_instance = recognize_table_api.RecognizeTableApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'id': "id_example",
    }
    try:
        # GetRecognizeTable
        api_response = api_instance.get_recognize_table(
            query_params=query_params,
        )
        pprint(api_response)
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling RecognizeTableApi->get_recognize_table: %s\n" % e)
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
200 | [ApiResponseFor200](#get_recognize_table.ApiResponseFor200) | Success

#### get_recognize_table.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OCRResponse**](../../models/OCRResponse.md) |  | 


### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_recognize_table**
<a name="post_recognize_table"></a>
> str post_recognize_table(ocr_recognize_table_body)

PostRecognizeTable

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import recognize_table_api
from aspose_ocr_cloud.model.problem_details import ProblemDetails
from aspose_ocr_cloud.model.ocr_recognize_table_body import OCRRecognizeTableBody
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
    api_instance = recognize_table_api.RecognizeTableApi(api_client)

    # example passing only required values which don't have defaults set
    body = OCRRecognizeTableBody(
        image='YQ==',
        settings=OCRSettingsRecognizeTable(
            language=Language("English"),
            make_skew_correct=True,
            make_spell_check=False,
            make_contrast_correction=False,
            result_type_table=ResultTypeTable("Text"),
            rotate=1,
            make_binarization=True,
            make_upsampling=False,
            dsr_mode=DsrMode("Regions"),
            dsr_confidence=DsrConfidence("Default"),
            result_type=ResultType("Text"),
            regions=[
                OCRRegion(
                    rect=OCRRect(
                        top_left_x=1,
                        top_left_y=1,
                        bottom_right_x=1,
                        bottom_right_y=1,
                    ),
                    order=1,
                )
            ],
        ),
    )
    try:
        # PostRecognizeTable
        api_response = api_instance.post_recognize_table(
            body=body,
        )
        pprint(api_response)
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling RecognizeTableApi->post_recognize_table: %s\n" % e)
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
[**OCRRecognizeTableBody**](../../models/OCRRecognizeTableBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_recognize_table.ApiResponseFor200) | Task unique ID
401 | [ApiResponseFor401](#post_recognize_table.ApiResponseFor401) | Unauthorized

#### post_recognize_table.ApiResponseFor200
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

#### post_recognize_table.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](../../models/ProblemDetails.md) |  | 


### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

