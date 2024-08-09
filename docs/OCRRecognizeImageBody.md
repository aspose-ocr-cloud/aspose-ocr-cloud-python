# OCRRecognizeImageBody

Combines Image data and OCR Recognition settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsRecognizeImage**](OCRSettingsRecognizeImage.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_recognize_image_body import OCRRecognizeImageBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRecognizeImageBody from a JSON string
ocr_recognize_image_body_instance = OCRRecognizeImageBody.from_json(json)
# print the JSON string representation of the object
print(OCRRecognizeImageBody.to_json())

# convert the object into a dict
ocr_recognize_image_body_dict = ocr_recognize_image_body_instance.to_dict()
# create an instance of OCRRecognizeImageBody from a dict
ocr_recognize_image_body_from_dict = OCRRecognizeImageBody.from_dict(ocr_recognize_image_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


