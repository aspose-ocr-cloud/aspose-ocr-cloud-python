# TTSBody

Represents input text data with settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Gets or Sets text | 
**settings** | [**TTSSettings**](TTSSettings.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.tts_body import TTSBody

# TODO update the JSON string below
json = "{}"
# create an instance of TTSBody from a JSON string
tts_body_instance = TTSBody.from_json(json)
# print the JSON string representation of the object
print(TTSBody.to_json())

# convert the object into a dict
tts_body_dict = tts_body_instance.to_dict()
# create an instance of TTSBody from a dict
tts_body_from_dict = TTSBody.from_dict(tts_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


