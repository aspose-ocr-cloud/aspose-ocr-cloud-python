# TTSSettings

TTS setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**LanguageTTS**](LanguageTTS.md) |  | 
**result_type** | [**ResultTypeTTS**](ResultTypeTTS.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.tts_settings import TTSSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TTSSettings from a JSON string
tts_settings_instance = TTSSettings.from_json(json)
# print the JSON string representation of the object
print(TTSSettings.to_json())

# convert the object into a dict
tts_settings_dict = tts_settings_instance.to_dict()
# create an instance of TTSSettings from a dict
tts_settings_from_dict = TTSSettings.from_dict(tts_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


