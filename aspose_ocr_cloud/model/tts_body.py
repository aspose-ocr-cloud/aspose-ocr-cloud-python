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


class TTSBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "settings",
            "text",
        }
        
        class properties:
            
            
            class text(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
        
            @staticmethod
            def settings() -> typing.Type['TTSSettings']:
                return TTSSettings
            __annotations__ = {
                "text": text,
                "settings": settings,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    settings: 'TTSSettings'
    text: MetaOapg.properties.text
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'TTSSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["settings"], typing_extensions.Literal["text"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> 'TTSSettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["settings"], typing_extensions.Literal["text"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        settings: 'TTSSettings',
        text: typing.Union[MetaOapg.properties.text, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TTSBody':
        return super().__new__(
            cls,
            *_args,
            settings=settings,
            text=text,
            _configuration=_configuration,
        )

from aspose_ocr_cloud.model.tts_settings import TTSSettings