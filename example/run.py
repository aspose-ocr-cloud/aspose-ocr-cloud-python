import recognize_image_api_examples
import binarize_image_api_examples
import convert_text_to_speech_examples
import convert_text_to_speech_trial_examples
import recognize_image_trial_examples
import utils

from aspose_ocr_cloud.configuration import Configuration


def run_demo():
    utils.create_results_dir()

    config_trial = Configuration()
    convert_text_to_speech_trial_examples.run_convert_text_to_speech_trial_demo(config_trial)
    recognize_image_trial_examples.run_recognize_image_trial_demo(config_trial)

    config = Configuration(client_id='YOUR_CLIENT_ID', \
                           client_secret='YOUR_CLIENT_SECRET')
    
    recognize_image_api_examples.run_recognize_image_demo(config)
    binarize_image_api_examples.run_binarize_image_demo(config)
    convert_text_to_speech_examples.run_convert_text_to_speech_demo(config)


if __name__ == '__main__':
    run_demo()
