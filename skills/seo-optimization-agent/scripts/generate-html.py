#!/usr/bin/env python3
"""
SEO Optimized HTML Generator
Generates SEO-optimized HTML from raw content and SEO audit report.

Usage:
    python generate-html.py --content input.txt --report report.json --output post.html
    python generate-html.py --notion-webhook PAYLOAD --output post.html
"""

import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional


class SEOHTMLGenerator:
    def __init__(self, content: str, report: Dict[str, Any], title: str = "", keyword: str = ""):
        self.content = content
        self.report = report
        self.title = title or report.get("title", "Untitled")
        self.keyword = keyword or report.get("keyword_analysis", {}).get("keyword", "")
    
    def generate_meta_tags(self) -> str:
        desc = self.report.get("meta_tags", {})
        meta_desc = ""
        for issue in desc.get("issues", []):
            if "Missing meta description" in issue:
                meta_desc = f"Learn about {self.keyword or self.title}. Expert guide with tips and best practices."
        
        return f'''    <meta name="description" content="{meta_desc or 'Comprehensive guide on ' + self.title}">
    <meta name="keywords" content="{self.keyword or self.title}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://example.com/{self.title.lower().replace(' ', '-')}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{self.title}">
    <meta property="og:description" content="{meta_desc or 'Comprehensive guide on ' + self.title}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://example.com/{self.title.lower().replace(' ', '-')}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{self.title}">
    <meta name="twitter:description" content="{meta_desc or 'Comprehensive guide on ' + self.title}">'''
    
    def generate_schema(self) -> str:
        return f'''    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{self.title}",
        "description": "Comprehensive guide on {self.keyword or self.title}",
        "author": {{ "@type": "Person", "name": "Author" }},
        "datePublished": "{datetime.now().strftime('%Y-%m-%d')}",
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "https://example.com/{self.title.lower().replace(' ', '-')}"
        }},
        "keywords": "{self.keyword or self.title}"
    }}
    </script>'''
    
    def optimize_content(self) -> str:
        lines = self.content.split('\n')
        optimized = []
        keyword_lower = self.keyword.lower() if self.keyword else ""
        
        for line in lines:
            # Optimize headings
            if line.startswith('# ') and keyword_lower and keyword_lower not in line.lower():
                line = f"# {self.keyword}: {line[2:]}"
            elif line.startswith('## ') and keyword_lower and keyword_lower not in line.lower() and len(optimized) < 5:
                # Add keyword to early H2s naturally
                pass
            
            # Add alt text suggestion for images
            if '![' in line and ']()' in line:
                line = line.replace(']()', f'](image.jpg "{self.keyword} illustration")')
            
            optimized.append(line)
        
        return '\n'.join(optimized)
    
    def generate_html(self) -> str:
        optimized_content = self.optimize_content()
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
{self.generate_meta_tags()}
    {self.generate_schema()}
    
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; }}
        h1 {{ font-size: 2em; margin-bottom: 0.5em; }}
        h2 {{ font-size: 1.5em; margin-top: 1.5em; }}
        h3 {{ font-size: 1.25em; margin-top: 1em; }}
        img {{ max-width: 100%; height: auto; }}
        a {{ color: #0066cc; }}
        p {{ margin: 1em 0; }}
        @media (max-width: 600px) {{ body {{ padding: 10px; }} }}
    </style>
</head>
<body>
    <article>
        {optimized_content}
    </article>
</body>
</html>'''


def main():
    parser = argparse.ArgumentParser(description="SEO Optimized HTML Generator")
    parser.add_argument("--content", "-c", help="Input content file")
    parser.add_argument("--report", "-r", help="SEO audit report JSON")
    parser.add_argument("--output", "-o", help="Output HTML file")
    parser.add_argument("--title", "-t", help="Post title")
    parser.add_argument("--keyword", "-k", help="Primary keyword")
    parser.add_argument("--notion-webhook", help="Notion webhook payload")
    
    args = parser.parse_args()
    
    if args.notion_webhook:
        payload = json.loads(args.notion_webhook)
        content = payload.get("content", "")
        title = payload.get("title", args.title or "")
        keyword = payload.get("keyword", args.keyword or "")
        report = payload.get("report", {})
    elif args.content and args.report:
        with open(args.content) as f:
            content = f.read()
        with open(args.report) as f:
            report = json.load(f)
        title = args.title or Path(args.content).stem
        keyword = args.keyword or report.get("keyword_analysis", {}).get("keyword", "")
    else:
        print("ERROR: Provide --content and --report, or --notion-webhook", file=sys.stderr)
        sys.exit(1)
    
    generator = SEOHTMLGenerator(content, report, title, keyword)
    html = generator.generate_html()
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"HTML saved: {args.output}")
    else:
        print(html)


if __name__ == "__main__":
    main()
