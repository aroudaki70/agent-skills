#!/bin/bash
# Remote Connection Manager
# For connecting to Ollama, GitHub, and remote development

# === OLLAMA REMOTE ===
# To connect to remote Ollama server:
# Set environment variable:
#   Windows: set OLLAMA_BASE_URL=http://REMOTE_IP:11434
#   Linux/Mac: export OLLAMA_BASE_URL=http://REMOTE_IP:11434
#
# Example for remote Ollama:
#   export OLLAMA_BASE_URL=http://192.168.1.100:11434
#   ollama list  # List models on remote server
#   ollama run llama3 "Hello"  # Run model on remote

# === GITHUB REMOTE ===
# Already authenticated with gh CLI
# To push/pull:
#   git push origin main
#   git pull origin main

# === VS CODE REMOTE ===
# Option 1: VS Code SSH
#   ssh user@remote-server
#   code --folder-uri /path/to/project
#
# Option 2: VS Code Codespaces
#   Create codespace from GitHub
#
# Option 3: Tunnel (ngrok, etc.)
#   ngrok tcp 11434  # Tunnel Ollama port

# === TEST CONNECTIONS ===
test_ollama() {
    curl -s http://localhost:11434/api/tags || echo "Ollama not running locally"
}

test_remote_ollama() {
    if [ -n "$OLLAMA_BASE_URL" ]; then
        curl -s "$OLLAMA_BASE_URL/api/tags" || echo "Remote Ollama not accessible"
    else
        echo "OLLAMA_BASE_URL not set"
    }
}

test_github() {
    gh auth status
}

# Uncomment to test:
# test_ollama
# test_github