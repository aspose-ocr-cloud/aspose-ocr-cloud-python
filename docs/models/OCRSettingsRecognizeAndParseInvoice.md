# aspose_ocr_cloud.model.ocr_settings_recognize_and_parse_invoice.OCRSettingsRecognizeAndParseInvoice

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**makeSkewCorrect** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**makeBinarization** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**makeUpsampling** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**resultType** | [**ResultType**](ResultType.md) | [**ResultType**](ResultType.md) |  | [optional] 
**language** | [**Language**](Language.md) | [**Language**](Language.md) |  | [optional] 
**Rotate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**makeSpellCheck** | bool,  | BoolClass,  | Option to enable spell checking and correction algorithm. False by default | [optional] if omitted the server will use the default value of False
**makeContrastCorrection** | bool,  | BoolClass,  | Option to enable image contrast correction algorithm. True by default | [optional] if omitted the server will use the default value of False
**dsrMode** | [**DsrMode**](DsrMode.md) | [**DsrMode**](DsrMode.md) |  | [optional] 
**dsrConfidence** | [**DsrConfidence**](DsrConfidence.md) | [**DsrConfidence**](DsrConfidence.md) |  | [optional] 
**resultTypeTable** | [**ResultTypeTable**](ResultTypeTable.md) | [**ResultTypeTable**](ResultTypeTable.md) |  | [optional] 
**[regions](#regions)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 

# regions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OCRRegion**](OCRRegion.md) | [**OCRRegion**](OCRRegion.md) | [**OCRRegion**](OCRRegion.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

