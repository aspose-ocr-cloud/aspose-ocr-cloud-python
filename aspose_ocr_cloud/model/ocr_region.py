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


class OCRRegion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents information about strict regions to recognize text
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def rect() -> typing.Type['OCRRect']:
                return OCRRect
            order = schemas.Int32Schema
            __annotations__ = {
                "rect": rect,
                "order": order,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rect"]) -> 'OCRRect': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rect"], typing_extensions.Literal["order"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rect"]) -> typing.Union['OCRRect', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rect"], typing_extensions.Literal["order"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        rect: typing.Union['OCRRect', schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OCRRegion':
        return super().__new__(
            cls,
            *_args,
            rect=rect,
            order=order,
            _configuration=_configuration,
        )

from aspose_ocr_cloud.model.ocr_rect import OCRRect
