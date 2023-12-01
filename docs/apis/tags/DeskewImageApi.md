<a name="__pageTop"></a>
# aspose_ocr_cloud.apis.tags.deskew_image_api.DeskewImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_deskew_image**](#cancel_deskew_image) | **delete** /v5.0/ocr/DeskewImage | CancelDeskewImage
[**get_deskew_image**](#get_deskew_image) | **get** /v5.0/ocr/DeskewImage | GetDeskewImage
[**post_deskew_image**](#post_deskew_image) | **post** /v5.0/ocr/DeskewImage | PostDeskewImage

# **cancel_deskew_image**
<a name="cancel_deskew_image"></a>
> cancel_deskew_image(id)

CancelDeskewImage

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import deskew_image_api
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
    api_instance = deskew_image_api.DeskewImageApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'id': "id_example",
    }
    try:
        # CancelDeskewImage
        api_response = api_instance.cancel_deskew_image(
            query_params=query_params,
        )
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling DeskewImageApi->cancel_deskew_image: %s\n" % e)
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
200 | [ApiResponseFor200](#cancel_deskew_image.ApiResponseFor200) | Success

#### cancel_deskew_image.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_deskew_image**
<a name="get_deskew_image"></a>
> OCRResponse get_deskew_image(id)

GetDeskewImage

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import deskew_image_api
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
    api_instance = deskew_image_api.DeskewImageApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'id': "id_example",
    }
    try:
        # GetDeskewImage
        api_response = api_instance.get_deskew_image(
            query_params=query_params,
        )
        pprint(api_response)
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling DeskewImageApi->get_deskew_image: %s\n" % e)
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
200 | [ApiResponseFor200](#get_deskew_image.ApiResponseFor200) | Success

#### get_deskew_image.ApiResponseFor200
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

# **post_deskew_image**
<a name="post_deskew_image"></a>
> str post_deskew_image(ocr_deskew_image_body)

PostDeskewImage

### Example

* OAuth Authentication (JWT):
```python
import aspose_ocr_cloud
from aspose_ocr_cloud.apis.tags import deskew_image_api
from aspose_ocr_cloud.model.problem_details import ProblemDetails
from aspose_ocr_cloud.model.ocr_deskew_image_body import OCRDeskewImageBody
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
    api_instance = deskew_image_api.DeskewImageApi(api_client)

    # example passing only required values which don't have defaults set
    body = OCRDeskewImageBody(
        image='YQ==',
    )
    try:
        # PostDeskewImage
        api_response = api_instance.post_deskew_image(
            body=body,
        )
        pprint(api_response)
    except aspose_ocr_cloud.ApiException as e:
        print("Exception when calling DeskewImageApi->post_deskew_image: %s\n" % e)
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
[**OCRDeskewImageBody**](../../models/OCRDeskewImageBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_deskew_image.ApiResponseFor200) | Success
401 | [ApiResponseFor401](#post_deskew_image.ApiResponseFor401) | Unauthorized

#### post_deskew_image.ApiResponseFor200
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

#### post_deskew_image.ApiResponseFor401
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

