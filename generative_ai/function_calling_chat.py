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

from vertexai.generative_models import ChatSession


def generate_function_call_chat(project_id: str) -> ChatSession:
    # [START generativeaionvertexai_gemini_function_calling_chat]
    import vertexai
    from vertexai.generative_models import (
        FunctionDeclaration,
        GenerationConfig,
        GenerativeModel,
        Part,
        Tool,
    )
<<<<<<< HEAD

    # TODO(developer): Update and un-comment below lines
    # project_id = "PROJECT_ID"

    # Initialize Vertex AI
=======

    # Initialize Vertex AI
    # project_id = "PROJECT_ID"
    # TODO(developer): Update and un-comment below lines
>>>>>>> 92bc4fd631977b7bb302eb84fb025e176f72fef5
    vertexai.init(project=project_id, location="us-central1")

    # Specify a function declaration and parameters for an API request
    get_product_sku = "get_product_sku"
    get_product_sku_func = FunctionDeclaration(
        name=get_product_sku,
        description="Get the SKU for a product",
        # Function parameters are specified in OpenAPI JSON schema format
        parameters={
            "type": "object",
            "properties": {
                "product_name": {"type": "string", "description": "Product name"}
            },
        },
    )

    # Specify another function declaration and parameters for an API request
    get_store_location_func = FunctionDeclaration(
        name="get_store_location",
        description="Get the location of the closest store",
        # Function parameters are specified in OpenAPI JSON schema format
        parameters={
            "type": "object",
            "properties": {"location": {"type": "string", "description": "Location"}},
        },
    )

    # Define a tool that includes the above functions
    retail_tool = Tool(
        function_declarations=[
            get_product_sku_func,
            get_store_location_func,
        ],
    )

    # Initialize Gemini model
    model = GenerativeModel(
        model_name="gemini-1.0-pro-001",
        generation_config=GenerationConfig(temperature=0),
        tools=[retail_tool],
    )

    # Start a chat session
    chat = model.start_chat()

    # Send a prompt for the first conversation turn that should invoke the get_product_sku function
    response = chat.send_message("Do you have the Pixel 8 Pro in stock?")

    function_call = response.candidates[0].function_calls[0]
    print(function_call)

    # Check the function name that the model responded with, and make an API call to an external system
    if function_call.name == get_product_sku:
        # Extract the arguments to use in your API call
        product_name = function_call.args["product_name"]  # noqa: F841

        # Here you can use your preferred method to make an API request to retrieve the product SKU, as in:
        # api_response = requests.post(product_api_url, data={"product_name": product_name})

        # In this example, we'll use synthetic data to simulate a response payload from an external API
        api_response = {"sku": "GA04834-US", "in_stock": "yes"}

    # Return the API response to Gemini, so it can generate a model response or request another function call
    response = chat.send_message(
        Part.from_function_response(
            name=get_product_sku,
            response={
                "content": api_response,
            },
        ),
    )
    # Extract the text from the model response
    print(response.text)

    # Send a prompt for the second conversation turn that should invoke the get_store_location function
    response = chat.send_message(
        "Is there a store in Mountain View, CA that I can visit to try it out?"
    )

    function_call = response.candidates[0].function_calls[0]
    print(function_call)

    # Check the function name that the model responded with, and make an API call to an external system
    if function_call.name == "get_store_location":
        # Extract the arguments to use in your API call
        location = function_call.args["location"]  # noqa: F841

        # Here you can use your preferred method to make an API request to retrieve store location closest to the user, as in:
        # api_response = requests.post(store_api_url, data={"location": location})

        # In this example, we'll use synthetic data to simulate a response payload from an external API
        api_response = {"store": "2000 N Shoreline Blvd, Mountain View, CA 94043, US"}

    # Return the API response to Gemini, so it can generate a model response or request another function call
    response = chat.send_message(
        Part.from_function_response(
            name="get_store_location",
            response={
                "content": api_response,
            },
        ),
    )

    # Extract the text from the model response
    print(response.text)
    # [END generativeaionvertexai_gemini_function_calling_chat]

    return chat
