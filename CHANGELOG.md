# Changelog

**Note**: This changelog is for tracking very technical and small changes only. Major feature additions and documentation are maintained in `AI_VIDEO_SHORTS.md` and `QUICKSTART.md`.

## [Unreleased] - 2026-05-07

### Fixed
- **MoviePy v2 API compatibility** in `shorts_creator/video_assembler.py`
  - Replaced deprecated v1 method-chaining API with v2 API
  - Simplified to v2-only code (no backward compatibility checks)
  - Fixed TextClip: `fontsize` → `font_size` (snake_case)
  - Fixed TextClip: `align` → `text_align` (v2 requirement)
  - Removed deprecated `transparent` argument from TextClip
  - Fixed TextClip: moved `duration` from constructor to `.with_duration()` (v2 requirement)
  - Added explicit font path to `VideoConfig` and `TextClip` to prevent "Invalid font" errors on Linux
  - Switched `TextClip` calls to use keyword arguments for better compatibility with MoviePy v2
- **Quick Create UI** in `shorts_creator/shorts_ui.py`
  - Separated "Tone" (script style) from "Voice" (TTS voice name)
  - Added proper voice selection dropdown with Edge TTS voices
  - `tts_voice` now correctly set instead of being ignored
- **TTS method validation** in `shorts_creator/shorts_workflow.py`
  - Added guard to reject TTS methods that require `task_df`
  - Only allows: edge_tts, azure_tts, openai_tts, fish_tts, custom_tts
- **Subtitle processing UI** in `st.py`
  - Fixed step count mismatch: UI now shows 5 steps (matching actual tasks)
  - Combined "Cutting/aligning" and "Generating timeline" into one step
- **Audio processing UI** in `st.py`
  - Added missing "Merge full audio" step to UI (was hidden, causing 4 vs 5 mismatch)
- **Config update consistency** in `core/utils/config_utils.py`
  - `update_key()` now raises `KeyError` for missing intermediate keys (was silent `False`)
  - Consistent error handling for both intermediate and final missing keys
- **Reference-before-assignment bug** in `shorts_creator/video_assembler.py`
  - Fixed `_add_captions()`: `txt.h` was used before `txt` object existed
  - Split TextClip creation and positioning into two separate lines
- **Project Configuration Defaults** in `config.yaml`
  - Switched `display_language` and `target_language` to English for educational video creation
  - Set `tts_method` to `edge_tts` and updated default voice to `en-US-GuyNeural` for free, high-quality English voiceovers
  - Disabled `demucs` by default to streamline workflow and reduce dependency overhead

### Added
- **AI Shorts Creator Module** - Complete short-form video creation system
  - `shorts_creator/script_generator.py` - AI-powered script writing with LLM
  - `shorts_creator/footage_generator.py` - Stock footage + AI image generation
  - `shorts_creator/video_assembler.py` - TikTok/Reels format video assembly
  - `shorts_creator/shorts_workflow.py` - Complete automated workflow
  - `shorts_creator/shorts_ui.py` - Streamlit user interface
- **Manual Video Creation Script** - `create_puppy_linux_video.py`
  - Added a specialized script to generate a video about PuppyLinux advantages
  - Bypasses LLM API requirement by providing a pre-defined script structure
  - Demonstrates end-to-end workflow (TTS, AI Images, Assembly) using free tools

### Features
- **Script Generation**
  - Multiple content styles (educational, entertainment, motivational, how-to, listicle, facts, storytelling, news)
  - Automatic hook generation for engagement
  - Hashtag suggestions
  - Script enhancement options
  - Video series generation

- **Footage Generation**
  - Stock footage from Pexels and Pixabay (free tiers)
  - AI image generation via Pollinations.ai (FREE, no API key)
  - AI image generation via FLUX (HuggingFace)
  - AI image generation via Stable Diffusion XL (HuggingFace)
  - Automatic visual matching to script segments

- **Video Assembly**
  - TikTok/Reels format (9:16 aspect ratio, 1080x1920)
  - Automatic caption overlay
  - Background music support
  - Transitions and fade effects
  - Watermark options

- **User Interface**
  - Quick Create interface
  - Advanced options panel
  - History browser
  - Integrated into main VideoLingo app as "🎬 AI Shorts Creator" tab

### Free Options (No API Key Required)
- Pollinations.ai for AI image generation
- Edge TTS for voiceover synthesis
- Pexels/Pixabay free tiers for stock footage

### Configuration
- Added `WorkflowConfig` dataclass for easy configuration
- Added `VideoConfig` dataclass for video output settings
- Support for multiple TTS engines (Edge, Azure, OpenAI)
- Support for multiple image generation engines (Pollinations, FLUX, SD)

### Documentation
- `AI_VIDEO_SHORTS.md` - Main documentation for the Shorts Creator module
- `QUICKSTART.md` - Quick start guide
- `shorts_creator/README.md` - Module documentation
- `demo_shorts.py` - Demo script for testing capabilities
- `launch_shorts.py` - Standalone launcher for Shorts Creator

### Integration
- Modified `st.py` to include "🎬 AI Shorts Creator" tab
- Added `shorts_creator_section()` function to main app

### Dependencies
- Added moviepy for video processing
- Added Pillow for image handling
- Added pydub for audio processing
- Added requests for API calls

### Testing
- Verified Pollinations.ai image generation works correctly
- Verified all modules import successfully
- Verified MoviePy 2.x compatibility

---

## [Original] - VideoLingo Base

### Original Features
- YouTube video download via yt-dlp
- WhisperX word-level subtitle recognition
- NLP and AI-powered subtitle segmentation
- Custom + AI-generated terminology
- 3-step Translate-Reflect-Adaptation
- Netflix-standard single-line subtitles
- Dubbing with GPT-SoVITS, Azure, OpenAI, etc.
- Multi-language support
- Detailed logging with progress resumption
