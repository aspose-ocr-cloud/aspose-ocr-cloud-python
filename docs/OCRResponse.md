# OCRResponse

Response with Recognition result for specific task ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The specific Task ID that result was made for | [optional] 
**response_status_code** | [**ResponseStatusCode**](ResponseStatusCode.md) |  | [optional] 
**task_status** | [**OCRTaskStatus**](OCRTaskStatus.md) |  | [optional] 
**results** | [**List[OCRResult]**](OCRResult.md) | List of results - Especially Text or PDF files | [optional] [readonly] 
**error** | [**OCRError**](OCRError.md) |  | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_response import OCRResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OCRResponse from a JSON string
ocr_response_instance = OCRResponse.from_json(json)
# print the JSON string representation of the object
print(OCRResponse.to_json())

# convert the object into a dict
ocr_response_dict = ocr_response_instance.to_dict()
# create an instance of OCRResponse from a dict
ocr_response_from_dict = OCRResponse.from_dict(ocr_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


