# -*- coding: utf-8 -*-

# Copyright 2014 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64


def encode_base64(input_bytes):
    """Encode bytes as a base64 string without any padding."""

    input_len = len(input_bytes)
    output_len = 4 * ((input_len + 2) // 3) + (input_len + 2) % 3 - 2
    output_bytes = base64.b64encode(input_bytes)
    output_string = output_bytes[:output_len].decode("ascii")
    return output_string


def decode_base64(input_string):
    """Decode a base64 string to bytes inferring padding from the length of the
    string."""

    input_bytes = input_string.encode("ascii")
    input_len = len(input_bytes)
    padding = b"=" * (3 - ((input_len + 3) % 4))
    output_len = 3 * ((input_len + 2) // 4) + (input_len + 2) % 4 - 2
    output_bytes = base64.b64decode(input_bytes + padding)
    return output_bytes[:output_len]
