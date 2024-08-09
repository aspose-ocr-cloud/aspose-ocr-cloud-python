# TTSResult

Represents information about response after TTS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | File data type (extension) | [optional] 
**data** | **bytearray** | File binary data | [optional] 

## Example

```python
from aspose_ocr_cloud.models.tts_result import TTSResult

# TODO update the JSON string below
json = "{}"
# create an instance of TTSResult from a JSON string
tts_result_instance = TTSResult.from_json(json)
# print the JSON string representation of the object
print(TTSResult.to_json())

# convert the object into a dict
tts_result_dict = tts_result_instance.to_dict()
# create an instance of TTSResult from a dict
tts_result_from_dict = TTSResult.from_dict(tts_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


