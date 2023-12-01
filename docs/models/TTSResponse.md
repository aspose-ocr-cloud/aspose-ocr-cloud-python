# aspose_ocr_cloud.model.tts_response.TTSResponse

Response with Recognition result for specific task ID

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response with Recognition result for specific task ID | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | None, str,  | NoneClass, str,  | The specific Task ID that result was made for | [optional] 
**responseStatusCode** | [**ResponseStatusCode**](ResponseStatusCode.md) | [**ResponseStatusCode**](ResponseStatusCode.md) |  | [optional] 
**taskStatus** | [**TTSTaskStatus**](TTSTaskStatus.md) | [**TTSTaskStatus**](TTSTaskStatus.md) |  | [optional] 
**[results](#results)** | list, tuple, None,  | tuple, NoneClass,  | List of results - Especially Text or PDF files | [optional] 
**error** | [**TTSError**](TTSError.md) | [**TTSError**](TTSError.md) |  | [optional] 

# results

List of results - Especially Text or PDF files

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of results - Especially Text or PDF files | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TTSResult**](TTSResult.md) | [**TTSResult**](TTSResult.md) | [**TTSResult**](TTSResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

