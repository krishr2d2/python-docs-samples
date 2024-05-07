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


class LangchainApp:
    def __init__(self, project: str, location: str):
        self.project_id = project
        self.location = location

    def set_up(self):
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_google_vertexai import ChatVertexAI
        try:
            from google.cloud.aiplatform import vertexai
        except:
            import vertexai

        vertexai.init(
            project=self.project_id,
            location=self.location,
        )

        system = (
            "You are a helpful assistant that answers questions "
            "about Google Cloud."
        )
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([
            ("system", system), ("human", human)
        ])
        chat = ChatVertexAI()
        self.chain = prompt | chat

    def query(self, question: str):
        """Query the application.

        Args:
            question: The user prompt.

        Returns:
            str: The LLM response.
        """
        return self.chain.invoke({"text": question}).content


def generate_content(PROJECT_ID: str, REGION: str, STAGING_BUCKET: str) -> object:
    # [START generativeaionvertexai_create_reasoning_engine_advanced]
    import vertexai
    from vertexai.preview import reasoning_engines

    vertexai.init(project=PROJECT_ID,location=REGION,staging_bucket=STAGING_BUCKET)

    # Create a remote app with reasoning engine
    # This may take 1-2 minutes to finish because it builds a container and turn up HTTP servers. 
    remote_app = reasoning_engines.ReasoningEngine.create(
        LangchainApp(project=PROJECT_ID, location=REGION),
        requirements=[
            "google-cloud-aiplatform==1.45.0",
            "langchain-google-vertexai",
            "langchain-core"
        ],
        display_name="Simple GCP helper app",
        description="Simple GCP helper app",
        sys_version="3.10",
        extra_packages=[],
    )
    # [END generativeaionvertexai_create_reasoning_engine_advanced]
    return remote_app

if __name__ == "__main__":
    # Locally test
    PROJECT_ID = 'your-project-id'
    REGION = 'us-central1'

    app = LangchainApp(project=PROJECT_ID, location=REGION)
    app.set_up()
    print(app.query("What is Vertex AI?"))

