 23.11.0
# Aspose.OCR Cloud for Python SDK 23.11.0

![PyPI](https://img.shields.io/pypi/v/aspose-ocr-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-ocr-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-ocr-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-ocr-cloud/aspose-ocr-cloud-python)](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-ocr-Cloud/aspose-ocr-cloud-python)

[Aspose.OCR Cloud](https://products.aspose.cloud/ocr/) is an optical character recognition as a service. With it, you can easily add OCR functionality to almost any device or platform, including netbooks, mini PCs, or even entry-level smartphones.

Our engine can read text from images, photos, screenshots and scanned PDFs in a wide variety of European, Cyrillic and Oriental fonts, returning results in the most popular document formats. Powerful built-in image processing filters based on neural networks automatically correct skewed and distorted images, automatically remove dirt, smudges, scratches, glare and other image defects that can affect recognition accuracy. To further improve the results, Aspose.OCR Cloud has a built-in spell checker that automatically replaces misspelled words and saves you the trouble of manually correcting the recognition results.

Even the complex recognition tasks can be done with a couple of API calls. To make interacting with Aspose.OCR Cloud services from Python applications even easier, we provide the software development kit (SDK) for Python. It handles all the routine operations such as establishing connections, sending API requests, and parsing responses, wrapping all these tasks into a few simple classes.

Aspose.OCR Cloud SDK for Python is open source under the MIT license. You can freely use it for any projects, including commercial and proprietary applications, as well as modify any part of its code.

## Try Online
[Image to Text](https://products.aspose.app/ocr/scan-image) | [Image to Searchable PDF](https://products.aspose.app/ocr/ocr-to-pdf) | [PDF OCR](https://products.aspose.app/ocr/pdf-ocr)| [Receipt Scanner](https://products.aspose.app/ocr/scan-receipt)
:---: | :---: | :---:| :---:
[![Scan Image](https://products.aspose.app/ocr/scan-image/img/ocr-recognize-48.png)](https://products.aspose.app/ocr/scan-image) | [![Image to Searchable PDF](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-4-48.png)](https://products.aspose.app/ocr/ocr-to-pdf) | [![PDF OCR](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-2-48.png)](https://products.aspose.app/ocr/pdf-ocr) | [![Receipt Scanner](https://products.aspose.app/ocr/scan-image/img/aspose-scan-receipt-48.png)](https://products.aspose.app/ocr/scan-receipt) 

## What was changed in version 23.11.0

A summary of recent changes, enhancements and bug fixes in **Aspose.OCR Cloud SDK for Python 23.11.0** release:

Key | Summary | Category
--- | ------- | --------
OCR&#8209;3560 | Added an API for extracting structured information from scanned invoices. | New feature
OCR&#8209;3722 | Added a free API for evaluating text-to-speech conversion that works without [authorization](/ocr/authorization/).<br />Some restrictions apply. See below for details. | New feature
OCR&#8209;3171 | Added an API for getting [task status](/ocr/recognition-workflow/#3-fetch-the-recognition-result) without downloading a full recognition result. | Enhancement

REST API changes: https://releases.aspose.cloud/ocr/release-notes/2023/aspose-ocr-cloud-23-11-0-release-notes/

### Public API changes and backwards compatibility

This section lists all public API changes introduced in **Aspose.OCR Cloud SDK for Python 23.11.0** that may affect the code of existing applications.

#### Added public APIs:

The following public APIs have been introduced in this release:

##### Extracting structured information from invoice

The following new classes have been added for extracting structured information in JSON format from scanned or photographed invoices:

Class | Description
----- | -----------
`RecognizeAndParseInvoiceApi` | Invoice processing API.
`OCRSettingsRecognizeAndParseInvoice` | Invoice processing settings.
`OCRRecognizeAndParseInvoiceBody` | Invoice processing request body.

[Learn more...](https://docs.aspose.cloud/ocr/recognize-parse-invoice/)

##### Text-to-speech evaluation

The following new classes have been added:

Class | Description
----- | -----------
`ConvertTextToSpeechTrialApi` | Evaluation text-to-speech conversion API (without authorization).

The evaluation mode has some limitations:

- **10** requests per day from a single IP address.
- The text size must not exceed **500** characters, including spaces and punctuation.
- The phrase _"Please authenticate to the API to remove this message"_ is inserted at a random position within the generated audio.

[Learn more...](https://docs.aspose.cloud/ocr/text-to-speech/)

##### Quickly fetch processing status

The following new classes have been added:

Class | Description
----- | -----------
`UtilitiesApi` | Universal API for various management and monitoring purposes.

[Learn more...](https://docs.aspose.cloud/ocr/subscription/)

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
            task_id_response = api_instance.post_recognize_image(
                body=body,
            )
            task_id = task_id_response.body
            print(f'Your task ID is {task_id}')

            # Step 2: perform get result request
            task_response : OCRResponse = api_instance.get_recognize_image(
                query_params={'id':task_id}
            )
            assert task_response.response.status == 200
            assert task_response.body['taskStatus'] == 'Completed'
            recognized_text_raw = task_response.body['results'][0]['data']
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
- [See requirements.txt](./requirements.txt)
_________________________


## Aspose.OCR Cloud SDKs

||||||
|--------------|----------|-------|---------|---------|
|[.NET & Core](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-dotnet)|[Java](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-java)|[Python](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python)|[Node.js](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs)|[Android](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-android)


[Product Page](https://products.aspose.cloud/ocr/) | [Documentation](https://docs.aspose.cloud/display/ocrcloud/Home) | [API Reference](https://apireference.aspose.cloud/ocr/) | [Code Samples](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs) | [Blog](https://blog.aspose.cloud/category/ocr/) | [Free Support](https://forum.aspose.cloud/c/ocr) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
