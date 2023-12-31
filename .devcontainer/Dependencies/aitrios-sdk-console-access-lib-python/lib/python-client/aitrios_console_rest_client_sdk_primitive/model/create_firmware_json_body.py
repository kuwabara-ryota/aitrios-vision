# coding: utf-8

"""
    AITRIOS | Console

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
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

from aitrios_console_rest_client_sdk_primitive import schemas  # noqa: F401


class CreateFirmwareJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CreateFirmware API model
    """


    class MetaOapg:
        
        class properties:
            firmware_type = schemas.StrSchema
            version_number = schemas.StrSchema
            comment = schemas.StrSchema
            file_name = schemas.StrSchema
            file_content = schemas.StrSchema
            __annotations__ = {
                "firmware_type": firmware_type,
                "version_number": version_number,
                "comment": comment,
                "file_name": file_name,
                "file_content": file_content,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware_type"]) -> MetaOapg.properties.firmware_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firmware_type", "version_number", "comment", "file_name", "file_content", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware_type"]) -> typing.Union[MetaOapg.properties.firmware_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_number"]) -> typing.Union[MetaOapg.properties.version_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> typing.Union[MetaOapg.properties.file_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_content"]) -> typing.Union[MetaOapg.properties.file_content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firmware_type", "version_number", "comment", "file_name", "file_content", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firmware_type: typing.Union[MetaOapg.properties.firmware_type, str, schemas.Unset] = schemas.unset,
        version_number: typing.Union[MetaOapg.properties.version_number, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        file_name: typing.Union[MetaOapg.properties.file_name, str, schemas.Unset] = schemas.unset,
        file_content: typing.Union[MetaOapg.properties.file_content, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateFirmwareJsonBody':
        return super().__new__(
            cls,
            *args,
            firmware_type=firmware_type,
            version_number=version_number,
            comment=comment,
            file_name=file_name,
            file_content=file_content,
            _configuration=_configuration,
            **kwargs,
        )
