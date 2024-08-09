# OCRRecognizeRegionsBody

Combines Image data and OCR Recognition settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsRecognizeRegions**](OCRSettingsRecognizeRegions.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_recognize_regions_body import OCRRecognizeRegionsBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRecognizeRegionsBody from a JSON string
ocr_recognize_regions_body_instance = OCRRecognizeRegionsBody.from_json(json)
# print the JSON string representation of the object
print(OCRRecognizeRegionsBody.to_json())

# convert the object into a dict
ocr_recognize_regions_body_dict = ocr_recognize_regions_body_instance.to_dict()
# create an instance of OCRRecognizeRegionsBody from a dict
ocr_recognize_regions_body_from_dict = OCRRecognizeRegionsBody.from_dict(ocr_recognize_regions_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


