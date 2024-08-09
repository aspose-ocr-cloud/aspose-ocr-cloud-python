# OCRSettingsRecognizeFont

OCR Process setting for Font image recognition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**Language**](Language.md) |  | [optional] 
**make_skew_correct** | **bool** | Option to enable skew correction algorithm. True by default | [optional] [default to True]
**make_spell_check** | **bool** | Option to enable spell checking and correction algorithm. False by default | [optional] [default to False]
**make_contrast_correction** | **bool** | Option to enable image contrast correction algorithm. True by default | [optional] [default to False]
**result_type** | [**ResultType**](ResultType.md) |  | [optional] 
**rotate** | **int** | Rotate image&gt; | [optional] 
**make_binarization** | **bool** | Option to enable image binarization algorithm. False by default | [optional] [default to True]
**make_upsampling** | **bool** | Option to enable image up-sampling algorithm to improve quality. True by default | [optional] [default to False]
**dsr_mode** | [**DsrMode**](DsrMode.md) |  | [optional] 
**dsr_confidence** | [**DsrConfidence**](DsrConfidence.md) |  | [optional] 
**result_type_table** | [**ResultTypeTable**](ResultTypeTable.md) |  | [optional] 
**regions** | [**List[OCRRegion]**](OCRRegion.md) | Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_settings_recognize_font import OCRSettingsRecognizeFont

# TODO update the JSON string below
json = "{}"
# create an instance of OCRSettingsRecognizeFont from a JSON string
ocr_settings_recognize_font_instance = OCRSettingsRecognizeFont.from_json(json)
# print the JSON string representation of the object
print(OCRSettingsRecognizeFont.to_json())

# convert the object into a dict
ocr_settings_recognize_font_dict = ocr_settings_recognize_font_instance.to_dict()
# create an instance of OCRSettingsRecognizeFont from a dict
ocr_settings_recognize_font_from_dict = OCRSettingsRecognizeFont.from_dict(ocr_settings_recognize_font_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


