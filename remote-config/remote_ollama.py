#!/usr/bin/env python3
"""
Remote Ollama Connection Manager
Connect to remote Ollama servers

Usage:
    python remote_ollama.py --host 192.168.1.100 --port 11434
    python remote_ollama.py --url http://remote-server:11434
    python remote_ollama.py --list-models
"""

import os
import sys
import argparse
import requests
from typing import Optional, List, Dict

DEFAULT_PORT = 11434

class RemoteOllama:
    def __init__(self, host: str = "localhost", port: int = DEFAULT_PORT, base_url: Optional[str] = None):
        if base_url:
            self.base_url = base_url.rstrip('/')
        else:
            self.base_url = f"http://{host}:{port}"
        
        self.headers = {"Content-Type": "application/json"}
    
    def list_models(self) -> List[Dict]:
        """List available models on remote server"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("models", [])
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to {self.base_url}: {e}")
            return []
    
    def generate(self, model: str, prompt: str, **kwargs) -> str:
        """Generate text using remote model"""
        payload = {
            "model": model,
            "prompt": prompt,
            **kwargs
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                headers=self.headers,
                stream=kwargs.get("stream", False),
                timeout=120
            )
            response.raise_for_status()
            
            if kwargs.get("stream", False):
                for chunk in response.iter_lines():
                    if chunk:
                        print(chunk.decode('utf-8'))
                return ""
            else:
                return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
    
    def chat(self, model: str, messages: List[Dict], **kwargs) -> str:
        """Chat with remote model"""
        payload = {
            "model": model,
            "messages": messages,
            **kwargs
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                headers=self.headers,
                stream=kwargs.get("stream", False),
                timeout=120
            )
            response.raise_for_status()
            
            if kwargs.get("stream", False):
                for chunk in response.iter_lines():
                    if chunk:
                        print(chunk.decode('utf-8'))
                return ""
            else:
                return response.json().get("message", {}).get("content", "")
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
    
    def check_connection(self) -> bool:
        """Check if remote server is accessible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False


def main():
    parser = argparse.ArgumentParser(description="Remote Ollama Connection Manager")
    parser.add_argument("--host", default="localhost", help="Ollama server IP/hostname")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Ollama server port")
    parser.add_argument("--url", help="Full URL (overrides host/port)")
    parser.add_argument("--list", "-l", action="store_true", help="List available models")
    parser.add_argument("--model", "-m", help="Model name to use")
    parser.add_argument("--prompt", "-p", help="Prompt to send")
    parser.add_argument("--chat", action="store_true", help="Chat mode")
    
    args = parser.parse_args()
    
    # Create connection
    client = RemoteOllama(host=args.host, port=args.port, base_url=args.url)
    
    # Check connection
    if not client.check_connection():
        print(f"Cannot connect to {client.base_url}")
        print("Make sure:")
        print("  1. Ollama is running on remote server")
        print("  2. OLLAMA_HOST=0.0.0.0:11434 is set on remote")
        print("  3. Firewall allows port 11434")
        sys.exit(1)
    
    print(f"Connected to {client.base_url}")
    
    # List models
    if args.list:
        models = client.list_models()
        if models:
            print("\nAvailable models:")
            for m in models:
                print(f"  - {m.get('name', 'unknown')} ({m.get('size', 'unknown')})")
        else:
            print("No models found")
        return
    
    # Generate/chat
    if args.prompt:
        if args.chat:
            messages = [{"role": "user", "content": args.prompt}]
            response = client.chat(args.model or "llama3", messages)
        else:
            response = client.generate(args.model or "llama3", args.prompt)
        print(response)
    elif not args.list:
        # Interactive mode
        print("Interactive mode. Press Ctrl+C to exit.")
        model = args.model or "llama3"
        messages = []
        
        while True:
            try:
                user_input = input("\n> ")
                messages.append({"role": "user", "content": user_input})
                response = client.chat(model, messages)
                print(f"\n{response}")
                messages.append({"role": "assistant", "content": response})
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    main()