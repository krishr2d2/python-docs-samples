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


class SimpleAdditionApp:

    def query(self, a: int, b: int):
        """Query the application.

        Args:
            a: The first input number
            b: The second input number

        Returns:
            int: The additional result.
        """

        return f"{int(a)} + {int(b)} is {int(a+b)}" 




def generate_content(PROJECT_ID: str, REGION: str, STAGING_BUCKET: str) -> object:
    # [START generativeaionvertexai_create_reasoning_engine_basic]
    import vertexai
    from vertexai.preview import reasoning_engines

    vertexai.init(project=PROJECT_ID,location=REGION,staging_bucket=STAGING_BUCKET)

    # Create a remote app with reasoning engine
    # This may take 1-2 minutes to finish because it builds a container and turns up HTTP servers. 
    remote_app = reasoning_engines.ReasoningEngine.create(
        SimpleAdditionApp(),
        display_name="A simple demo app",
        description="A simple demo app",
        requirements=[],
        extra_packages=[]
    )
    # [END generativeaionvertexai_create_reasoning_engine_basic]
    return remote_app


if __name__ == "__main__":
    # Locally test
    app = SimpleAdditionApp()
    app.query(a=1, b=2)