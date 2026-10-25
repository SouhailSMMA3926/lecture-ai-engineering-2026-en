"""Lecture 01 Homework: Advanced Level - Response Time & Token Benchmark.

Usage:
    uv run python -m app.ask "What is LoRA?"
"""

import argparse
import time

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

DEFAULT_QUESTION = "What are the 3 homework levels in the AIE2026 course?"


def ask(question: str) -> str:
    client = genai.Client(api_key=get_api_key())

    start_time = time.perf_counter()
    response = client.models.generate_content(model=MODEL, contents=question)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f"[Model] {MODEL}")
    print(f"[Latency] {elapsed_time:.2f} seconds")

    if hasattr(response, "usage_metadata") and response.usage_metadata:
        in_tokens = response.usage_metadata.prompt_token_count
        out_tokens = response.usage_metadata.candidates_token_count
        total_tokens = response.usage_metadata.total_token_count
        print(f"[Tokens] Input: {in_tokens} | Output: {out_tokens} | Total: {total_tokens}")

        if elapsed_time > 0 and out_tokens:
            tok_per_sec = out_tokens / elapsed_time
            print(f"[Speed] {tok_per_sec:.2f} output tokens/sec")

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a bare LLM a question and measure latency")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[question] {args.question}\n")
    try:
        print(ask(args.question))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()