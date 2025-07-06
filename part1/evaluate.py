from agent import run_agent
from agent import load_systemprompt_config
from schemas import PromptResponse

test_cases = [
    {
        "prompt": "What's the weather like in Mumbai?",
        "expected_tool": "weather"
    },
    {
        "prompt": "Tell me a funny joke",
        "expected_tool": "joke"
    },
    {
        "prompt": "Something motivational please",
        "expected_tool": "quote"
    },
    {
        "prompt": "What's 2 + 2?",  
        "expected_tool": "none"
    }
]

def evaluate_test_case(prompt: str, expected_tool: str, config: dict) -> dict:
    response = run_agent(prompt)

    passed = (
        response.metadata.tool_name == expected_tool and
        ((expected_tool == "none" and response.response == config["fallback"]["no_match"]) or
         (expected_tool != "none" and response.metadata.success))
    )

    return {
        "prompt": prompt,
        "expected_tool": expected_tool,
        "actual_tool": response.metadata.tool_name,
        "success": response.metadata.success,
        "response": response.response,
        "pass": passed
    }

def run_evaluation():
    config = load_systemprompt_config()
    results = []

    for case in test_cases:
        result = evaluate_test_case(case["prompt"], case["expected_tool"], config)
        results.append(result)

    print("\nEvaluation Results:")
    for res in results:
        status = "PASS" if res["pass"] else "FAIL"
        print(f"\nPrompt: {res['prompt']}")
        print(f"Expected Tool: {res['expected_tool']}")
        print(f"Actual Tool: {res['actual_tool']}")
        print(f"Success: {res['success']}")
        print(f"Response: {res['response']}")
        print(f"Status: {status}")

    total = len(results)
    passed = sum(r["pass"] for r in results)
    print(f"\nSummary: {passed}/{total} passed")

if __name__ == "__main__":
    run_evaluation()
