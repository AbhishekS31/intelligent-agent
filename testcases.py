import pytest
from agent import run_agent
from schemas import PromptResponse
from agent import load_systemprompt_config

config = load_systemprompt_config()

test_cases = [
    ("What's the weather in Delhi today?", "weather"),
    ("Tell me something funny", "joke"),
    ("Give me an inspiring quote", "quote"),

    ("Is it hot or cold outside?", "weather"),
    ("I could use a good laugh", "joke"),
    ("Something motivational please", "quote"),

    ("How do I install Linux?", "none"),
]

@pytest.mark.parametrize("prompt, expected_tool", test_cases)
def test_agent_tool_routing_and_fallback(prompt, expected_tool):
    response = run_agent(prompt)
    
    assert isinstance(response, PromptResponse)
    assert response.metadata.tool_name == expected_tool

    if expected_tool == "none":
        assert response.response == config["fallback"]["no_match"]
        assert not response.metadata.success
    else:
        assert response.metadata.success
        assert isinstance(response.response, str)
        assert response.response.strip() != ""
