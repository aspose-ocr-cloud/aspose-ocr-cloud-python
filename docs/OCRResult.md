# OCRResult

Represents information about response after OCR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | File data type (extension) | [optional] 
**data** | **bytearray** | File binary data | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_result import OCRResult

# TODO update the JSON string below
json = "{}"
# create an instance of OCRResult from a JSON string
ocr_result_instance = OCRResult.from_json(json)
# print the JSON string representation of the object
print(OCRResult.to_json())

# convert the object into a dict
ocr_result_dict = ocr_result_instance.to_dict()
# create an instance of OCRResult from a dict
ocr_result_from_dict = OCRResult.from_dict(ocr_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


