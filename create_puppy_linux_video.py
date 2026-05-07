#!/usr/bin/env python3
"""
Custom script to create a video about PuppyLinux.
This script bypasses the LLM script generation by providing a pre-defined script.
"""

import os
import sys
import json
import time

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shorts_creator.shorts_workflow import ShortsWorkflow, WorkflowConfig

def create_puppy_linux_video():
    # Define the script data manually to bypass LLM requirement
    script_data = {
        "title": "Why PuppyLinux is the Ultimate Rescue OS",
        "hook": "Is your old laptop gathering dust? Don't throw it away just yet!",
        "segments": [
            {
                "text": "Is your old laptop gathering dust? Don't throw it away just yet!",
                "duration_estimate": 5,
                "visual_suggestion": "An old, dusty laptop being opened",
                "emphasis": "old laptop"
            },
            {
                "text": "Meet PuppyLinux. It's an incredibly lightweight operating system that can bring almost any old computer back to life.",
                "duration_estimate": 8,
                "visual_suggestion": "PuppyLinux logo with a cute puppy",
                "emphasis": "bring back to life"
            },
            {
                "text": "First, it's tiny! We're talking under 400 megabytes. It runs entirely in your RAM, making it blazing fast even on ancient hardware.",
                "duration_estimate": 10,
                "visual_suggestion": "Graphic showing RAM and fast speed",
                "emphasis": "blazing fast"
            },
            {
                "text": "Second, it's portable. You can run the entire OS from a simple USB stick without touching your hard drive.",
                "duration_estimate": 7,
                "visual_suggestion": "A person plugging in a USB stick",
                "emphasis": "portable"
            },
            {
                "text": "It comes packed with everything you need: a browser, word processor, and media tools. It's the perfect rescue disk or daily driver for low-spec machines.",
                "duration_estimate": 10,
                "visual_suggestion": "Screen recording of PuppyLinux desktop apps",
                "emphasis": "everything you need"
            },
            {
                "text": "Ready to give your old PC a second chance? Download PuppyLinux today and experience the speed!",
                "duration_estimate": 8,
                "visual_suggestion": "Old laptop running fast with PuppyLinux",
                "emphasis": "second chance"
            }
        ],
        "full_script": "Is your old laptop gathering dust? Don't throw it away just yet! Meet PuppyLinux. It's an incredibly lightweight operating system that can bring almost any old computer back to life. First, it's tiny! We're talking under 400 megabytes. It runs entirely in your RAM, making it blazing fast even on ancient hardware. Second, it's portable. You can run the entire OS from a simple USB stick without touching your hard drive. It comes packed with everything you need: a browser, word processor, and media tools. It's the perfect rescue disk or daily driver for low-spec machines. Ready to give your old PC a second chance? Download PuppyLinux today and experience the speed!",
        "hashtags": ["#PuppyLinux", "#Linux", "#TechTips", "#RetroTech", "#OldLaptop"],
        "delivery_tips": ["Keep the tone enthusiastic and fast-paced", "Emphasize the speed and portability"],
        "visual_notes": "Use a mix of retro tech visuals and clean modern graphics"
    }

    # Configure the workflow
    config = WorkflowConfig(
        script_duration=60,
        script_style='educational',
        script_tone='enthusiastic',
        script_language='English',
        tts_method='edge_tts',
        tts_voice='en-US-GuyNeural',
        prefer_stock=False, # Use AI images (Pollinations) as it's free and reliable
        image_engine='pollinations',
        add_captions=True,
        output_dir='output/shorts'
    )

    workflow = ShortsWorkflow(config)
    
    # We need to manually run the steps because create_video calls _generate_script
    print("🚀 Starting PuppyLinux Video Creation...")
    
    def progress(pct, msg):
        print(f"[{pct}%] {msg}")

    try:
        # Step 1: Save the manual script
        progress(10, "Saving script...")
        script_path = workflow._save_script(script_data, "PuppyLinux Advantages")
        
        # Step 2: Generate Voiceover
        progress(30, "Generating voiceover...")
        audio_files = workflow._generate_voiceover(script_data)
        
        # Step 3: Prepare Visuals
        progress(50, "Preparing visuals (AI Images)...")
        visual_files = workflow._prepare_visuals(script_data)
        
        # Step 4: Assemble Video
        progress(70, "Assembling video...")
        video_path = workflow._assemble_video(script_data, audio_files, visual_files)
        
        print("\n" + "="*60)
        print("✅ SUCCESS! PuppyLinux Video Created")
        print("="*60)
        print(f"Video path: {video_path}")
        print(f"Script: {script_path}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_puppy_linux_video()
