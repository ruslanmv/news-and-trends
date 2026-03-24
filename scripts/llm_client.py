#!/usr/bin/env python3
"""
scripts/llm_client.py

Multi-provider LLM client for news-and-trends generation.

Selection (in order):
  1) NEWS_LLM_MODEL  (recommended)  e.g. "openai/gpt-4o-mini"
  2) LLM_MODEL
  3) Auto-detect: pick the best provider based on available API keys
     Priority: OpenAI > Anthropic > WatsonX > Groq > Ollama
  4) Fallback: "ollama/gemma:2b" (for local development only)
"""

import os
import sys
from crewai import LLM


def _auto_detect_model():
    """Auto-detect the best available LLM based on which API keys are set."""
    if os.environ.get("OPENAI_API_KEY"):
        model = "openai/gpt-4o-mini"
        print(f"[llm_client] Auto-detected OPENAI_API_KEY -> {model}")
        return model

    if os.environ.get("ANTHROPIC_API_KEY"):
        model = "anthropic/claude-haiku-4-5-20251001"
        print(f"[llm_client] Auto-detected ANTHROPIC_API_KEY -> {model}")
        return model

    wx_key = os.environ.get("WATSONX_APIKEY") or os.environ.get("WATSONX_API_KEY")
    wx_proj = os.environ.get("WATSONX_PROJECT_ID") or os.environ.get("WATSONX_PROJECTID")
    if wx_key and wx_proj:
        model = "watsonx/meta-llama/llama-3-3-70b-instruct"
        print(f"[llm_client] Auto-detected WATSONX credentials -> {model}")
        return model

    if os.environ.get("GROQ_API_KEY"):
        model = "groq/llama3-8b-8192"
        print(f"[llm_client] Auto-detected GROQ_API_KEY -> {model}")
        return model

    print(
        "[llm_client] No cloud API keys found. Falling back to ollama/gemma:2b.\n"
        "  Set OPENAI_API_KEY, ANTHROPIC_API_KEY, or WATSONX_APIKEY for reliable CI runs.",
        file=sys.stderr,
    )
    return "ollama/gemma:2b"


def get_llm():
    """
    Instantiate a CrewAI LLM that can talk to:
      - OpenAI (gpt-4o-mini, etc.)
      - Anthropic Claude
      - IBM watsonx.ai
      - Groq (free tier)
      - Local Ollama (fallback for local dev)
    """
    model = os.environ.get("NEWS_LLM_MODEL") or os.environ.get("LLM_MODEL") or ""
    if not model:
        model = _auto_detect_model()

    temperature = float(os.environ.get("NEWS_LLM_TEMPERATURE", "0.7"))

    kwargs = {}

    # Local Ollama
    if model.startswith("ollama/"):
        base_url = os.environ.get("OLLAMA_API_BASE") or os.environ.get("OLLAMA_HOST") or "http://127.0.0.1:11434"
        kwargs["base_url"] = base_url
        print(f"\U0001f916 Using Ollama model '{model}' at {base_url}")

    # IBM watsonx.ai (remote)
    elif model.startswith("watsonx/"):
        base_url = os.environ.get("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        kwargs["base_url"] = base_url
        api_key = os.environ.get("WATSONX_APIKEY") or os.environ.get("WATSONX_API_KEY")
        project_id = os.environ.get("WATSONX_PROJECT_ID") or os.environ.get("WATSONX_PROJECTID")
        if api_key:
            kwargs["api_key"] = api_key
        if project_id:
            kwargs["project_id"] = project_id
        print(f"\U0001f916 Using Watsonx model '{model}' at {base_url}")

    else:
        # OpenAI / Anthropic / Groq / etc. handled by LiteLLM via CrewAI
        print(f"\U0001f916 Using remote provider model '{model}' via LiteLLM")

    llm = LLM(
        model=model,
        temperature=temperature,
        **kwargs,
    )
    return llm


# Singleton instance to import in other scripts
llm = get_llm()
