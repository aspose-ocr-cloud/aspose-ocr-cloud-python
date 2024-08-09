# OCRError

Error to return to SDK client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **List[str]** | A list of various clear descriptions of the errors | [optional] [readonly] 
**warnings** | **List[str]** | Warning messages - non critical errors: e.g. some data lost | [optional] [readonly] 

## Example

```python
from aspose_ocr_cloud.models.ocr_error import OCRError

# TODO update the JSON string below
json = "{}"
# create an instance of OCRError from a JSON string
ocr_error_instance = OCRError.from_json(json)
# print the JSON string representation of the object
print(OCRError.to_json())

# convert the object into a dict
ocr_error_dict = ocr_error_instance.to_dict()
# create an instance of OCRError from a dict
ocr_error_from_dict = OCRError.from_dict(ocr_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


