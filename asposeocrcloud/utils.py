import enum
from enum import Enum, IntFlag, unique


@unique
class SupportedPipelines(Enum):
    TESSERACT = 1
    ASPOSE_CLOUD = 2
    DSR_STEP_1 = 3
    DSR_STEP_2 = 4
    KEEP_ALIVE_CHECK = 5
    RECEIPT_FULL = 6
    RECOGNIZE_PDF = 7
    CRAFT_TABLES = 8


@unique
class LanguageGroup(Enum):
    ENGLISH = 1
    GERMAN = 2
    FRENCH = 3
    ITALIAN = 4
    SPANISH = 5
    PORTUGUESE = 6
    POLISH = 7
    SLOVENE = 8
    SLOVAK = 9
    NETHERLANDS = 10
    LITHUANIAN = 11
    LATVIAN = 12
    DANISH = 13
    NORWEGIAN = 14
    FINNISH = 15
    SERBIAN = 16
    CROATIAN = 17
    CZECH = 18
    SWEDISH = 19
    ESTONIAN = 20
    ROMANIAN = 21
    CHINESE = 22
    RUSSIAN = 23
    ARABIC = 24
    HINDI = 25
    UKRAINIAN = 26
    BENGALI = 27
    TIBETAN = 28
    THAI = 29
    URDU = 30
    TURKISH = 31
    KOREAN = 32
    INDONESIAN = 33
    HEBREW = 34
    JAVANESE = 35
    GREEK = 36
    JAPANESE = 37
    PERSIAN = 38


@unique
class TaskStatuses(Enum):
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3


@unique
class ResultType(IntFlag):
    Text = 1
    PDF = 2
    hOCR = 4
    Internal = 8


@unique
class DSRConfidence(Enum):
    Default = 0
    Low = 1
    LowMid = 2
    Mid = 3
    MidHigh = 4
    High = 5
    Ultra = 6
    All = 7


@unique
class DSRPipeline(Enum):
    DsrNoFilter = 1
    DsrAndFilter = 2
    NoDSRnoFilter = 3
    TextDetector = 4
    DsrPlusDetector = 5


class Parameters:
    """Parameters for Aspose OCR"""
    def __init__(self, language: LanguageGroup, resultType: ResultType, skewCorrect: bool, spellCheck: bool,
                 dsrMode: DSRPipeline, dsrConfidence: DSRConfidence, makeContrastCorrection: bool):
        """
        Args:
            language: language to be recognized
            resultType: return type
            skewCorrect: enable skew correction module
            spellCheck: enable spell check
            dsrMode: select Document Structure Recognition mode
            dsrConfidence: DSR confidence
            makeContrastCorrection: enable auto contrast correction
        """
        self.language = language
        self.resultType = resultType
        self.skewCorrect = skewCorrect
        self.spellCheck = spellCheck
        self.dsrMode = dsrMode
        self.dsrConfidence = dsrConfidence
        self.makeContrastCorrection = makeContrastCorrection
