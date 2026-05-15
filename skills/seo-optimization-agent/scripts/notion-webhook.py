#!/usr/bin/env python3
"""
Notion Webhook Handler for SEO Optimization
Receives blog post data from Notion, runs SEO audit, generates optimized HTML.

Usage:
    # Start webhook server
    python notion-webhook.py --serve --port 8080
    
    # Process single payload
    python notion-webhook.py --payload '{"title":"...","content":"...","keyword":"..."}'
"""

import json
import argparse
import sys
import os
from pathlib import Path
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import subprocess
import tempfile


class NotionWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            payload = json.loads(body)
            result = process_payload(payload)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def log_message(self, format, *args):
        print(f"[{datetime.now().isoformat()}] {format % args}", file=sys.stderr)


def process_payload(payload: dict) -> dict:
    """Process a Notion webhook payload through SEO pipeline"""
    title = payload.get("title", "Untitled")
    content = payload.get("content", "")
    keyword = payload.get("keyword", "")
    meta = payload.get("meta_description", "")
    
    output_dir = Path(payload.get("output_dir", "./output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Save content to temp file
    content_file = output_dir / f"{title.lower().replace(' ', '-')}-content.txt"
    with open(content_file, "w") as f:
        f.write(content)
    
    # Step 2: Run SEO audit
    report_file = output_dir / f"{title.lower().replace(' ', '-')}-report.json"
    audit_args = [
        sys.executable, str(Path(__file__).parent / "seo-audit.py"),
        str(content_file),
        "--output", str(report_file),
        "--title", title,
        "--keyword", keyword,
        "--meta", meta
    ]
    subprocess.run(audit_args, check=True)
    
    # Step 3: Generate optimized HTML
    html_file = output_dir / f"{title.lower().replace(' ', '-')}-optimized.html"
    html_args = [
        sys.executable, str(Path(__file__).parent / "generate-html.py"),
        "--content", str(content_file),
        "--report", str(report_file),
        "--output", str(html_file),
        "--title", title,
        "--keyword", keyword
    ]
    subprocess.run(html_args, check=True)
    
    # Step 4: Load report for response
    with open(report_file) as f:
        report = json.load(f)
    
    return {
        "status": "complete",
        "title": title,
        "seo_score": report.get("score", 0),
        "issues_count": len(report.get("issues", [])),
        "report_url": str(report_file),
        "html_url": str(html_file),
        "timestamp": datetime.now().isoformat()
    }


def main():
    parser = argparse.ArgumentParser(description="Notion Webhook for SEO Optimization")
    parser.add_argument("--serve", action="store_true", help="Start webhook server")
    parser.add_argument("--port", type=int, default=8080, help="Server port")
    parser.add_argument("--payload", help="Process a single JSON payload")
    parser.add_argument("--payload-file", help="Process a JSON payload file")
    
    args = parser.parse_args()
    
    if args.serve:
        server = HTTPServer(("0.0.0.0", args.port), NotionWebhookHandler)
        print(f"Notion webhook server running on port {args.port}")
        print(f"Configure Notion to POST to http://YOUR_IP:{args.port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")
            server.server_close()
    elif args.payload:
        payload = json.loads(args.payload)
        result = process_payload(payload)
        print(json.dumps(result, indent=2))
    elif args.payload_file:
        with open(args.payload_file) as f:
            payload = json.load(f)
        result = process_payload(payload)
        print(json.dumps(result, indent=2))
    else:
        # Interactive test
        print("SEO Notion Webhook - Interactive Mode")
        print("Enter payload (Ctrl+D to finish):")
        payload = json.loads(sys.stdin.read())
        result = process_payload(payload)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
