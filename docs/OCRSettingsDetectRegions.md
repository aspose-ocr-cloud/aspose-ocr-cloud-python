# OCRSettingsDetectRegions

OCR Process setting for Image recognition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**make_skew_correct** | **bool** | Option to enable skew correction algorithm. True by default | [optional] [default to True]
**make_contrast_correction** | **bool** | Option to enable image contrast correction algorithm. True by default | [optional] [default to False]
**make_upsampling** | **bool** | Option to enable image up-sampling algorithm to improve quality. True by default | [optional] [default to False]
**dsr_confidence** | [**DsrConfidence**](DsrConfidence.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**rotate** | **int** | Rotate image&gt; | [optional] 
**make_spell_check** | **bool** | Option to enable spell checking and correction algorithm. False by default | [optional] [default to False]
**make_binarization** | **bool** | Option to enable image binarization algorithm. False by default | [optional] [default to True]
**dsr_mode** | [**DsrMode**](DsrMode.md) |  | [optional] 
**result_type** | [**ResultType**](ResultType.md) |  | [optional] 
**result_type_table** | [**ResultTypeTable**](ResultTypeTable.md) |  | [optional] 
**regions** | [**List[OCRRegion]**](OCRRegion.md) | Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion | [optional] 

## Example

```python
from aspose_ocr_cloud.models.ocr_settings_detect_regions import OCRSettingsDetectRegions

# TODO update the JSON string below
json = "{}"
# create an instance of OCRSettingsDetectRegions from a JSON string
ocr_settings_detect_regions_instance = OCRSettingsDetectRegions.from_json(json)
# print the JSON string representation of the object
print(OCRSettingsDetectRegions.to_json())

# convert the object into a dict
ocr_settings_detect_regions_dict = ocr_settings_detect_regions_instance.to_dict()
# create an instance of OCRSettingsDetectRegions from a dict
ocr_settings_detect_regions_from_dict = OCRSettingsDetectRegions.from_dict(ocr_settings_detect_regions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


