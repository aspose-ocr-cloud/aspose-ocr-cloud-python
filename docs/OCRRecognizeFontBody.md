# OCRRecognizeFontBody

Combines Image data and OCR Recognition settings for Font image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsRecognizeFont**](OCRSettingsRecognizeFont.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_recognize_font_body import OCRRecognizeFontBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRecognizeFontBody from a JSON string
ocr_recognize_font_body_instance = OCRRecognizeFontBody.from_json(json)
# print the JSON string representation of the object
print(OCRRecognizeFontBody.to_json())

# convert the object into a dict
ocr_recognize_font_body_dict = ocr_recognize_font_body_instance.to_dict()
# create an instance of OCRRecognizeFontBody from a dict
ocr_recognize_font_body_from_dict = OCRRecognizeFontBody.from_dict(ocr_recognize_font_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


