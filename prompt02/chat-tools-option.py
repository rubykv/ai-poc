import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))


def get_best_friend(name):
    if "leia" in name.lower():
        return json.dumps({"friend": "Han Solo"})
    elif name.lower() == "Han Solo":
        return json.dumps({"friend": "Luke"})
    else:
        return json.dumps({"friend": "C3PO"})


def run_conversation():
    messages = [{"role": "user", "content": "Who's the best friend of Leia?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_best_friend",
                "description": "Get best friends name from Star wars",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Lead character's name from Star Wars",
                        },
                    },
                    "required": ["name"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    print(f'\n First Response: {response}\n')
    response_message = response.choices[0].message
    tool_call_response = response_message.tool_calls[0]  # validate message is a tool call

    if tool_call_response:
        available_functions = {
            "get_best_friend": get_best_friend,
        }
        messages.append(response_message)
        function_name = tool_call_response.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call_response.function.arguments)
        function_response = function_to_call(
            name=function_args.get("name")
        )
        messages.append(
            {
                "tool_call_id": tool_call_response.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
        )
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
        )
        return second_response


print(f'\n Second Response: {run_conversation()}\n')
