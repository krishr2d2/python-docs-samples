# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

import create_reasoning_engine_advanced
import create_reasoning_engine_basic
import delete_reasoning_engine
import get_reasoning_engine
import list_reasoning_engine


PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
REGION = "us-central1"
REASONING_ENGINE_ID = "REASONING_ENGINE_ID"
STAGING_BUCKET = "STAGING_BUCKET"


def test_create_reasoning_engine_advanced() -> None:
    response = create_reasoning_engine_advanced.generate_content(PROJECT_ID, REGION, STAGING_BUCKET)
    assert response


def test_create_reasoning_engine_basic() -> None:
    response = create_reasoning_engine_basic.generate_content(PROJECT_ID, REGION, STAGING_BUCKET)
    assert response


def test_delete_reasoning_engine() -> None:
    response = delete_reasoning_engine.generate_content(PROJECT_ID, REGION, REASONING_ENGINE_ID, STAGING_BUCKET)
    assert response


def test_get_reasoning_engine() -> None:
    response = get_reasoning_engine.generate_content(PROJECT_ID, REGION, REASONING_ENGINE_ID)
    assert response


def test_list_reasoning_engine() -> None:
    response = list_reasoning_engine.generate_content(PROJECT_ID, REGION, STAGING_BUCKET)
    assert response
