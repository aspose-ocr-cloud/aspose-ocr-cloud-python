# OCRRegion

Represents information about strict regions to recognize text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rect** | [**OCRRect**](OCRRect.md) |  | [optional] 
**order** | **int** | The serial number of the region for the formation of the text | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_region import OCRRegion

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRegion from a JSON string
ocr_region_instance = OCRRegion.from_json(json)
# print the JSON string representation of the object
print(OCRRegion.to_json())

# convert the object into a dict
ocr_region_dict = ocr_region_instance.to_dict()
# create an instance of OCRRegion from a dict
ocr_region_from_dict = OCRRegion.from_dict(ocr_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


