# Aspose.OCR Cloud for Python SDK 24.11.0

![PyPI](https://img.shields.io/pypi/v/aspose-ocr-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-ocr-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-ocr-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-ocr-cloud/aspose-ocr-cloud-python)](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/blob/master/LICENSE)

[Aspose.OCR Cloud](https://products.aspose.cloud/ocr/) is an optical character recognition as a service. With it, you can easily add OCR functionality to almost any device or platform, including netbooks, mini PCs, or even entry-level smartphones.

Our engine can read text from images, photos, screenshots and scanned PDFs in a wide variety of European, Cyrillic and Oriental fonts, returning results in the most popular document formats. Powerful built-in image processing filters based on neural networks automatically correct skewed and distorted images, automatically remove dirt, smudges, scratches, glare and other image defects that can affect recognition accuracy. To further improve the results, Aspose.OCR Cloud has a built-in spell checker that automatically replaces misspelled words and saves you the trouble of manually correcting the recognition results.

Even the complex recognition tasks can be done with a couple of API calls. To make interacting with Aspose.OCR Cloud services from Python applications even easier, we provide the software development kit (SDK) for Python. It handles all the routine operations such as establishing connections, sending API requests, and parsing responses, wrapping all these tasks into a few simple classes.

Aspose.OCR Cloud SDK for Python is open source under the MIT license. You can freely use it for any projects, including commercial and proprietary applications, as well as modify any part of its code.

## Try Online
[Image to Text](https://products.aspose.app/ocr/scan-image) | [Image to Searchable PDF](https://products.aspose.app/ocr/ocr-to-pdf) | [PDF OCR](https://products.aspose.app/ocr/pdf-ocr)| [Receipt Scanner](https://products.aspose.app/ocr/scan-receipt)
:---: | :---: | :---:| :---:
[![Scan Image](https://products.aspose.app/ocr/scan-image/img/ocr-recognize-48.png)](https://products.aspose.app/ocr/scan-image) | [![Image to Searchable PDF](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-4-48.png)](https://products.aspose.app/ocr/ocr-to-pdf) | [![PDF OCR](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-2-48.png)](https://products.aspose.app/ocr/pdf-ocr) | [![Receipt Scanner](https://products.aspose.app/ocr/scan-image/img/aspose-scan-receipt-48.png)](https://products.aspose.app/ocr/scan-receipt) 


## What was changed in version 24.11.0


A summary of recent changes, enhancements and bug fixes in **Aspose.OCR Cloud SDK for Java 24.11.0** release:

Key | Summary | Category
--- | ------- | --------
OCR-3977 | Added recognition of the Uyghur language, including mixed Uyghur/English texts. | New feature
OCR-3978 | Added recognition of the Telugu language, including mixed Telugu/English texts. | New feature
OCR-3979 | Added recognition of the Kannada language, including mixed Kannada/English texts. | New feature
OCR-3980 | Added recognition of the Tamil language, including mixed Tamil/English texts. | New feature
OCR-3985 | Added recognition of the Devanagari-based scripts, including mixed Devanagari/English texts. | New feature
OCR-3986 | Added support for mixed Arabic/English texts. | Enhancement
OCR-3984 | Added support for mixed Japanese/English texts. | Enhancement
OCR-3983 | Added support for mixed Korean/English texts. | Enhancement
OCR-3982 | Added support for mixed Chinese/English texts. | Enhancement
OCR-3987 | Added support for mixed Persian/English texts. | Enhancement

REST API changes: https://releases.aspose.cloud/ocr/release-notes/2024/aspose-ocr-cloud-24-11-0-release-notes/

#### New recognition languages

The following recognition languages have been added:

Script     | REST API
---------- | --------
Uyghur     | `Language.Uyghur`
Telugu     | `Language.Telugu`
Kannada    | `Language.Kannada`
Tamil      | `Language.Tamil`
Devanagari-based languages | `Language.Devanagari`


All of the OCR languages mentioned above also support the recognition of mixed texts, including those with Latin characters.

### Mixed language support

Aspose.OCR Cloud now supports the recognition of texts which include both native and Latin characters for the following languages:

- Arabic (`Language.Arabic`)
- Chinese (`Language.Chinese`)
- Japanese (`Language.Japanese`)
- Korean (`Language.Korean`)
- Persian (`Language.Persian`)

#### Updated public APIs:

_No changes_

#### Removed public APIs:

_No changes._

## Quickstart

Make your solution using [SDK](#asposeocr-cloud-sdks), follow these steps:

#### 1. Get API keys if you haven't

Make a personal account on [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/) and click _Get Keys_. These keys are useful for all Aspose Cloud products. If you have any trouble, look at this [detailed manual](https://docs.aspose.cloud/total/create-new-app-and-get-app-key-and-sid/).

#### 2. Run Demo

  * Checkout the SDK or get from [pip](https://pypi.org/project/aspose-ocr-cloud/) (pip install aspose-ocr-cloud)
  * Set Your AppSid & AppKey
  * Run Python console [Demo](./Example/run.py)


<p align="center">
  <a title="Download ZIP" href="https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/archive/master.zip">
     <img src="testdata/download.png" />
  </a>
</p>

---------------------------


## OCR in Python

```python
# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).

	
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

```
_________________________

### Structure

This project includes:   
- Python console demo application - "[./example](./example/run.py)"
- Module "asposeocrcloud" - this is SDK located in "[./asposeocrcloud](asposeocrcloud)". You can integrate it in your application.
- Module "test" - "[./test](./test)" UnitTest. You can take a look at them to see various code examples.
- Folder "docs" - "[./docs](./docs)" Full documentation for Aspose.OCR SDK in HTML format.

### Dependencies
- Python 3.9
- [See requirements.txt](./requirements.txt)
_________________________


## Aspose.OCR Cloud SDKs

||||||
|--------------|----------|-------|---------|---------|
|[.NET & Core](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-dotnet)|[Java](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-java)|[Python](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python)|[Node.js](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs)|[Android](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-android)


[Product Page](https://products.aspose.cloud/ocr/) | [Documentation](https://docs.aspose.cloud/display/ocrcloud/Home) | [API Reference](https://apireference.aspose.cloud/ocr/) | [Code Samples](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs) | [Blog](https://blog.aspose.cloud/category/ocr/) | [Free Support](https://forum.aspose.cloud/c/ocr) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
