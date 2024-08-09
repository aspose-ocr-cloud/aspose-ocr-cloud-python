import aspose_ocr_cloud
import utils

from aspose_ocr_cloud.api import convert_text_to_speech_trial_api
from aspose_ocr_cloud.configuration import Configuration
from aspose_ocr_cloud.models.tts_response import TTSResponse
from aspose_ocr_cloud.models.tts_body import TTSBody
from aspose_ocr_cloud.models.tts_settings import TTSSettings
from aspose_ocr_cloud.models.language_tts import LanguageTTS
from aspose_ocr_cloud.models.result_type_tts import ResultTypeTTS


def run_convert_text_to_speech_trial_demo(config: Configuration):    
    with aspose_ocr_cloud.ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = convert_text_to_speech_trial_api.ConvertTextToSpeechTrialApi(api_client)

        source_text = "This is a convert text to speech trial API test"

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
            task_id = api_instance.post_convert_text_to_speech_trial(
                tts_body=body,
            )
            print(f'Your task ID is {task_id}')

            # Step 2: perform get result request
            task_response : TTSResponse = api_instance.get_convert_text_to_speech_trial(
                id=task_id
            )
            assert task_response.response_status_code == 'Ok'
            assert task_response.task_status == 'Completed'
            sound_bytes = utils.base64_bytes_to_bytes(task_response.results[0].data)
            with open(f"results/{task_id}.wav", "wb") as file:
                file.write(sound_bytes)
            print (f'Result saved to results/{task_id}.wav\nTask completed.Press Enter to continue')
            input()

        except aspose_ocr_cloud.ApiException as e:
            print("Exception when calling ConvertTextToSpeechApi: %s\n" % e)