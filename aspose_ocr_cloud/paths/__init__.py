# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from aspose_ocr_cloud.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V5_0_OCR_BINARIZE_IMAGE = "/v5.0/ocr/BinarizeImage"
    V5_0_OCR_CONVERT_TEXT_TO_SPEECH = "/v5.0/ocr/ConvertTextToSpeech"
    V5_0_OCR_CONVERT_TEXT_TO_SPEECH_TRIAL = "/v5.0/ocr/ConvertTextToSpeechTrial"
    V5_0_OCR_DESKEW_IMAGE = "/v5.0/ocr/DeskewImage"
    V5_0_OCR_DETECT_REGIONS = "/v5.0/ocr/DetectRegions"
    V5_0_OCR_DEWARP_IMAGE = "/v5.0/ocr/DewarpImage"
    V5_0_OCR_DJ_VU2PDF = "/v5.0/ocr/DjVu2PDF"
    V5_0_OCR_IDENTIFY_FONT = "/v5.0/ocr/IdentifyFont"
    V5_0_OCR_IMAGE_PROCESSING_POST_UPSAMPLING_IMAGE_FILE = "/v5.0/ocr/ImageProcessing/PostUpsamplingImageFile"
    V5_0_OCR_IMAGE_PROCESSING_POST_BINARIZATION_FILE = "/v5.0/ocr/ImageProcessing/PostBinarizationFile"
    V5_0_OCR_IMAGE_PROCESSING_POST_SKEW_CORRECTION_FILE = "/v5.0/ocr/ImageProcessing/PostSkewCorrectionFile"
    V5_0_OCR_IMAGE_PROCESSING_POST_DEWARPING_FILE = "/v5.0/ocr/ImageProcessing/PostDewarpingFile"
    V5_0_OCR_IMAGE_PROCESSING_GET_RESULT_TASK = "/v5.0/ocr/ImageProcessing/GetResultTask"
    V5_0_OCR_IMAGE_PROCESSING_GET_RESULT_FILE = "/v5.0/ocr/ImageProcessing/GetResultFile"
    V5_0_OCR_RECOGNIZE_AND_PARSE_INVOICE = "/v5.0/ocr/RecognizeAndParseInvoice"
    V5_0_OCR_RECOGNIZE_IMAGE = "/v5.0/ocr/RecognizeImage"
    V5_0_OCR_RECOGNIZE_LABEL = "/v5.0/ocr/RecognizeLabel"
    V5_0_OCR_RECOGNIZE_PDF = "/v5.0/ocr/RecognizePdf"
    V5_0_OCR_RECOGNIZE_RECEIPT = "/v5.0/ocr/RecognizeReceipt"
    V5_0_OCR_RECOGNIZE_REGIONS = "/v5.0/ocr/RecognizeRegions"
    V5_0_OCR_RECOGNIZE_TABLE = "/v5.0/ocr/RecognizeTable"
    V5_0_OCR_TEXT_TO_SPEECH_POST_TEXT_TO_SPEECH = "/v5.0/ocr/TextToSpeech/PostTextToSpeech"
    V5_0_OCR_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT = "/v5.0/ocr/TextToSpeech/GetTextToSpeechResult"
    V5_0_OCR_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT_FILE = "/v5.0/ocr/TextToSpeech/GetTextToSpeechResultFile"
    V5_0_OCR_UPSCALE_IMAGE = "/v5.0/ocr/UpscaleImage"
    V5_0_OCR_UTILITIES_GET_TASK_STATUS = "/v5.0/ocr/Utilities/GetTaskStatus"
