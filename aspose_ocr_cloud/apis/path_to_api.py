import typing_extensions

from aspose_ocr_cloud.paths import PathValues
from aspose_ocr_cloud.apis.paths.v5_0_ocr_binarize_image import V50OcrBinarizeImage
from aspose_ocr_cloud.apis.paths.v5_0_ocr_convert_text_to_speech import V50OcrConvertTextToSpeech
from aspose_ocr_cloud.apis.paths.v5_0_ocr_convert_text_to_speech_trial import V50OcrConvertTextToSpeechTrial
from aspose_ocr_cloud.apis.paths.v5_0_ocr_deskew_image import V50OcrDeskewImage
from aspose_ocr_cloud.apis.paths.v5_0_ocr_detect_regions import V50OcrDetectRegions
from aspose_ocr_cloud.apis.paths.v5_0_ocr_dewarp_image import V50OcrDewarpImage
from aspose_ocr_cloud.apis.paths.v5_0_ocr_dj_vu2_pdf import V50OcrDjVu2PDF
from aspose_ocr_cloud.apis.paths.v5_0_ocr_identify_font import V50OcrIdentifyFont
from aspose_ocr_cloud.apis.paths.v5_0_ocr_image_processing_post_upsampling_image_file import V50OcrImageProcessingPostUpsamplingImageFile
from aspose_ocr_cloud.apis.paths.v5_0_ocr_image_processing_post_binarization_file import V50OcrImageProcessingPostBinarizationFile
from aspose_ocr_cloud.apis.paths.v5_0_ocr_image_processing_post_skew_correction_file import V50OcrImageProcessingPostSkewCorrectionFile
from aspose_ocr_cloud.apis.paths.v5_0_ocr_image_processing_post_dewarping_file import V50OcrImageProcessingPostDewarpingFile
from aspose_ocr_cloud.apis.paths.v5_0_ocr_image_processing_get_result_task import V50OcrImageProcessingGetResultTask
from aspose_ocr_cloud.apis.paths.v5_0_ocr_image_processing_get_result_file import V50OcrImageProcessingGetResultFile
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_and_parse_invoice import V50OcrRecognizeAndParseInvoice
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_image import V50OcrRecognizeImage
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_label import V50OcrRecognizeLabel
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_pdf import V50OcrRecognizePdf
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_receipt import V50OcrRecognizeReceipt
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_regions import V50OcrRecognizeRegions
from aspose_ocr_cloud.apis.paths.v5_0_ocr_recognize_table import V50OcrRecognizeTable
from aspose_ocr_cloud.apis.paths.v5_0_ocr_text_to_speech_post_text_to_speech import V50OcrTextToSpeechPostTextToSpeech
from aspose_ocr_cloud.apis.paths.v5_0_ocr_text_to_speech_get_text_to_speech_result import V50OcrTextToSpeechGetTextToSpeechResult
from aspose_ocr_cloud.apis.paths.v5_0_ocr_text_to_speech_get_text_to_speech_result_file import V50OcrTextToSpeechGetTextToSpeechResultFile
from aspose_ocr_cloud.apis.paths.v5_0_ocr_upscale_image import V50OcrUpscaleImage
from aspose_ocr_cloud.apis.paths.v5_0_ocr_utilities_get_task_status import V50OcrUtilitiesGetTaskStatus

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V5_0_OCR_BINARIZE_IMAGE: V50OcrBinarizeImage,
        PathValues.V5_0_OCR_CONVERT_TEXT_TO_SPEECH: V50OcrConvertTextToSpeech,
        PathValues.V5_0_OCR_CONVERT_TEXT_TO_SPEECH_TRIAL: V50OcrConvertTextToSpeechTrial,
        PathValues.V5_0_OCR_DESKEW_IMAGE: V50OcrDeskewImage,
        PathValues.V5_0_OCR_DETECT_REGIONS: V50OcrDetectRegions,
        PathValues.V5_0_OCR_DEWARP_IMAGE: V50OcrDewarpImage,
        PathValues.V5_0_OCR_DJ_VU2PDF: V50OcrDjVu2PDF,
        PathValues.V5_0_OCR_IDENTIFY_FONT: V50OcrIdentifyFont,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_UPSAMPLING_IMAGE_FILE: V50OcrImageProcessingPostUpsamplingImageFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_BINARIZATION_FILE: V50OcrImageProcessingPostBinarizationFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_SKEW_CORRECTION_FILE: V50OcrImageProcessingPostSkewCorrectionFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_DEWARPING_FILE: V50OcrImageProcessingPostDewarpingFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_GET_RESULT_TASK: V50OcrImageProcessingGetResultTask,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_GET_RESULT_FILE: V50OcrImageProcessingGetResultFile,
        PathValues.V5_0_OCR_RECOGNIZE_AND_PARSE_INVOICE: V50OcrRecognizeAndParseInvoice,
        PathValues.V5_0_OCR_RECOGNIZE_IMAGE: V50OcrRecognizeImage,
        PathValues.V5_0_OCR_RECOGNIZE_LABEL: V50OcrRecognizeLabel,
        PathValues.V5_0_OCR_RECOGNIZE_PDF: V50OcrRecognizePdf,
        PathValues.V5_0_OCR_RECOGNIZE_RECEIPT: V50OcrRecognizeReceipt,
        PathValues.V5_0_OCR_RECOGNIZE_REGIONS: V50OcrRecognizeRegions,
        PathValues.V5_0_OCR_RECOGNIZE_TABLE: V50OcrRecognizeTable,
        PathValues.V5_0_OCR_TEXT_TO_SPEECH_POST_TEXT_TO_SPEECH: V50OcrTextToSpeechPostTextToSpeech,
        PathValues.V5_0_OCR_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT: V50OcrTextToSpeechGetTextToSpeechResult,
        PathValues.V5_0_OCR_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT_FILE: V50OcrTextToSpeechGetTextToSpeechResultFile,
        PathValues.V5_0_OCR_UPSCALE_IMAGE: V50OcrUpscaleImage,
        PathValues.V5_0_OCR_UTILITIES_GET_TASK_STATUS: V50OcrUtilitiesGetTaskStatus,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V5_0_OCR_BINARIZE_IMAGE: V50OcrBinarizeImage,
        PathValues.V5_0_OCR_CONVERT_TEXT_TO_SPEECH: V50OcrConvertTextToSpeech,
        PathValues.V5_0_OCR_CONVERT_TEXT_TO_SPEECH_TRIAL: V50OcrConvertTextToSpeechTrial,
        PathValues.V5_0_OCR_DESKEW_IMAGE: V50OcrDeskewImage,
        PathValues.V5_0_OCR_DETECT_REGIONS: V50OcrDetectRegions,
        PathValues.V5_0_OCR_DEWARP_IMAGE: V50OcrDewarpImage,
        PathValues.V5_0_OCR_DJ_VU2PDF: V50OcrDjVu2PDF,
        PathValues.V5_0_OCR_IDENTIFY_FONT: V50OcrIdentifyFont,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_UPSAMPLING_IMAGE_FILE: V50OcrImageProcessingPostUpsamplingImageFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_BINARIZATION_FILE: V50OcrImageProcessingPostBinarizationFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_SKEW_CORRECTION_FILE: V50OcrImageProcessingPostSkewCorrectionFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_POST_DEWARPING_FILE: V50OcrImageProcessingPostDewarpingFile,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_GET_RESULT_TASK: V50OcrImageProcessingGetResultTask,
        PathValues.V5_0_OCR_IMAGE_PROCESSING_GET_RESULT_FILE: V50OcrImageProcessingGetResultFile,
        PathValues.V5_0_OCR_RECOGNIZE_AND_PARSE_INVOICE: V50OcrRecognizeAndParseInvoice,
        PathValues.V5_0_OCR_RECOGNIZE_IMAGE: V50OcrRecognizeImage,
        PathValues.V5_0_OCR_RECOGNIZE_LABEL: V50OcrRecognizeLabel,
        PathValues.V5_0_OCR_RECOGNIZE_PDF: V50OcrRecognizePdf,
        PathValues.V5_0_OCR_RECOGNIZE_RECEIPT: V50OcrRecognizeReceipt,
        PathValues.V5_0_OCR_RECOGNIZE_REGIONS: V50OcrRecognizeRegions,
        PathValues.V5_0_OCR_RECOGNIZE_TABLE: V50OcrRecognizeTable,
        PathValues.V5_0_OCR_TEXT_TO_SPEECH_POST_TEXT_TO_SPEECH: V50OcrTextToSpeechPostTextToSpeech,
        PathValues.V5_0_OCR_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT: V50OcrTextToSpeechGetTextToSpeechResult,
        PathValues.V5_0_OCR_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT_FILE: V50OcrTextToSpeechGetTextToSpeechResultFile,
        PathValues.V5_0_OCR_UPSCALE_IMAGE: V50OcrUpscaleImage,
        PathValues.V5_0_OCR_UTILITIES_GET_TASK_STATUS: V50OcrUtilitiesGetTaskStatus,
    }
)
