

def demo():
    from asposeocrcloud.configuration import Configuration
    from asposeocrcloud.api.ocr_api import OcrApi
    configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                                  appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")
    api = OcrApi(configuration)

    res = api.post_recognize_from_url("https://upload.wikimedia.org/wikipedia/commons/2/2f/Book_of_Abraham_FirstPage.png")
    print(res.text)


if __name__ == '__main__':
    demo()
