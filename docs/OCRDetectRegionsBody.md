# OCRDetectRegionsBody

Combines Image data and OCR Recognition settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsDetectRegions**](OCRSettingsDetectRegions.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_detect_regions_body import OCRDetectRegionsBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRDetectRegionsBody from a JSON string
ocr_detect_regions_body_instance = OCRDetectRegionsBody.from_json(json)
# print the JSON string representation of the object
print(OCRDetectRegionsBody.to_json())

# convert the object into a dict
ocr_detect_regions_body_dict = ocr_detect_regions_body_instance.to_dict()
# create an instance of OCRDetectRegionsBody from a dict
ocr_detect_regions_body_from_dict = OCRDetectRegionsBody.from_dict(ocr_detect_regions_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


