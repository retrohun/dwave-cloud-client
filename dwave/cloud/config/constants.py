# Copyright 2024 D-Wave Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration defaults.

.. versionchanged:: 0.13.1
   Some of these constants previously lived under ``dwave.cloud.api.constants``.

"""

__all__ = ['DEFAULT_METADATA_API_ENDPOINT', 'DEFAULT_REGION',
           'DEFAULT_SOLVER_API_ENDPOINT', 'DEFAULT_LEAP_API_ENDPOINT']


# Default API endpoints
DEFAULT_METADATA_API_ENDPOINT = 'https://cloud.dwavesys.com/metadata/v1/'

DEFAULT_REGION = 'na-west-1'

DEFAULT_SOLVER_API_ENDPOINT = 'https://cloud.dwavesys.com/sapi/'

DEFAULT_LEAP_API_ENDPOINT = 'https://cloud.dwavesys.com/leap/api/'
