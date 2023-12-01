# coding: utf-8

"""
    Aspose OCR Cloud 5.0 API

    Aspose OCR Cloud 5.0 API  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from aspose_ocr_cloud import schemas  # noqa: F401


class OCRSettingsRecognizePdf(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    OCR Process setting for Scanned multiple PDF document recognition
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def language() -> typing.Type['Language']:
                return Language
            makeSkewCorrect = schemas.BoolSchema
            makeSpellCheck = schemas.BoolSchema
            makeContrastCorrection = schemas.BoolSchema
        
            @staticmethod
            def dsrMode() -> typing.Type['DsrMode']:
                return DsrMode
        
            @staticmethod
            def dsrConfidence() -> typing.Type['DsrConfidence']:
                return DsrConfidence
        
            @staticmethod
            def resultType() -> typing.Type['ResultType']:
                return ResultType
            Rotate = schemas.Int32Schema
            makeBinarization = schemas.BoolSchema
            makeUpsampling = schemas.BoolSchema
        
            @staticmethod
            def resultTypeTable() -> typing.Type['ResultTypeTable']:
                return ResultTypeTable
            
            
            class regions(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OCRRegion']:
                        return OCRRegion
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regions':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "language": language,
                "makeSkewCorrect": makeSkewCorrect,
                "makeSpellCheck": makeSpellCheck,
                "makeContrastCorrection": makeContrastCorrection,
                "dsrMode": dsrMode,
                "dsrConfidence": dsrConfidence,
                "resultType": resultType,
                "Rotate": Rotate,
                "makeBinarization": makeBinarization,
                "makeUpsampling": makeUpsampling,
                "resultTypeTable": resultTypeTable,
                "regions": regions,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> 'Language': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["makeSkewCorrect"]) -> MetaOapg.properties.makeSkewCorrect: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["makeSpellCheck"]) -> MetaOapg.properties.makeSpellCheck: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["makeContrastCorrection"]) -> MetaOapg.properties.makeContrastCorrection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dsrMode"]) -> 'DsrMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dsrConfidence"]) -> 'DsrConfidence': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resultType"]) -> 'ResultType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rotate"]) -> MetaOapg.properties.Rotate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["makeBinarization"]) -> MetaOapg.properties.makeBinarization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["makeUpsampling"]) -> MetaOapg.properties.makeUpsampling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resultTypeTable"]) -> 'ResultTypeTable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regions"]) -> MetaOapg.properties.regions: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["language"], typing_extensions.Literal["makeSkewCorrect"], typing_extensions.Literal["makeSpellCheck"], typing_extensions.Literal["makeContrastCorrection"], typing_extensions.Literal["dsrMode"], typing_extensions.Literal["dsrConfidence"], typing_extensions.Literal["resultType"], typing_extensions.Literal["Rotate"], typing_extensions.Literal["makeBinarization"], typing_extensions.Literal["makeUpsampling"], typing_extensions.Literal["resultTypeTable"], typing_extensions.Literal["regions"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union['Language', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["makeSkewCorrect"]) -> typing.Union[MetaOapg.properties.makeSkewCorrect, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["makeSpellCheck"]) -> typing.Union[MetaOapg.properties.makeSpellCheck, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["makeContrastCorrection"]) -> typing.Union[MetaOapg.properties.makeContrastCorrection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dsrMode"]) -> typing.Union['DsrMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dsrConfidence"]) -> typing.Union['DsrConfidence', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resultType"]) -> typing.Union['ResultType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rotate"]) -> typing.Union[MetaOapg.properties.Rotate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["makeBinarization"]) -> typing.Union[MetaOapg.properties.makeBinarization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["makeUpsampling"]) -> typing.Union[MetaOapg.properties.makeUpsampling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resultTypeTable"]) -> typing.Union['ResultTypeTable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regions"]) -> typing.Union[MetaOapg.properties.regions, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["language"], typing_extensions.Literal["makeSkewCorrect"], typing_extensions.Literal["makeSpellCheck"], typing_extensions.Literal["makeContrastCorrection"], typing_extensions.Literal["dsrMode"], typing_extensions.Literal["dsrConfidence"], typing_extensions.Literal["resultType"], typing_extensions.Literal["Rotate"], typing_extensions.Literal["makeBinarization"], typing_extensions.Literal["makeUpsampling"], typing_extensions.Literal["resultTypeTable"], typing_extensions.Literal["regions"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        language: typing.Union['Language', schemas.Unset] = schemas.unset,
        makeSkewCorrect: typing.Union[MetaOapg.properties.makeSkewCorrect, bool, schemas.Unset] = schemas.unset,
        makeSpellCheck: typing.Union[MetaOapg.properties.makeSpellCheck, bool, schemas.Unset] = schemas.unset,
        makeContrastCorrection: typing.Union[MetaOapg.properties.makeContrastCorrection, bool, schemas.Unset] = schemas.unset,
        dsrMode: typing.Union['DsrMode', schemas.Unset] = schemas.unset,
        dsrConfidence: typing.Union['DsrConfidence', schemas.Unset] = schemas.unset,
        resultType: typing.Union['ResultType', schemas.Unset] = schemas.unset,
        Rotate: typing.Union[MetaOapg.properties.Rotate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        makeBinarization: typing.Union[MetaOapg.properties.makeBinarization, bool, schemas.Unset] = schemas.unset,
        makeUpsampling: typing.Union[MetaOapg.properties.makeUpsampling, bool, schemas.Unset] = schemas.unset,
        resultTypeTable: typing.Union['ResultTypeTable', schemas.Unset] = schemas.unset,
        regions: typing.Union[MetaOapg.properties.regions, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OCRSettingsRecognizePdf':
        return super().__new__(
            cls,
            *_args,
            language=language,
            makeSkewCorrect=makeSkewCorrect,
            makeSpellCheck=makeSpellCheck,
            makeContrastCorrection=makeContrastCorrection,
            dsrMode=dsrMode,
            dsrConfidence=dsrConfidence,
            resultType=resultType,
            Rotate=Rotate,
            makeBinarization=makeBinarization,
            makeUpsampling=makeUpsampling,
            resultTypeTable=resultTypeTable,
            regions=regions,
            _configuration=_configuration,
        )

from aspose_ocr_cloud.model.dsr_confidence import DsrConfidence
from aspose_ocr_cloud.model.dsr_mode import DsrMode
from aspose_ocr_cloud.model.language import Language
from aspose_ocr_cloud.model.ocr_region import OCRRegion
from aspose_ocr_cloud.model.result_type import ResultType
from aspose_ocr_cloud.model.result_type_table import ResultTypeTable
