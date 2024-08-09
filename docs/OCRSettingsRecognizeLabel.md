# OCRSettingsRecognizeLabel

OCR Process setting for Image recognition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**Language**](Language.md) |  | [optional] 
**make_skew_correct** | **bool** | Option to enable skew correction algorithm. True by default | [optional] [default to False]
**make_binarization** | **bool** | Option to enable binarization algorithm. False by default | [optional] [default to False]
**make_spell_check** | **bool** | Option to enable spell checking and correction algorithm. False by default | [optional] [default to False]
**make_contrast_correction** | **bool** | Option to enable image contrast correction algorithm. True by default | [optional] [default to False]
**make_upsampling** | **bool** | Option to enable image up-sampling algorithm to improve quality. True by default | [optional] [default to False]
**dsr_mode** | [**DsrMode**](DsrMode.md) |  | [optional] 
**dsr_confidence** | [**DsrConfidence**](DsrConfidence.md) |  | [optional] 
**result_type** | [**ResultType**](ResultType.md) |  | [optional] 
**rotate** | **int** | Rotate image&gt; | [optional] 
**result_type_table** | [**ResultTypeTable**](ResultTypeTable.md) |  | [optional] 
**regions** | [**List[OCRRegion]**](OCRRegion.md) | Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_settings_recognize_label import OCRSettingsRecognizeLabel

# TODO update the JSON string below
json = "{}"
# create an instance of OCRSettingsRecognizeLabel from a JSON string
ocr_settings_recognize_label_instance = OCRSettingsRecognizeLabel.from_json(json)
# print the JSON string representation of the object
print(OCRSettingsRecognizeLabel.to_json())

# convert the object into a dict
ocr_settings_recognize_label_dict = ocr_settings_recognize_label_instance.to_dict()
# create an instance of OCRSettingsRecognizeLabel from a dict
ocr_settings_recognize_label_from_dict = OCRSettingsRecognizeLabel.from_dict(ocr_settings_recognize_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


