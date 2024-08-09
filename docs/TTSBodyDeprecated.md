# TTSBodyDeprecated

Represents input text data with settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Gets or Sets text | 
**language** | [**LanguageTTS**](LanguageTTS.md) |  | 
**result_type** | [**ResultTypeTTS**](ResultTypeTTS.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.tts_body_deprecated import TTSBodyDeprecated

# TODO update the JSON string below
json = "{}"
# create an instance of TTSBodyDeprecated from a JSON string
tts_body_deprecated_instance = TTSBodyDeprecated.from_json(json)
# print the JSON string representation of the object
print(TTSBodyDeprecated.to_json())

# convert the object into a dict
tts_body_deprecated_dict = tts_body_deprecated_instance.to_dict()
# create an instance of TTSBodyDeprecated from a dict
tts_body_deprecated_from_dict = TTSBodyDeprecated.from_dict(tts_body_deprecated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


