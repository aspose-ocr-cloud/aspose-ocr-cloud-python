# coding: utf-8

"""
    Aspose OCR Cloud 5.0 API

    Aspose OCR Cloud 5.0 API

    The version of the OpenAPI document: 5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ResultTypeTable(str, Enum):
    """
    Result document type for Table OCR process
    """

    """
    allowed enum values
    """
    TEXT = 'Text'
    EXCEL = 'Excel'
    CSV = 'Csv'
    CSVANDEXCEL = 'CsvAndExcel'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResultTypeTable from a JSON string"""
        return cls(json.loads(json_str))


