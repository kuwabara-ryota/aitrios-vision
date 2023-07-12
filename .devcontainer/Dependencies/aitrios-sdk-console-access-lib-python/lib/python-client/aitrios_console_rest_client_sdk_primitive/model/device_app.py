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


class DeviceApp(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            
            
            class versions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                version = schemas.StrSchema
                                compiled_flg = schemas.StrSchema
                                status = schemas.StrSchema
                                comment = schemas.StrSchema
                                deploy_count = schemas.StrSchema
                                ins_id = schemas.StrSchema
                                ins_date = schemas.StrSchema
                                upd_id = schemas.StrSchema
                                upd_date = schemas.StrSchema
                                __annotations__ = {
                                    "version": version,
                                    "compiled_flg": compiled_flg,
                                    "status": status,
                                    "comment": comment,
                                    "deploy_count": deploy_count,
                                    "ins_id": ins_id,
                                    "ins_date": ins_date,
                                    "upd_id": upd_id,
                                    "upd_date": upd_date,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["compiled_flg"]) -> MetaOapg.properties.compiled_flg: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["deploy_count"]) -> MetaOapg.properties.deploy_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "compiled_flg", "status", "comment", "deploy_count", "ins_id", "ins_date", "upd_id", "upd_date", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["compiled_flg"]) -> typing.Union[MetaOapg.properties.compiled_flg, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["deploy_count"]) -> typing.Union[MetaOapg.properties.deploy_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ins_id"]) -> typing.Union[MetaOapg.properties.ins_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ins_date"]) -> typing.Union[MetaOapg.properties.ins_date, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["upd_id"]) -> typing.Union[MetaOapg.properties.upd_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["upd_date"]) -> typing.Union[MetaOapg.properties.upd_date, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "compiled_flg", "status", "comment", "deploy_count", "ins_id", "ins_date", "upd_id", "upd_date", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
                            compiled_flg: typing.Union[MetaOapg.properties.compiled_flg, str, schemas.Unset] = schemas.unset,
                            status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                            comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
                            deploy_count: typing.Union[MetaOapg.properties.deploy_count, str, schemas.Unset] = schemas.unset,
                            ins_id: typing.Union[MetaOapg.properties.ins_id, str, schemas.Unset] = schemas.unset,
                            ins_date: typing.Union[MetaOapg.properties.ins_date, str, schemas.Unset] = schemas.unset,
                            upd_id: typing.Union[MetaOapg.properties.upd_id, str, schemas.Unset] = schemas.unset,
                            upd_date: typing.Union[MetaOapg.properties.upd_date, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                version=version,
                                compiled_flg=compiled_flg,
                                status=status,
                                comment=comment,
                                deploy_count=deploy_count,
                                ins_id=ins_id,
                                ins_date=ins_date,
                                upd_id=upd_id,
                                upd_date=upd_date,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'versions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "versions": versions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "versions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versions"]) -> typing.Union[MetaOapg.properties.versions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "versions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        versions: typing.Union[MetaOapg.properties.versions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceApp':
        return super().__new__(
            cls,
            *args,
            name=name,
            versions=versions,
            _configuration=_configuration,
            **kwargs,
        )
