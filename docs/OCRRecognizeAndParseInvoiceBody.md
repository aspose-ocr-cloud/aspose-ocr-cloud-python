# OCRRecognizeAndParseInvoiceBody

Combines Image data and OCR Recognition settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsRecognizeAndParseInvoice**](OCRSettingsRecognizeAndParseInvoice.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_recognize_and_parse_invoice_body import OCRRecognizeAndParseInvoiceBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRecognizeAndParseInvoiceBody from a JSON string
ocr_recognize_and_parse_invoice_body_instance = OCRRecognizeAndParseInvoiceBody.from_json(json)
# print the JSON string representation of the object
print(OCRRecognizeAndParseInvoiceBody.to_json())

# convert the object into a dict
ocr_recognize_and_parse_invoice_body_dict = ocr_recognize_and_parse_invoice_body_instance.to_dict()
# create an instance of OCRRecognizeAndParseInvoiceBody from a dict
ocr_recognize_and_parse_invoice_body_from_dict = OCRRecognizeAndParseInvoiceBody.from_dict(ocr_recognize_and_parse_invoice_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


