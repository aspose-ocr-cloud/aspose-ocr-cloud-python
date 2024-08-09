# OCRRect

Represents a rectangle: Left-Top (X1-Y1) to Right-Bottom (X2-Y2)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_left_x** | **int** | X-Coordinate of top left corner | [optional] 
**top_left_y** | **int** | Y-Coordinate of top left corner | [optional] 
**bottom_right_x** | **int** | X-Coordinate of bottom right corner | [optional] 
**bottom_right_y** | **int** | Y-Coordinate of bottom right corner | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_rect import OCRRect

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRect from a JSON string
ocr_rect_instance = OCRRect.from_json(json)
# print the JSON string representation of the object
print(OCRRect.to_json())

# convert the object into a dict
ocr_rect_dict = ocr_rect_instance.to_dict()
# create an instance of OCRRect from a dict
ocr_rect_from_dict = OCRRect.from_dict(ocr_rect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


