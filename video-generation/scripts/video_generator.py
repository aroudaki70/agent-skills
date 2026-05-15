#!/usr/bin/env python3
"""
MiniMax Video Generation Script
Generate videos using MiniMax AI API

Requirements:
    pip install requests python-dotenv

Usage:
    python video_generator.py --script "Your video script here" --style "cinematic"
    python video_generator.py --template intro --output my_video.mp4
"""

import os
import json
import argparse
import requests
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MiniMaxVideoGenerator:
    """Video generation using MiniMax API"""
    
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.minimax.chat"):
        self.api_key = api_key or os.getenv("MINIMAX_API_KEY")
        self.base_url = base_url
        self.group_id = os.getenv("MINIMAX_GROUP_ID")
        
        if not self.api_key:
            raise ValueError("MiniMax API key required. Set MINIMAX_API_KEY env variable.")
    
    def generate_video(self, prompt: str, settings: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Generate video from text prompt
        
        Args:
            prompt: Description of the video to generate
            settings: Optional settings (duration, aspect ratio, etc.)
            
        Returns:
            Response with video URL or task ID
        """
        endpoint = f"{self.base_url}/v1/video/generation"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": prompt,
            "settings": settings or {
                "duration": 10,
                "resolution": "1920x1080",
                "fps": 30,
                "aspect_ratio": "16:9"
            }
        }
        
        if self.group_id:
            payload["group_id"] = self.group_id
        
        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status": "failed"}
    
    def generate_from_script(self, script: str, visual_prompt: str, 
                           text_overlay: Optional[str] = None,
                           style: str = "cinematic") -> Dict[str, Any]:
        """
        Generate video with full production elements
        
        Args:
            script: The dialogue/narrative script
            visual_prompt: Visual description for the scene
            text_overlay: Optional text to overlay
            style: Visual style (cinematic, animated, documentary, etc.)
        """
        # Combine elements into comprehensive prompt
        full_prompt = f"""
        Style: {style}
        Scene: {visual_prompt}
        Narrative: {script}
        """
        
        if text_overlay:
            full_prompt += f"\nText Overlay: {text_overlay}"
        
        return self.generate_video(full_prompt, {"style": style})
    
    def check_status(self, task_id: str) -> Dict[str, Any]:
        """Check generation status"""
        endpoint = f"{self.base_url}/v1/video/status/{task_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(endpoint, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


class VideoProductionManager:
    """Manage video production workflow"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def create_video_from_template(self, template_name: str, variables: Dict) -> str:
        """Create video using a template"""
        # Load template
        template_file = Path(f"templates/{template_name}.json")
        
        if not template_file.exists():
            return f"Template {template_name} not found"
        
        with open(template_file) as f:
            template = json.load(f)
        
        # Replace variables
        script = template["script"].format(**variables)
        visual_prompt = template["visual_prompt"].format(**variables)
        text_overlay = template.get("text_overlay", "").format(**variables) if template.get("text_overlay") else None
        style = template.get("style", "cinematic")
        
        return json.dumps({
            "script": script,
            "visual_prompt": visual_prompt,
            "text_overlay": text_overlay,
            "style": style
        }, indent=2)


def main():
    parser = argparse.ArgumentParser(description="MiniMax Video Generator")
    parser.add_argument("--script", "-s", help="Video script/prompt")
    parser.add_argument("--visual", "-v", help="Visual description")
    parser.add_argument("--text", "-t", help="Text overlay")
    parser.add_argument("--style", default="cinematic", help="Visual style")
    parser.add_argument("--template", help="Use a template")
    parser.add_argument("--output", "-o", help="Output file")
    
    args = parser.parse_args()
    
    if args.template:
        manager = VideoProductionManager()
        result = manager.create_video_from_template(args.template, {"title": "My Video"})
        print(result)
    elif args.script:
        generator = MiniMaxVideoGenerator()
        result = generator.generate_from_script(
            args.script,
            args.visual or args.script,
            args.text,
            args.style
        )
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()