# AI Video Shorts Creator

## Overview

This is a personalized extension of VideoLingo that creates automated short-form videos for TikTok, Instagram Reels, and YouTube Shorts.

## What Was Built

### Complete Shorts Creation Pipeline

1. **Script Generator** (`shorts_creator/script_generator.py`)
   - AI-powered script writing using LLM
   - Automatic hook generation for engagement
   - Multiple content styles (educational, entertainment, motivational, etc.)
   - Hashtag suggestions
   - Script enhancement options

2. **Footage Generator** (`shorts_creator/footage_generator.py`)
   - Stock footage from Pexels and Pixabay (free tiers available)
   - AI image generation via:
     - **Pollinations.ai** (FREE, no API key)
     - FLUX via HuggingFace
     - Stable Diffusion XL via HuggingFace
   - Automatic visual matching to script segments

3. **Video Assembler** (`shorts_creator/video_assembler.py`)
   - TikTok/Reels format (9:16 aspect ratio, 1080x1920)
   - Automatic caption overlay
   - Background music support
   - Transitions and fade effects
   - Watermark options

4. **Complete Workflow** (`shorts_creator/shorts_workflow.py`)
   - One-click video creation from topic
   - Video series generation
   - Progress tracking
   - Error handling

5. **Streamlit UI** (`shorts_creator/shorts_ui.py`)
   - Quick Create interface
   - Advanced options panel
   - History browser
   - Integrated into main VideoLingo app

## Free Features (No API Key Required)

| Feature | Free Option | Notes |
|---------|-------------|-------|
| Image Generation | Pollinations.ai | No API key needed, good quality |
| Voiceover | Edge TTS | Free, multiple voices |
| Stock Footage | Pexels/Pixabay | Free tiers available |
| Script Generation | ❌ Requires API | OpenAI, Claude, etc. |

## Installation

```bash
# Virtual environment already created
# Dependencies installed

# Start the app
.venv/bin/streamlit run st.py
```

## Usage

### Quick Create
1. Click "🎬 AI Shorts Creator" tab
2. Enter video topic
3. Select duration (15-90 seconds)
4. Choose style
5. Click "Create Video"

### Advanced Options
- Customize tone, hook type, target audience
- Select TTS engine and voice
- Choose image generation engine
- Configure captions and music

### Programmatic Usage

```python
from shorts_creator.shorts_workflow import quick_create_video

video_path = quick_create_video(
    topic="5 productivity tips",
    duration=60,
    style='educational'
)
```

## Configuration

Add your LLM API key to `config.yaml`:

```yaml
api:
  key: 'your-api-key'
  base_url: 'https://api.openai.com/v1'
  model: 'gpt-4'
```

Optional API keys for enhanced features:
- Pexels API key (stock footage)
- Pixabay API key (stock footage)
- HuggingFace API key (FLUX/SD image generation)

## Output Structure

```
output/shorts/
├── scripts/     # Generated scripts (JSON)
├── audio/       # Voiceover segments (WAV)
├── footage/     # Visual assets
│   ├── stock/   # Downloaded stock media
│   └── generated/ # AI-generated images
└── final/       # Completed videos (MP4)
```

## Content Styles

- `educational` - Teaching content
- `entertainment` - Fun, engaging content
- `motivational` - Inspiring content
- `how_to` - Tutorial, step-by-step
- `listicle` - List-based (e.g., "5 tips...")
- `facts` - Interesting facts/trivia
- `storytelling` - Narrative content
- `news` - Trending topics

## Documentation

- `QUICKSTART.md` - Quick start guide
- `shorts_creator/README.md` - Module documentation
- `demo_shorts.py` - Demo script
- `CHANGELOG.md` - Technical changes only

## Original Goal

> Use AI tokens to write a script, generate a voiceover (TTS), and then pull relevant stock footage or generate images (using free Flux/Stable Diffusion APIs) to assemble a complete short-form video (TikTok/Reels style).

**Status: ✅ FULLY IMPLEMENTED**
