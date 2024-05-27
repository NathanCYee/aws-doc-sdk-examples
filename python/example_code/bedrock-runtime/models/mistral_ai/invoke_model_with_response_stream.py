# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# snippet-start:[python.example_code.bedrock-runtime.InvokeModelWithResponseStream_MistralAI]
# Use the native inference API to send a text message to Mistral AI
# and print the response stream.

import boto3
import json

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Mistral Large.
model_id = "mistral.mistral-large-2402-v1:0"

# Define the message to send.
user_message = "Describe the purpose of a 'hello world' program in one line."

# Embed the message in Mistral's prompt format.
prompt = f"<s>[INST] {user_message} [/INST]"

# Format the request payload using the model's native structure.
native_request = {
    "prompt": prompt,
    "max_tokens": 512,
    "temperature": 0.5,
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
streaming_response = client.invoke_model_with_response_stream(
    modelId=model_id, body=request
)

# Extract and print the response text in real-time.
for event in streaming_response["body"]:
    chunk = json.loads(event["chunk"]["bytes"])
    if "outputs" in chunk:
        print(chunk["outputs"][0]["text"], end="")

# snippet-end:[python.example_code.bedrock-runtime.InvokeModelWithResponseStream_MistralAI]