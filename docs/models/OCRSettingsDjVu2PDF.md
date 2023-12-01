# aspose_ocr_cloud.model.ocr_settings_dj_vu2_pdf.OCRSettingsDjVu2PDF

OCR Process setting for Image recognition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | OCR Process setting for Image recognition | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**language** | [**Language**](Language.md) | [**Language**](Language.md) |  | [optional] 
**Rotate** | decimal.Decimal, int,  | decimal.Decimal,  | Rotate image&gt; | [optional] value must be a 32 bit integer
**makeSkewCorrect** | bool,  | BoolClass,  | Option to enable skew correction algorithm. True by default | [optional] if omitted the server will use the default value of True
**makeSpellCheck** | bool,  | BoolClass,  | Option to enable spell checking and correction algorithm. False by default | [optional] if omitted the server will use the default value of False
**makeContrastCorrection** | bool,  | BoolClass,  | Option to enable image contrast correction algorithm. True by default | [optional] if omitted the server will use the default value of False
**makeBinarization** | bool,  | BoolClass,  | Option to enable image binarization algorithm. False by default | [optional] if omitted the server will use the default value of True
**makeUpsampling** | bool,  | BoolClass,  | Option to enable image up-sampling algorithm to improve quality. True by default | [optional] if omitted the server will use the default value of False
**dsrMode** | [**DsrMode**](DsrMode.md) | [**DsrMode**](DsrMode.md) |  | [optional] 
**dsrConfidence** | [**DsrConfidence**](DsrConfidence.md) | [**DsrConfidence**](DsrConfidence.md) |  | [optional] 
**resultType** | [**ResultType**](ResultType.md) | [**ResultType**](ResultType.md) |  | [optional] 
**resultTypeTable** | [**ResultTypeTable**](ResultTypeTable.md) | [**ResultTypeTable**](ResultTypeTable.md) |  | [optional] 
**[regions](#regions)** | list, tuple, None,  | tuple, NoneClass,  | Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion | [optional] 

# regions

Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OCRRegion**](OCRRegion.md) | [**OCRRegion**](OCRRegion.md) | [**OCRRegion**](OCRRegion.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

