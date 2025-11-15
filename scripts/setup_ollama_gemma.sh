#!/usr/bin/env bash
set -euo pipefail

# Default model; you can override with: ./setup_ollama_gemma.sh llama3:8b
MODEL="${1:-gemma:2b}"
OLLAMA_HOST="${OLLAMA_HOST:-127.0.0.1}"
OLLAMA_PORT="${OLLAMA_PORT:-11434}"

echo "🔧 Target model: $MODEL"

detect_os() {
  local uname_s
  uname_s="$(uname -s 2>/dev/null || echo unknown)"

  case "$uname_s" in
    Linux*)   echo "linux"   ;;
    Darwin*)  echo "macos"   ;;
    MINGW*|MSYS*|CYGWIN*) echo "windows" ;;
    *)        echo "unknown" ;;
  esac
}

OS="$(detect_os)"
echo "🧭 Detected OS: $OS"

install_ollama_linux() {
  echo "📥 Installing Ollama on Linux..."
  if ! command -v curl >/dev/null 2>&1; then
    echo "❌ curl is required to install Ollama. Please install curl and re-run this script."
    exit 1
  fi
  curl -fsSL https://ollama.com/install.sh | sh
  echo "✅ Ollama installed (Linux)."
}

install_ollama_macos() {
  echo "📥 Installing Ollama on macOS..."

  # Prefer Homebrew if available
  if command -v brew >/dev/null 2>&1; then
    echo "🍺 Using Homebrew to install Ollama..."
    brew install --cask ollama || {
      echo "❌ Brew installation failed. Please install manually from https://ollama.com/download"
      exit 1
    }
  else
    echo "⚠️ Homebrew not found."
    echo "   Please install Ollama manually from https://ollama.com/download"
    exit 1
  fi

  echo "✅ Ollama installed (macOS)."
}

install_ollama_windows() {
  echo "📥 Installing Ollama on Windows (via winget)..."

  if ! command -v powershell.exe >/dev/null 2>&1; then
    echo "❌ powershell.exe not found from bash."
    echo "   Please install Ollama manually from https://ollama.com/download"
    exit 1
  fi

  # winget install in an elevated PowerShell
  powershell.exe -NoProfile -Command \
    "winget install -e --id Ollama.Ollama -h 0" || {
      echo "❌ winget installation failed. Please install manually from https://ollama.com/download"
      exit 1
    }

  echo "✅ Ollama installation requested via winget (Windows)."
  echo "   You may need to restart your shell so 'ollama' is on PATH."
}

ensure_ollama_installed() {
  if command -v ollama >/dev/null 2>&1; then
    echo "✅ Ollama is already installed."
    return 0
  fi

  echo "⚠️ Ollama not found on PATH. Attempting installation..."

  case "$OS" in
    linux)   install_ollama_linux   ;;
    macos)   install_ollama_macos   ;;
    windows) install_ollama_windows ;;
    *)
      echo "❌ Unsupported OS for auto-install."
      echo "   Please install Ollama manually from https://ollama.com/download"
      exit 1
      ;;
  esac

  # Refresh PATH in current shell if possible
  if ! command -v ollama >/dev/null 2>&1; then
    echo "⚠️ 'ollama' still not found on PATH after installation."
    echo "   You may need to open a new terminal or add Ollama to PATH."
    exit 1
  fi
}

wait_for_ollama() {
  echo "⏳ Waiting for Ollama API to be ready on http://$OLLAMA_HOST:$OLLAMA_PORT ..."
  for i in {1..30}; do
    if curl -fsS "http://$OLLAMA_HOST:$OLLAMA_PORT/api/tags" >/dev/null 2>&1; then
      echo "✅ Ollama API is responding."
      return 0
    fi
    sleep 1
  done

  echo "❌ Ollama API did not become ready in time."
  exit 1
}

start_ollama_serve_if_needed() {
  # If API already responds, don't start another server
  if curl -fsS "http://$OLLAMA_HOST:$OLLAMA_PORT/api/tags" >/dev/null 2>&1; then
    echo "ℹ️  Ollama server already running."
    return 0
  fi

  echo "🚀 Starting 'ollama serve' in the background..."
  # On macOS / Windows desktop, this may be unnecessary but is safe to attempt.
  nohup ollama serve >/tmp/ollama.log 2>&1 &

  wait_for_ollama
}

pull_model() {
  echo "⬇️  Pulling model: $MODEL ..."
  ollama pull "$MODEL"
  echo "✅ Model '$MODEL' is ready to use."
}

###############################################################################
# Main
###############################################################################

ensure_ollama_installed
start_ollama_serve_if_needed
pull_model
