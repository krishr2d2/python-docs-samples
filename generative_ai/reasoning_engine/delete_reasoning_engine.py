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


def generate_content(PROJECT_ID: str, REGION: str, REASONING_ENGINE_ID: str, STAGING_BUCKET: str) -> object:
    # [START generativeaionvertexai_delete_reasoning_engine]
    import vertexai
    from vertexai.preview import reasoning_engines

    vertexai.init(project=PROJECT_ID,location=REGION,staging_bucket=STAGING_BUCKET)

    remote_app = reasoning_engines.ReasoningEngine(
    f"projects/{PROJECT_ID}/locations/{REGION}/reasoningEngines/{REASONING_ENGINE_ID}"
    )

    remote_app.delete()
    # [END generativeaionvertexai_delete_reasoning_engine]