# OCRRecognizePdfBody

Combines Image data and OCR Recognition settings for PDF

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsRecognizePdf**](OCRSettingsRecognizePdf.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_recognize_pdf_body import OCRRecognizePdfBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRecognizePdfBody from a JSON string
ocr_recognize_pdf_body_instance = OCRRecognizePdfBody.from_json(json)
# print the JSON string representation of the object
print(OCRRecognizePdfBody.to_json())

# convert the object into a dict
ocr_recognize_pdf_body_dict = ocr_recognize_pdf_body_instance.to_dict()
# create an instance of OCRRecognizePdfBody from a dict
ocr_recognize_pdf_body_from_dict = OCRRecognizePdfBody.from_dict(ocr_recognize_pdf_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


