# OCRDjVu2PDFBody

Combines Image data and OCR Recognition settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsDjVu2PDF**](OCRSettingsDjVu2PDF.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocrdj_vu2_pdf_body import OCRDjVu2PDFBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRDjVu2PDFBody from a JSON string
ocrdj_vu2_pdf_body_instance = OCRDjVu2PDFBody.from_json(json)
# print the JSON string representation of the object
print(OCRDjVu2PDFBody.to_json())

# convert the object into a dict
ocrdj_vu2_pdf_body_dict = ocrdj_vu2_pdf_body_instance.to_dict()
# create an instance of OCRDjVu2PDFBody from a dict
ocrdj_vu2_pdf_body_from_dict = OCRDjVu2PDFBody.from_dict(ocrdj_vu2_pdf_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


