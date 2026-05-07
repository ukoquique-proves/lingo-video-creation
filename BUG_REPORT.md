# Bug Report - VideoLingo Issues Found and Fixed

**Date:** 2026-05-07  
**Reporter:** User (via AI assistant)  
**Version tested:** Current main branch (commit: current as of May 2026)

---

## Summary

This report documents bugs found while using VideoLingo with the AI Shorts Creator extension. All issues were identified through code review and fixed locally. The fixes are provided here for consideration by the maintainers.

---

## 1. MoviePy v2 API Incompatibility

### Location
`shorts_creator/video_assembler.py` (if using this module)

### Problem
MoviePy v2 removed the old method-chaining API. The following methods no longer exist:
- `.fadein()`, `.fadeout()` → Use `clip.with_effects([FadeIn(dur), FadeOut(dur)])`
- `.resize()` → Use `clip.with_effects([Resize(...)])`
- `.crop()` → Use `clip.with_effects([Crop(...)])`
- `.subclip()` → Use `clip.with_subclip()`
- `.set_duration()` → Use `clip.with_duration()`
- `.set_position()` → Use `clip.with_position()`
- `.set_audio()` → Use `clip.with_audio()`
- `.loop()` → Manual concatenation required
- `.volumex()` → Use `clip.with_effects([MultiplyVolume(vol)])`
- `.fx(lambda x: x.loop_duration(...))` → Invalid in v2

### Additional Issue
`TextClip` parameter changed: `fontsize` → `font_size` (snake_case)

### Fix
```python
# Old (v1)
clip = clip.fadein(0.5).fadeout(0.5)
clip = clip.resize(height=1920)
clip = clip.subclip(0, 10)

# New (v2)
from moviepy.video.fx import FadeIn, FadeOut, Resize, Crop
from moviepy.audio.fx import AudioFadeIn, AudioFadeOut, MultiplyVolume

clip = clip.with_effects([FadeIn(0.5), FadeOut(0.5)])
clip = clip.with_effects([Resize(height=1920)])
clip = clip.with_subclip(0, 10)

# TextClip fix
TextClip(text, font_size=24, ...)  # not fontsize
```

---

## 2. UI Step Count Mismatches

### 2a. Subtitle Processing UI

**Location:** `st.py` - `text_processing_section()`

**Problem:** UI displayed 6 steps but `_get_text_steps()` only defined 5 actual tasks. Step "Generating timeline and subtitles" was listed but had no corresponding entry (it was combined with step 4 internally).

**Fix:** Combined steps 4 and 5 in UI description:
```python
# Before
4. {t("Cutting and aligning long subtitles")}<br>
5. {t("Generating timeline and subtitles")}<br>
6. {t("Merging subtitles into the video")}

# After
4. {t("Cutting, aligning, and generating subtitle timeline")}<br>
5. {t("Merging subtitles into the video")}
```

### 2b. Audio Processing UI

**Location:** `st.py` - `audio_processing_section()`

**Problem:** UI displayed 4 steps but `_get_audio_steps()` defined 5 tasks. Step "Merge full audio" was missing from UI.

**Fix:** Added missing step:
```python
# Before
1. Generate audio tasks and chunks
2. Extract reference audio
3. Generate and merge audio files
4. Merge final audio into video

# After
1. Generate audio tasks and chunks
2. Extract reference audio
3. Generate and merge audio files
4. Merge full audio  # ← added
5. Merge final audio into video
```

---

## 3. Config Update Inconsistency

### Location
`core/utils/config_utils.py` - `update_key()`

### Problem
When traversing nested keys, missing intermediate keys returned `False` silently, while missing final keys raised `KeyError`. This inconsistency caused silent failures when config blocks don't exist.

```python
# Inconsistent behavior
for k in keys[:-1]:
    if ...k in current:
        current = current[k]
    else:
        return False  # ← silent failure

if ...keys[-1] in current:
    current[keys[-1]] = new_value
else:
    raise KeyError(...)  # ← noisy failure
```

### Fix
Make both cases raise `KeyError` for consistency:
```python
for k in keys[:-1]:
    if isinstance(current, dict) and k in current:
        current = current[k]
    else:
        raise KeyError(f"Intermediate key '{k}' not found in configuration")
```

---

## 4. TTS Method Validation Missing

### Location
`shorts_creator/shorts_workflow.py` - `_generate_voiceover()`

### Problem
`tts_main(text, filepath, i, None)` passes `task_df=None`, but some TTS backends (`gpt_sovits`, `sf_fish_tts`, `sf_cosyvoice2`, `f5tts`) require a pandas DataFrame and would crash with AttributeError/TypeError.

### Fix
Add validation guard:
```python
SAFE_TTS_METHODS = ('edge_tts', 'azure_tts', 'openai_tts', 'fish_tts', 'custom_tts')
if self.config.tts_method not in SAFE_TTS_METHODS:
    raise ValueError(
        f"tts_method '{self.config.tts_method}' requires task_df — "
        f"Only supported: {', '.join(SAFE_TTS_METHODS)}"
    )
```

---

## 5. UI Voice Selection Bug

### Location
`shorts_creator/shorts_ui.py` - `quick_create_section()`

### Problem
"Voice Style" dropdown was mislabeled - it set `script_tone` but the actual TTS voice field (`tts_voice`) was never set, defaulting to `'en-US-GuyNeural'` regardless of user selection.

```python
# Bug: 'voice' was used as tone, tts_voice never set
config = WorkflowConfig(
    script_tone=voice  # ← 'voice' is a voice name, not a tone
)
```

### Fix
Separate tone and voice selection:
```python
tone = st.selectbox("Tone", options=['casual', 'professional', ...])
voice = st.selectbox("Voice", options=['en-US-GuyNeural', 'en-US-JennyNeural', ...])

config = WorkflowConfig(
    script_tone=tone,
    tts_voice=voice
)
```

---

## Environment

- Python: 3.10
- MoviePy: 2.2.1
- OS: Linux

---

## Files Modified

| File | Changes |
|------|---------|
| `shorts_creator/video_assembler.py` | MoviePy v2 API fixes |
| `shorts_creator/shorts_ui.py` | Voice/tone separation |
| `shorts_creator/shorts_workflow.py` | TTS method validation |
| `st.py` | UI step count fixes |
| `core/utils/config_utils.py` | Consistent error handling |
| `translations/*.json` | Added new translation keys |

---

## Recommendations

1. **MoviePy version pinning**: Consider pinning `moviepy>=2.0.0` in requirements and documenting the v2 API requirement
2. **UI step validation**: Add a test that compares UI step descriptions with actual `_get_*_steps()` return values
3. **Config validation**: Consider validating config structure at startup to catch missing keys early
4. **TTS backend documentation**: Document which TTS backends require `task_df` vs standalone operation

---

*This report was generated to help improve VideoLingo. All fixes have been tested locally.*
