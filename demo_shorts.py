#!/usr/bin/env python3
"""
Demo script for AI Shorts Creator

This script demonstrates the complete workflow for creating a short-form video.
Run with: python demo_shorts.py
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shorts_creator.script_generator import ScriptGenerator
from shorts_creator.footage_generator import FootageGenerator
from shorts_creator.shorts_workflow import ShortsWorkflow, WorkflowConfig


def demo_script_generation():
    """Demo: Generate a script for a short video."""
    print("\n" + "="*60)
    print("DEMO: Script Generation")
    print("="*60)
    
    generator = ScriptGenerator()
    
    topic = "3 productivity tips that actually work"
    print(f"\nTopic: {topic}")
    print("Generating script...")
    
    script = generator.generate_script(
        topic=topic,
        style='educational',
        duration=60,
        tone='casual'
    )
    
    if script:
        print(f"\n✅ Script Generated!")
        print(f"Title: {script['title']}")
        print(f"\nHook: {script['hook']}")
        print(f"\nFull Script:\n{script['full_script']}")
        print(f"\nHashtags: {' '.join(script['hashtags'])}")
        return script
    else:
        print("❌ Script generation failed (check API key in config.yaml)")
        return None


def demo_image_generation():
    """Demo: Generate an AI image (free via Pollinations)."""
    print("\n" + "="*60)
    print("DEMO: AI Image Generation (Free)")
    print("="*60)
    
    generator = FootageGenerator()
    
    prompt = "A person working productively at a modern desk with laptop, professional lighting"
    print(f"\nPrompt: {prompt}")
    print("Generating image via Pollinations.ai (free, no API key needed)...")
    
    try:
        image_path = generator.generate_image(
            prompt=prompt,
            style='photorealistic',
            engine='pollinations',
            aspect_ratio='9:16'
        )
        print(f"\n✅ Image Generated: {image_path}")
        return image_path
    except Exception as e:
        print(f"❌ Image generation failed: {e}")
        return None


def demo_complete_workflow():
    """Demo: Complete video creation workflow."""
    print("\n" + "="*60)
    print("DEMO: Complete Video Creation Workflow")
    print("="*60)
    
    # Configure for free operation (no API keys needed)
    config = WorkflowConfig(
        script_duration=30,  # Shorter for demo
        script_style='educational',
        script_tone='casual',
        tts_method='edge_tts',  # Free TTS
        image_engine='pollinations',  # Free image generation
        prefer_stock=False,  # Use AI generation
        add_captions=True
    )
    
    workflow = ShortsWorkflow(config)
    
    topic = "Why drinking water is important"
    print(f"\nTopic: {topic}")
    print("\nThis will:")
    print("  1. Generate a 30-second script")
    print("  2. Create voiceover using Edge TTS (free)")
    print("  3. Generate visuals using Pollinations.ai (free)")
    print("  4. Assemble final video with captions")
    
    def progress(percent, message):
        print(f"  [{percent:3d}%] {message}")
    
    try:
        result = workflow.create_video(topic, progress_callback=progress)
        
        print("\n" + "="*60)
        print("✅ VIDEO CREATED SUCCESSFULLY!")
        print("="*60)
        print(f"Video: {result.get('video_path', 'N/A')}")
        print(f"Script: {result['files'].get('script', 'N/A')}")
        
        return result
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """Run all demos."""
    print("\n" + "="*60)
    print("🎬 AI Shorts Creator - Demo")
    print("="*60)
    
    print("\nThis demo showcases the Shorts Creator capabilities.")
    print("Note: Some features require API keys in config.yaml")
    
    # Menu
    while True:
        print("\n" + "-"*40)
        print("Select a demo:")
        print("  1. Script Generation (requires LLM API)")
        print("  2. AI Image Generation (free, no API needed)")
        print("  3. Complete Workflow (requires LLM API)")
        print("  4. Run all demos")
        print("  0. Exit")
        print("-"*40)
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            demo_script_generation()
        elif choice == '2':
            demo_image_generation()
        elif choice == '3':
            demo_complete_workflow()
        elif choice == '4':
            demo_script_generation()
            demo_image_generation()
            demo_complete_workflow()
        elif choice == '0':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
