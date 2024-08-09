# TTSError

Error to return to SDK client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **List[str]** | A list of various clear descriptions of the errors | [optional] [readonly] 
**warnings** | **List[str]** | Warning messages - non critical errors: e.g. some data lost | [optional] [readonly] 

## Example

```python
from aspose_ocr_cloud.models.tts_error import TTSError

# TODO update the JSON string below
json = "{}"
# create an instance of TTSError from a JSON string
tts_error_instance = TTSError.from_json(json)
# print the JSON string representation of the object
print(TTSError.to_json())

# convert the object into a dict
tts_error_dict = tts_error_instance.to_dict()
# create an instance of TTSError from a dict
tts_error_from_dict = TTSError.from_dict(tts_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


