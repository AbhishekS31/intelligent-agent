from schemas import PromptResponse, ToolMetadata
from Tools import tool_1, tool_2, tool_3
import json

def load_systemprompt_config() -> dict:
    with open("Prompt/systemprompt_config.json") as f:
        return json.load(f)

def decide_tool(prompt: str, config: dict) -> str:
    prompt_lower = prompt.lower()
    for tool_name, keywords in config["tools"].items():
        if any(keyword in prompt_lower for keyword in keywords):
            return tool_name
    return "none"

def run_agent(prompt: str) -> PromptResponse:
    config = load_systemprompt_config()
    selected_tool = decide_tool(prompt, config)

    if selected_tool == "weather":
        result = tool_1.get_weather(prompt)
    elif selected_tool == "joke":
        result = tool_2.get_random_joke()
    elif selected_tool == "quote":
        result = tool_3.get_random_quote()
    else:
        return PromptResponse(
            response="Sorry, can't help with that.",
            metadata=ToolMetadata(tool_name="none", success=False, error_message="No matching tool")
        )

    if not result:
        return PromptResponse(
            response="Sorry! That didn’t work. You can try again.",
            metadata=ToolMetadata(tool_name=selected_tool, success=False, error_message="Tool returned no data")
        )

    return PromptResponse(
        response=result,
        metadata=ToolMetadata(tool_name=selected_tool, success=True)
    )
