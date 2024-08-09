# OCRRecognizeReceiptBody

Combines Image data and OCR Recognition settings fro Receipt image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | Gets or Sets Image | 
**settings** | [**OCRSettingsRecognizeReceipt**](OCRSettingsRecognizeReceipt.md) |  | 

## Example

```python
from aspose_ocr_cloud.models.ocr_recognize_receipt_body import OCRRecognizeReceiptBody

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRecognizeReceiptBody from a JSON string
ocr_recognize_receipt_body_instance = OCRRecognizeReceiptBody.from_json(json)
# print the JSON string representation of the object
print(OCRRecognizeReceiptBody.to_json())

# convert the object into a dict
ocr_recognize_receipt_body_dict = ocr_recognize_receipt_body_instance.to_dict()
# create an instance of OCRRecognizeReceiptBody from a dict
ocr_recognize_receipt_body_from_dict = OCRRecognizeReceiptBody.from_dict(ocr_recognize_receipt_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


