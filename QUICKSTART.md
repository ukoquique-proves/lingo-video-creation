# Quick Start Guide - AI Shorts Creator

## Installation Status

✅ Repository cloned: `Huanshere/VideoLingo`
✅ Shorts Creator module added
✅ Dependencies installed

## What's Been Added

### New Module: `shorts_creator/`

A complete short-form video creation system:

| File | Purpose |
|------|---------|
| `script_generator.py` | AI-powered script writing for TikTok/Reels |
| `footage_generator.py` | Stock footage + AI image generation |
| `video_assembler.py` | Video compilation with captions |
| `shorts_workflow.py` | Complete automated workflow |
| `shorts_ui.py` | Streamlit user interface |

### Key Features

1. **AI Script Writing**
   - Multiple styles: educational, entertainment, motivational, how_to, listicle
   - Automatic hook generation for engagement
   - Hashtag suggestions

2. **TTS Voiceover**
   - Edge TTS (FREE) - default
   - Azure TTS, OpenAI TTS - optional

3. **Visual Generation**
   - **Pollinations.ai** - FREE AI image generation (no API key needed)
   - FLUX / Stable Diffusion via HuggingFace (free tier)
   - Stock footage from Pexels/Pixabay (free tiers)

4. **Video Assembly**
   - 9:16 aspect ratio (TikTok/Reels format)
   - Automatic captions
   - Background music support
   - Transitions and effects

## How to Use

### Method 1: Streamlit UI (Recommended)

```bash
# After installation completes:
.venv/bin/streamlit run st.py
```

Then click the **"🎬 AI Shorts Creator"** tab.

### Method 2: Standalone Shorts Creator

```bash
.venv/bin/streamlit run launch_shorts.py
```

### Method 3: Programmatic

```python
from shorts_creator.shorts_workflow import quick_create_video

video_path = quick_create_video(
    topic="5 productivity tips",
    duration=60,
    style='educational'
)
```

## Configuration

Edit `config.yaml` to set your API keys:

```yaml
# LLM API (required for script generation)
api:
  key: 'your-openai-api-key'
  base_url: 'https://api.openai.com/v1'
  model: 'gpt-4'

# Optional: For stock footage
# Pexels: https://www.pexels.com/api/
# Pixabay: https://pixabay.com/api/docs/

# Optional: For FLUX/SD image generation
# HuggingFace: https://huggingface.co/settings/tokens
```

**Note:** You can use the system without API keys:
- Script generation requires an LLM API
- Image generation works with free Pollinations.ai
- TTS works with free Edge TTS

## Demo

Run the demo script to see capabilities:

```bash
python demo_shorts.py
```

## Output Location

Created videos are saved to:
```
output/shorts/
├── scripts/     # Generated scripts (JSON)
├── audio/       # Voiceover files (WAV)
├── footage/     # Visual assets
│   ├── stock/   # Downloaded stock media
│   └── generated/ # AI-generated images
└── final/       # Completed videos (MP4)
```

## Next Steps

1. Configure your API key in `config.yaml` for script generation
2. Run: `.venv/bin/streamlit run st.py`
3. Click "🎬 AI Shorts Creator" tab
4. Enter a topic and create your first video!

## Documentation

- `AI_VIDEO_SHORTS.md` - Complete feature documentation
- `shorts_creator/README.md` - Module documentation
- `CHANGELOG.md` - Technical changes only
