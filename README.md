![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-ocr-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-ocr-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-ocr-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-ocr-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-ocr-cloud/aspose-ocr-cloud-python)](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-ocr-Cloud/aspose-ocr-cloud-python)

# Python Cloud REST API for OCR
Aspose OCR Cloud Android SDK is a simple OCR technology, which you can use in your application to convert image to text.
[Aspose.OCR Cloud](https://products.aspose.cloud/ocr/cloud) is a simple SDK used to add text recognition to your app with merely a few lines of code.
In detail, it's a set of SDKs for optical character recognition and document scanning in our Cloud. It supports reading and recognizing text from most commonly used raster image formats. Just pass a specific image to the Aspose.OCR Cloud API, and it will return a response with recognized text.

It is easy to get started with Aspose.OCR Cloud, and there is nothing to install. Create an account at Aspose Cloud and get your application information, then you are ready to use [SDKs](#asposeocr-cloud-sdks)

## OCR Processing Features
- Recognize and extract text from images via OCR.
- Specify the area of the image from which you want to extract text.
- Perform OCR to recognize text from the whole or partial image.
- Fetch character and font information from raster images.
- Return the response in the JSON or XML format.
- Supports English text recognition.

## Save OCR As
TXT, PDF, HOCR

## Read OCR Formats
BMP, JPG, GIF, PNG, TIFF

## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](#asposeocr-cloud-sdks) in many development languages to make it easier to integrate with us.

## Examples

```python
from asposeocrcloud.configuration import Configuration
from asposeocrcloud.api.ocr_api import OcrApi
configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")
api = OcrApi(configuration)

file_path = r"\your\file\path\5.png"
res = api.post_recognize_from_content(file_path)
print(res.text)
```
_________________________

## Quickstart

Make your solution using [SDK](#asposeocr-cloud-sdks), follow these steps:

#### 1. Get API keys if you haven't

Make a personal account on [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/) and click _Get Keys_. These keys are useful for all Aspose Cloud products. If you have any trouble, look at this [detailed manual](https://docs.aspose.cloud/total/create-new-app-and-get-app-key-and-sid/).

#### 2. Run Demo

  * Checkout the SDK or get from [pip](https://pypi.org/project/aspose-ocr-cloud/) (pip install aspose-ocr-cloud)
  * Set Your AppSid & AppKey
  * Run Python console [Demo](./demo/run.py) or [UnitTests](./test/test_ocr_api.py)


<p align="center">
  <a title="Download ZIP" href="https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/archive/master.zip">
     <img src="testdata/download.png" />
  </a>
</p>

---------------------------

### Structure

This project includes:   
- Python console demo application - "[./demo](./demo/run.py)"
- Module "asposeocrcloud" - this is SDK located in "[./asposeocrcloud](asposeocrcloud)". You can integrate it in your application. It contains both OCR and [Aspose.Storage](https://github.com/aspose-storage-cloud/) API
- Module "test" - "[./test](./test)" UnitTest. You can take a look at them to see various code examples.
- Module "demo" - "[./demo](./demo)" Sample console demo project.
- Folder "docs" - "[./docs](./docs)" Full documentation for Aspose.OCR SDK in HTML format.

### Dependencies
- [See requirements.txt](./requirements.txt)
_________________________

## Aspose.OCR Cloud SDKs in Popular Languages

| .NET | Java | Python| Android |
|---|---|---|---|
| [GitHub](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-dotnet) |[GitHub](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-java) | [GitHub](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python)|[GitHub](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-android)|
| [NuGet](https://www.nuget.org/packages/Aspose.ocr-Cloud/)| [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-ocr-cloud) | [PIP](https://pypi.org/project/aspose-ocr-cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-ocr-cloud)) |

[Product Page](https://products.aspose.cloud/ocr/python) | [Documentation](https://docs.aspose.cloud/display/ocrcloud/Home) | [API Reference](https://apireference.aspose.cloud/ocr/) | [Code Samples](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python) | [Blog](https://blog.aspose.cloud/category/ocr/) | [Free Support](https://forum.aspose.cloud/c/ocr) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
