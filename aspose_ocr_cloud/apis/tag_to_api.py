import typing_extensions

from aspose_ocr_cloud.apis.tags import TagValues
from aspose_ocr_cloud.apis.tags.binarize_image_api import BinarizeImageApi
from aspose_ocr_cloud.apis.tags.convert_text_to_speech_api import ConvertTextToSpeechApi
from aspose_ocr_cloud.apis.tags.convert_text_to_speech_trial_api import ConvertTextToSpeechTrialApi
from aspose_ocr_cloud.apis.tags.deskew_image_api import DeskewImageApi
from aspose_ocr_cloud.apis.tags.detect_regions_api import DetectRegionsApi
from aspose_ocr_cloud.apis.tags.dewarp_image_api import DewarpImageApi
from aspose_ocr_cloud.apis.tags.dj_vu2_pdf_api import DjVu2PDFApi
from aspose_ocr_cloud.apis.tags.identify_font_api import IdentifyFontApi
from aspose_ocr_cloud.apis.tags.image_processing_api import ImageProcessingApi
from aspose_ocr_cloud.apis.tags.recognize_and_parse_invoice_api import RecognizeAndParseInvoiceApi
from aspose_ocr_cloud.apis.tags.recognize_image_api import RecognizeImageApi
from aspose_ocr_cloud.apis.tags.recognize_label_api import RecognizeLabelApi
from aspose_ocr_cloud.apis.tags.recognize_pdf_api import RecognizePdfApi
from aspose_ocr_cloud.apis.tags.recognize_receipt_api import RecognizeReceiptApi
from aspose_ocr_cloud.apis.tags.recognize_regions_api import RecognizeRegionsApi
from aspose_ocr_cloud.apis.tags.recognize_table_api import RecognizeTableApi
from aspose_ocr_cloud.apis.tags.text_to_speech_api import TextToSpeechApi
from aspose_ocr_cloud.apis.tags.upscale_image_api import UpscaleImageApi
from aspose_ocr_cloud.apis.tags.utilities_api import UtilitiesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BINARIZE_IMAGE: BinarizeImageApi,
        TagValues.CONVERT_TEXT_TO_SPEECH: ConvertTextToSpeechApi,
        TagValues.CONVERT_TEXT_TO_SPEECH_TRIAL: ConvertTextToSpeechTrialApi,
        TagValues.DESKEW_IMAGE: DeskewImageApi,
        TagValues.DETECT_REGIONS: DetectRegionsApi,
        TagValues.DEWARP_IMAGE: DewarpImageApi,
        TagValues.DJ_VU2PDF: DjVu2PDFApi,
        TagValues.IDENTIFY_FONT: IdentifyFontApi,
        TagValues.IMAGE_PROCESSING: ImageProcessingApi,
        TagValues.RECOGNIZE_AND_PARSE_INVOICE: RecognizeAndParseInvoiceApi,
        TagValues.RECOGNIZE_IMAGE: RecognizeImageApi,
        TagValues.RECOGNIZE_LABEL: RecognizeLabelApi,
        TagValues.RECOGNIZE_PDF: RecognizePdfApi,
        TagValues.RECOGNIZE_RECEIPT: RecognizeReceiptApi,
        TagValues.RECOGNIZE_REGIONS: RecognizeRegionsApi,
        TagValues.RECOGNIZE_TABLE: RecognizeTableApi,
        TagValues.TEXT_TO_SPEECH: TextToSpeechApi,
        TagValues.UPSCALE_IMAGE: UpscaleImageApi,
        TagValues.UTILITIES: UtilitiesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BINARIZE_IMAGE: BinarizeImageApi,
        TagValues.CONVERT_TEXT_TO_SPEECH: ConvertTextToSpeechApi,
        TagValues.CONVERT_TEXT_TO_SPEECH_TRIAL: ConvertTextToSpeechTrialApi,
        TagValues.DESKEW_IMAGE: DeskewImageApi,
        TagValues.DETECT_REGIONS: DetectRegionsApi,
        TagValues.DEWARP_IMAGE: DewarpImageApi,
        TagValues.DJ_VU2PDF: DjVu2PDFApi,
        TagValues.IDENTIFY_FONT: IdentifyFontApi,
        TagValues.IMAGE_PROCESSING: ImageProcessingApi,
        TagValues.RECOGNIZE_AND_PARSE_INVOICE: RecognizeAndParseInvoiceApi,
        TagValues.RECOGNIZE_IMAGE: RecognizeImageApi,
        TagValues.RECOGNIZE_LABEL: RecognizeLabelApi,
        TagValues.RECOGNIZE_PDF: RecognizePdfApi,
        TagValues.RECOGNIZE_RECEIPT: RecognizeReceiptApi,
        TagValues.RECOGNIZE_REGIONS: RecognizeRegionsApi,
        TagValues.RECOGNIZE_TABLE: RecognizeTableApi,
        TagValues.TEXT_TO_SPEECH: TextToSpeechApi,
        TagValues.UPSCALE_IMAGE: UpscaleImageApi,
        TagValues.UTILITIES: UtilitiesApi,
    }
)
