# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from aspose_ocr_cloud.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BINARIZE_IMAGE = "BinarizeImage"
    CONVERT_TEXT_TO_SPEECH = "ConvertTextToSpeech"
    CONVERT_TEXT_TO_SPEECH_TRIAL = "ConvertTextToSpeechTrial"
    DESKEW_IMAGE = "DeskewImage"
    DETECT_REGIONS = "DetectRegions"
    DEWARP_IMAGE = "DewarpImage"
    DJ_VU2PDF = "DjVu2PDF"
    IDENTIFY_FONT = "IdentifyFont"
    IMAGE_PROCESSING = "ImageProcessing"
    RECOGNIZE_AND_PARSE_INVOICE = "RecognizeAndParseInvoice"
    RECOGNIZE_IMAGE = "RecognizeImage"
    RECOGNIZE_LABEL = "RecognizeLabel"
    RECOGNIZE_PDF = "RecognizePdf"
    RECOGNIZE_RECEIPT = "RecognizeReceipt"
    RECOGNIZE_REGIONS = "RecognizeRegions"
    RECOGNIZE_TABLE = "RecognizeTable"
    TEXT_TO_SPEECH = "TextToSpeech"
    UPSCALE_IMAGE = "UpscaleImage"
    UTILITIES = "Utilities"
