import aspose_ocr_cloud
import utils

from aspose_ocr_cloud.apis.tags import convert_text_to_speech_api
from aspose_ocr_cloud.configuration import Configuration
from aspose_ocr_cloud.model.tts_response import TTSResponse
from aspose_ocr_cloud.model.tts_body import TTSBody
from aspose_ocr_cloud.model.tts_settings import TTSSettings
from aspose_ocr_cloud.model.language_tts import LanguageTTS
from aspose_ocr_cloud.model.result_type_tts import ResultTypeTTS


def run_convert_text_to_speech_demo(config: Configuration):    
    with aspose_ocr_cloud.ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = convert_text_to_speech_api.ConvertTextToSpeechApi(api_client)

        source_text = "This is a convert text to speech API test"

        # Create request body
        body = TTSBody(
            text = source_text,
            settings = TTSSettings(
                language = LanguageTTS.ENGLISH,
                resultType = ResultTypeTTS.WAV
                )
            )
        
        try:
            # Step 1: perform post request
            task_id_response = api_instance.post_convert_text_to_speech(
                body=body,
            )
            task_id = task_id_response.body
            print(f'Your task ID is {task_id}')

            # Step 2: perform get result request
            task_response : TTSResponse = api_instance.get_convert_text_to_speech(
                query_params={'id':task_id}
            )
            assert task_response.response.status == 200
            assert task_response.body['taskStatus'] == 'Completed'
            sound_bytes = utils.base64_bytes_to_bytes(task_response.body['results'][0]['data'])
            with open(f"results/{task_id}.wav", "wb") as file:
                file.write(sound_bytes)
            print (f'Result saved to results/{task_id}.wav\nTask completed.Press Enter to continue')
            input()

        except aspose_ocr_cloud.ApiException as e:
            print("Exception when calling ConvertTextToSpeechApi: %s\n" % e)