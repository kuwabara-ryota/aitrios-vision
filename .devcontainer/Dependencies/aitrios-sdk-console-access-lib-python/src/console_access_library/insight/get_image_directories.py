# ------------------------------------------------------------------------
# Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=unused-argument
# pylint:disable=redefined-builtin
# pylint:disable=too-many-arguments
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=broad-except

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaGetImageDirectories(Schema):
    """Schema for API for GetImageDirectories.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, optional : Device ID.
    device_id = fields.String(
        required=False, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if "device_id" in data and (
            data["device_id"] is None or str(data["device_id"]).strip() == ""
        ):
            raise ValidationError("device_id is required or can't be empty string")


class GetImageDirectories(ConsoleAccessBaseClass):
    """This class implements API for each device group, a list of image storage \
        directories for each device is acquired.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetImageDirectories

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_image_directories(self, device_id: str = None):
        """Image storage directory list retrieval API. For each device group, a list of image \
        storage directories for each device is acquired.

        Args:
            device_id (str, optional): Device ID \
                If specified, the image directory list associated with the specified \
                device ID is returned. Case-sensitive

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------------+------------+------------+-------------------------------+
                | *Level1*         | *Level2*   | *Type*     | *Description*                 |
                +------------------+------------+------------+-------------------------------+
                | ``No_item_name`` |            |            | Device Affiliation Group Array|
                +------------------+------------+------------+-------------------------------+
                |                  |``group_id``| ``string`` | Set the device group ID.      |
                +------------------+------------+------------+-------------------------------+
                |                  | ``devices``| ``array``  | Refer :ref:`devices <devices>`|
                |                  |            |            | for more details              |
                +------------------+------------+------------+-------------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | devices           | .. _devices:                                               |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +-------------------+--------------------+------------+--------------------------+
                | ``devices``       |  ``array``         |            | Device Array.            |
                |                   |                    |            | The subordinate          |
                |                   |                    |            | elements are listed      |
                |                   |                    |            | in ascending order       |
                |                   |                    |            | by device ID             |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_id``       | ``string`` | Device ID.               |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_name``     | ``string`` | Device name at the time  |
                |                   |                    |            | of registration          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``Image``           | ``array``  | The descendant elements  |
                |                   |                    |            | are listed in ascending  |
                |                   |                    |            | order by directory name. |
                +-------------------+--------------------+------------+--------------------------+

            **Error Response Schema**

                - **Generic Error Response** :

                    If Any generic error returned from the Low Level SDK
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Generic Error"
                    - ``datetime`` (str) : Time

                - **Validation Error Response** :

                    If incorrect API input parameters OR
                    if any input string parameter found empty.
                    Then, Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : validation error message for respective input parameter
                    - ``code`` (str) : "E001"
                    - ``datetime`` (str) : Time

                - **Key Error Response** :

                    If API key error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Key Error"
                    - ``datetime`` (str) : Time

                - **Type Error Response** :

                    If API type error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Type Error"
                    - ``datetime`` (str) : Time

                - **Attribute Error Response** :

                    If API attribute error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Attribute Error"
                    - ``datetime`` (str) : Time

                - **Value Error Response** :

                    If API value error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Value Error"
                    - ``datetime`` (str) : Time

                - **HTTP Error Response** :

                    If the API http_status returned from the Console Server
                    is other than 200. Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Console server.
                    - ``code`` (str) : error code received from the Console server.
                    - ``datetime`` (str) : Time

        Example:
            .. code-block:: python

                import os
                import sys
                from pprint import pprint

                from console_access_library.client import Client
                from console_access_library.common.config import Config
                from console_access_library.common.read_console_access_settings
                import ReadConsoleAccessSettings

                # For Console Access Library API Usage,
                # edit console access setting configuration parameters with real values.
                # file_path: samples/console_access_settings.yaml
                # console_access_settings:
                #     console_endpoint: "__console_endpoint__"
                #     portal_authorization_endpoint: "__portal_authorization_endpoint__"
                #     client_secret: "__client_secret__"
                #     client_id: "__client_id__"

                # Set path for Console Access Library Setting File.
                SETTING_FILE_PATH = os.path.join(os.getcwd(),
                                                 "samples",
                                                 "console_access_settings.yaml")

                # Instantiate Console Access Library ReadConsoleAccessSettings.
                read_console_access_settings_obj = ReadConsoleAccessSettings(SETTING_FILE_PATH)

                # Instantiate Console Access Library Config.
                config_obj = Config(
                    read_console_access_settings_obj.console_endpoint,
                    read_console_access_settings_obj.portal_authorization_endpoint,
                    read_console_access_settings_obj.client_id,
                    read_console_access_settings_obj.client_secret
                )

                # Instantiate Console Access Library Client.
                client_obj = Client(config_obj)

                # Create Instance for Insight
                insight_obj = client_obj.get_insight()

                # set the real value
                device_id = "__device_id__"

                # Insight - GetImageDirectories
                response = insight_obj.get_image_directories(device_id)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            if "device_id" in _local_params and _local_params["device_id"] is None:
                del _local_params["device_id"]

            # Validate schema
            _local_params = SchemaGetImageDirectories().load(_local_params)

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                insight_api_api_instance = insight_api.InsightApi(api_client)

                try:
                    _return_get_image_directories = insight_api_api_instance.get_image_directories(
                        query_params=_local_params
                    )
                    return _return_get_image_directories.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_image_directories = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_image_directories = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_image_directories = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_image_directories = self.on_attribute_error_response(
                        __name__, attr_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_image_directories = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_get_image_directories = self.on_generic_error_response(
                        __name__, exception
                    )

        except ValidationError as err:
            _return_get_image_directories = self.on_validation_error_response(__name__, err)

        return _return_get_image_directories