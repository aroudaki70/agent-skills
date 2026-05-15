#!/usr/bin/env python3
"""
SEO Content Audit Script
Analyzes blog post content for SEO optimization opportunities.

Usage:
    python seo-audit.py input.txt --output report.json
    python seo-audit.py --notion-webhook PAYLOAD --output report.json
"""

import json
import re
import argparse
import sys
from pathlib import Path
from typing import Dict, Any

class SEOAuditor:
    def __init__(self, content: str, title: str = "", meta_desc: str = ""):
        self.content = content
        self.title = title
        self.meta_desc = meta_desc
        self.word_count = len(content.split())
        self.reading_time = max(1, self.word_count // 200)
    
    def analyze_keyword_density(self, keyword: str) -> float:
        if not keyword or self.word_count == 0:
            return 0.0
        count = self.content.lower().count(keyword.lower())
        return round((count / self.word_count) * 100, 2)
    
    def check_heading_structure(self) -> Dict[str, Any]:
        headings = {
            "h1": re.findall(r'<h1[^>]*>(.*?)</h1>', self.content, re.I),
            "h2": re.findall(r'<h2[^>]*>(.*?)</h2>', self.content, re.I),
            "h3": re.findall(r'<h3[^>]*>(.*?)</h3>', self.content, re.I),
        }
        
        issues = []
        if len(headings["h1"]) == 0:
            issues.append("Missing H1 tag")
        elif len(headings["h1"]) > 1:
            issues.append("Multiple H1 tags found")
        if len(headings["h2"]) == 0:
            issues.append("No H2 subheadings found")
        
        return {"headings": headings, "issues": issues}
    
    def check_meta_tags(self) -> Dict[str, Any]:
        issues = []
        
        if self.title:
            if len(self.title) < 30:
                issues.append("Title too short (< 30 chars)")
            elif len(self.title) > 60:
                issues.append("Title too long (> 60 chars)")
        else:
            issues.append("Missing title tag")
        
        if self.meta_desc:
            if len(self.meta_desc) < 120:
                issues.append("Meta description too short (< 120 chars)")
            elif len(self.meta_desc) > 160:
                issues.append("Meta description too long (> 160 chars)")
        else:
            issues.append("Missing meta description")
        
        return {"issues": issues}
    
    def check_images(self) -> Dict[str, Any]:
        images = re.findall(r'<img[^>]+>', self.content, re.I)
        missing_alt = []
        
        for img in images:
            if 'alt=' not in img.lower():
                missing_alt.append(img)
        
        return {
            "total_images": len(images),
            "missing_alt": len(missing_alt),
            "issues": [f"{len(missing_alt)} images missing alt text"] if missing_alt else []
        }
    
    def check_links(self) -> Dict[str, Any]:
        internal = re.findall(r'href=[\'"]?(/[^\'" >]+)', self.content)
        external = re.findall(r'href=[\'"]?(https?://[^\'" >]+)', self.content)
        
        issues = []
        if len(internal) == 0 and len(external) == 0:
            issues.append("No links found in content")
        elif len(internal) == 0:
            issues.append("No internal links found")
        
        return {
            "internal_links": len(internal),
            "external_links": len(external),
            "issues": issues
        }
    
    def check_schema(self) -> Dict[str, Any]:
        has_schema = 'application/ld+json' in self.content
        return {
            "has_structured_data": has_schema,
            "issues": ["No JSON-LD structured data found"] if not has_schema else []
        }
    
    def generate_report(self, keyword: str = "") -> Dict[str, Any]:
        heading_analysis = self.check_heading_structure()
        meta_analysis = self.check_meta_tags()
        image_analysis = self.check_images()
        link_analysis = self.check_links()
        schema_analysis = self.check_schema()
        
        all_issues = (
            heading_analysis["issues"] +
            meta_analysis["issues"] +
            image_analysis["issues"] +
            link_analysis["issues"] +
            schema_analysis["issues"]
        )
        
        base_score = 100
        base_score -= len(all_issues) * 10
        
        keyword_density = 0
        if keyword:
            keyword_density = self.analyze_keyword_density(keyword)
            if keyword_density < 0.5:
                base_score -= 10
            elif keyword_density > 3:
                base_score -= 10
        
        score = max(0, min(100, base_score))
        
        return {
            "score": score,
            "word_count": self.word_count,
            "reading_time_minutes": self.reading_time,
            "keyword_analysis": {
                "keyword": keyword,
                "density_percent": keyword_density,
                "recommendation": "Increase keyword usage" if keyword_density < 0.5 else "Good density" if keyword_density <= 2 else "Reduce keyword density"
            } if keyword else {},
            "heading_structure": heading_analysis,
            "meta_tags": meta_analysis,
            "images": image_analysis,
            "links": link_analysis,
            "structured_data": schema_analysis,
            "issues": all_issues,
            "priority_actions": [
                {"severity": "Critical", "items": [i for i in all_issues if "Missing" in i or "Multiple" in i]},
                {"severity": "High", "items": [i for i in all_issues if "too short" in i or "too long" in i]},
                {"severity": "Medium", "items": [i for i in all_issues if "No" in i or "missing" in i]},
            ]
        }


def main():
    parser = argparse.ArgumentParser(description="SEO Content Audit Tool")
    parser.add_argument("input", nargs="?", help="Input text file")
    parser.add_argument("--output", "-o", help="Output report file")
    parser.add_argument("--title", "-t", help="Content title")
    parser.add_argument("--meta", "-m", help="Meta description")
    parser.add_argument("--keyword", "-k", help="Primary keyword")
    parser.add_argument("--notion-webhook", help="Notion webhook payload")
    
    args = parser.parse_args()
    
    if args.notion_webhook:
        payload = json.loads(args.notion_webhook)
        content = payload.get("content", "")
        title = payload.get("title", args.title or "")
        meta = payload.get("meta_description", args.meta or "")
    elif args.input:
        with open(args.input) as f:
            content = f.read()
        title = args.title or Path(args.input).stem
        meta = args.meta or ""
    else:
        content = sys.stdin.read()
        title = args.title or "Untitled"
        meta = args.meta or ""
    
    auditor = SEOAuditor(content, title, meta)
    report = auditor.generate_report(args.keyword or "")
    
    if args.output:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=2)
        print(f"Report saved: {args.output}")
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
