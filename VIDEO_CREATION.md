# Video Creation Guide - AI Shorts Creator

This guide walks you through creating a short-form video using the AI Shorts Creator extension.

> **For technical details and features, see [AI_VIDEO_SHORTS.md](AI_VIDEO_SHORTS.md)**

---

## Prerequisites

1. **API Keys** - See [AI_VIDEO_SHORTS.md](AI_VIDEO_SHORTS.md#configuration) for required keys
   - LLM API required for script generation
   - Edge TTS works free without API key

2. **Dependencies**:
   ```bash
   cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
   source .venv/bin/activate
   ```

---

## Method 1: Streamlit UI (Recommended)

### Step 1: Launch the App

```bash
cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
source .venv/bin/activate
streamlit run st.py
```

### Step 2: Navigate to Shorts Creator

1. Open browser to `http://localhost:8501`
2. Click on **"🎬 AI Shorts Creator"** tab

### Step 3: Quick Create (Simple)

1. **Enter Video Topic**: e.g., "5 tips for better productivity"
2. **Select Duration**: 15, 30, 45, 60, or 90 seconds
3. **Select Content Style**: educational, entertainment, motivational, etc.
4. **Select Language**: English, Spanish, French, etc.
5. **Select Tone**: casual, professional, enthusiastic, calm
6. **Select Voice**: en-US-GuyNeural, en-US-JennyNeural, etc.
7. **Click "🎬 Create Video"**

### Step 4: Wait for Processing

The app will:
1. Generate script using AI
2. Create voiceover using TTS
3. Fetch/generate visuals
4. Assemble final video

Progress will be shown in the UI.

### Step 5: Download Video

Once complete:
- Video will display in the UI
- Click **"📥 Download Video"** to save
- Videos are saved to `output/shorts/final/`

---

## Method 2: Standalone Shorts App

### Step 1: Launch Shorts Creator Only

```bash
cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
source .venv/bin/activate
streamlit run launch_shorts.py
```

This opens the Shorts Creator directly without the main VideoLingo interface.

---

## Method 3: Programmatic (Python Script)

### Step 1: Create a Script

Create `my_video.py`:

```python
from shorts_creator.shorts_workflow import ShortsWorkflow, WorkflowConfig

# Configure the workflow
config = WorkflowConfig(
    script_style='educational',
    script_duration=60,
    script_tone='casual',
    script_language='English',
    tts_method='edge_tts',
    tts_voice='en-US-GuyNeural',
    prefer_stock=True,
    image_style='photorealistic',
    image_engine='pollinations',  # Free option
    add_captions=True,
    add_background_music=False,
    output_dir='output/shorts'
)

# Create workflow
workflow = ShortsWorkflow(config)

# Generate video
result = workflow.create_video(
    topic="5 tips for better productivity",
    progress_callback=lambda pct, msg: print(f"[{pct}%] {msg}")
)

print(f"Video created: {result['video_path']}")
```

### Step 2: Run the Script

```bash
cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
source .venv/bin/activate
python my_video.py
```

---

## Method 4: Demo Script

A demo script is included for testing:

```bash
cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
source .venv/bin/activate
python demo_shorts.py
```

This will:
1. Generate a sample script
2. Create AI images using Pollinations (free)
3. Assemble a test video

---

> **Output location**: See [AI_VIDEO_SHORTS.md](AI_VIDEO_SHORTS.md#output-structure)

---

## Troubleshooting

### "No API key found"
- Check `config.yaml` has required API keys
- For free options: Edge TTS and Pollinations work without keys

### "MoviePy error"
- Ensure MoviePy v2 is installed: `pip show moviepy`
- Version should be 2.x.x

### "TextClip font error"
- Install fonts: `apt-get install fonts-liberation` (Linux)
- Or use a different font in config

### "Audio generation failed"
- Check TTS configuration in `config.yaml`
- Edge TTS is most reliable (free)

### "Image generation failed"
- Pollinations is free and doesn't require API key
- For better quality, configure HuggingFace API key

### "ModuleNotFoundError: No module named 'demucs'" or "No module named 'demucs.api'"
The main VideoLingo app requires demucs for audio separation. The installed version may be incompatible. Fix:
```bash
cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
source .venv/bin/activate
pip install demucs --upgrade
```

**Alternative**: Use the **Standalone Shorts App** or **Demo Script** instead (see below) - they don't require demucs.

### "ModuleNotFoundError: No module named 'torch'"
Torch is required for audio processing. Fix:
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
```

---

## Alternative Methods (Bypass Main App Dependencies)

If the main Streamlit app fails due to missing dependencies (demucs, torch, whisperx), use **Method 2** (Standalone App) or **Method 4** (Demo Script) instead - they only require Shorts Creator dependencies.

---

## Quick Test Command

For a quick test that everything works:

```bash
cd /root/a_VIDEO_GENERATION/VideoLingo/Lingo
source .venv/bin/activate
python -c "
from shorts_creator.script_generator import ScriptGenerator
gen = ScriptGenerator()
script = gen.generate_script('Test topic', duration=30, style='educational')
print('✅ Script generation works!')
print(f'Title: {script[\"title\"]}')
"
```

---

## Tips for Best Results

1. **Topics**: Be specific - "5 productivity tips for remote workers" > "productivity"
2. **Duration**: 30-60 seconds work best for TikTok/Reels
3. **Style**: Match style to platform (educational for TikTok, entertainment for Reels)
4. **Voice**: Test different voices to find the right tone
5. **Visuals**: Stock footage looks more professional; AI images are more unique

---

## Next Steps

After creating your video:
1. Review in `output/shorts/final/`
2. Upload to TikTok/Instagram/YouTube
3. Use the generated hashtags (in script JSON)
4. Iterate on topics and styles based on performance

---

## Success Story: PuppyLinux Video

**Date**: 2026-05-07

**Video Created**: `Why PuppyLinux is the Ultimate_1778184458.mp4`

**Settings Used**:
- Topic: "The advantages of PuppyLinux"
- Style: `motivational`
- Tone: `calm`
- Voice: `en-US-GuyNeural`
- Duration: 60 seconds

**Method Used**: Standalone Shorts App (`streamlit run launch_shorts.py`)

**Why Standalone?** The main VideoLingo app required demucs/torch/whisperx dependencies. The standalone app bypassed these and worked immediately.

**Result**: ✅ Successfully created a motivational short-form video about PuppyLinux with:
- AI-generated script
- Edge TTS voiceover
- AI-generated visuals (Pollinations)
- Captions and transitions

**Lessons Learned**:
1. Use `launch_shorts.py` if main app has dependency issues
2. Edge TTS + Pollinations = fully free video creation
3. Motivational + calm tone works well for educational content
