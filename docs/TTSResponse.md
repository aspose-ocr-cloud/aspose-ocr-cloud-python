# TTSResponse

Response with Recognition result for specific task ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The specific Task ID that result was made for | [optional] 
**response_status_code** | [**ResponseStatusCode**](ResponseStatusCode.md) |  | [optional] 
**task_status** | [**TTSTaskStatus**](TTSTaskStatus.md) |  | [optional] 
**results** | [**List[TTSResult]**](TTSResult.md) | List of results - Especially Text or PDF files | [optional] [readonly] 
**error** | [**TTSError**](TTSError.md) |  | [optional] 

## Example

```python
from aspose_ocr_cloud.models.tts_response import TTSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TTSResponse from a JSON string
tts_response_instance = TTSResponse.from_json(json)
# print the JSON string representation of the object
print(TTSResponse.to_json())

# convert the object into a dict
tts_response_dict = tts_response_instance.to_dict()
# create an instance of TTSResponse from a dict
tts_response_from_dict = TTSResponse.from_dict(tts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


