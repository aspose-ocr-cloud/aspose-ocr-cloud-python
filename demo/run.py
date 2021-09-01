from asposeocrcloud.configuration import Configuration
from asposeocrcloud.api.ocr_api import OcrApi
from asposeocrcloud.utils import Parameters, LanguageGroup, ResultType, DSRPipeline, DSRConfidence


def demo():
    configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                                  appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")

    recognize_from_content(configuration)
    recognize_from_url(configuration)
    # recognize_from_storage(configuration)


def recognize_from_content(conf):
    api = OcrApi(conf)
    params = Parameters(LanguageGroup.ENGLISH, ResultType.Text, False, False, DSRPipeline.DsrNoFilter,
                        DSRConfidence.Mid, False)

    res = api.post_recognize_from_content(
        'testdata/5.png', params)
    print(res.text)


def recognize_from_url(conf):
    api = OcrApi(conf)
    params = Parameters(LanguageGroup.ENGLISH, ResultType.Text, False, False, DSRPipeline.DsrNoFilter,
                        DSRConfidence.Mid, False)

    res = api.post_recognize_from_url(
        "https://www.cs.uregina.ca/Links/class-info/425-nova/Lab4/Picts/enhance_text.jpg", params)

    print(res.text)


def recognize_from_storage(conf):
    api = OcrApi(conf)
    params = Parameters(LanguageGroup.ENGLISH, ResultType.Text, False, False, DSRPipeline.DsrNoFilter,
                        DSRConfidence.Mid, False)

    res = api.get_recognize_from_storage(params,
                                         "file.png")
    print(res.text)


if __name__ == '__main__':
    demo()

