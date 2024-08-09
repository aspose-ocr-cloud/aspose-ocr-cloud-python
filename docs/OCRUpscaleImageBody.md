# OCRUpscaleImageBody

Combines Image data and OCR processing settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 

## Example

```python
from aspose_ocr_cloud.models.ocr_upscale_image_body import OCRUpscaleImageBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRUpscaleImageBody from a JSON string
ocr_upscale_image_body_instance = OCRUpscaleImageBody.from_json(json)
# print the JSON string representation of the object
print(OCRUpscaleImageBody.to_json())

# convert the object into a dict
ocr_upscale_image_body_dict = ocr_upscale_image_body_instance.to_dict()
# create an instance of OCRUpscaleImageBody from a dict
ocr_upscale_image_body_from_dict = OCRUpscaleImageBody.from_dict(ocr_upscale_image_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

