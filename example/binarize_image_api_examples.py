import aspose_ocr_cloud
import base64
import os
import utils

from aspose_ocr_cloud.configuration import Configuration
from aspose_ocr_cloud.apis.tags import binarize_image_api
from aspose_ocr_cloud.model.ocr_binarize_image_body import OCRBinarizeImageBody
from aspose_ocr_cloud.model.ocr_response import OCRResponse


def run_binarize_image_demo(config: Configuration):

    with aspose_ocr_cloud.ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = binarize_image_api.BinarizeImageApi(api_client)

        # Read image file and conver it into base64 string
        image_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../samples/binarization_latin.png')

        # Create request body
        body = OCRBinarizeImageBody(
            image=utils.file_to_base64(image_file_path)
            )
        try:
            # Step 1: perform post request
            task_id_response = api_instance.post_binarize_image(
                body=body,
            )
            task_id = task_id_response.body
            print(f'Your task ID is {task_id}')

            # Step 2: perform get result request
            task_response : OCRResponse = api_instance.get_binarize_image(
                query_params={'id':task_id}
            )
            assert task_response.response.status == 200
            assert task_response.body['taskStatus'] == 'Completed'
            binarized_image_bytes = utils.base64_bytes_to_bytes(task_response.body['results'][0]['data'])
            with open(f"results/{task_id}.png", "wb") as file:
                file.write(binarized_image_bytes)
            print (f'Result saved to results/{task_id}.png\nTask completed.Press Enter to continue')
            input()

        except aspose_ocr_cloud.ApiException as e:
            print("Exception when calling BinarizeImageApi: %s\n" % e)

