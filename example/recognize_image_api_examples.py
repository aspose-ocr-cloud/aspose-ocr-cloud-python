import aspose_ocr_cloud
import base64
import os
import utils

from aspose_ocr_cloud.configuration import Configuration
from aspose_ocr_cloud.api import recognize_image_api
from aspose_ocr_cloud.models.problem_details import ProblemDetails
from aspose_ocr_cloud.models.ocr_recognize_image_body import OCRRecognizeImageBody
from aspose_ocr_cloud.models.ocr_settings_recognize_image import OCRSettingsRecognizeImage
from aspose_ocr_cloud.models.language import Language
from aspose_ocr_cloud.models.dsr_mode import DsrMode
from aspose_ocr_cloud.models.dsr_confidence import DsrConfidence
from aspose_ocr_cloud.models.result_type import ResultType
from aspose_ocr_cloud.models.ocr_region import OCRRegion
from aspose_ocr_cloud.models.ocr_rect import OCRRect
from aspose_ocr_cloud.models.ocr_response import OCRResponse


def run_recognize_image_demo(config: Configuration):

    with aspose_ocr_cloud.ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = recognize_image_api.RecognizeImageApi(api_client)

        # Read image file and conver it into base64 string
        image_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../samples/latin.png')

        # Create request body
        body = OCRRecognizeImageBody(
            image=utils.file_to_base64(image_file_path),
            settings=OCRSettingsRecognizeImage(
                language=Language("English"),
                makeSkewCorrect=False,
                makeBinarization=False,
                makeSpellCheck=False,
                makeContrastCorrection=False,
                makeUpsampling=False,
                dsrMode=DsrMode("NoDsrNoFilter"),
                dsrConfidence=DsrConfidence("Default"),
                resultType=ResultType("Text")
            ),
        )
        try:
            # Step 1: perform post request
            task_id = api_instance.post_recognize_image(
                body,
            )
            print(f'Your task ID is {task_id}')

            # Step 2: perform get result request
            task_response : OCRResponse = api_instance.get_recognize_image(
                id=task_id
            )
            assert task_response.response_status_code == 'Ok'
            assert task_response.task_status == 'Completed'
            recognized_text_raw = task_response.results[0].data
            recognized_text = bytearray(base64.b64decode(str(recognized_text_raw))).decode('utf-8')
            print (f'Recognized text:\n{recognized_text}')
            print (f'Task completed.Press Enter to continue')
            input()

        except aspose_ocr_cloud.ApiException as e:
            print("Exception when calling RecognizeImageApi: %s\n" % e)

