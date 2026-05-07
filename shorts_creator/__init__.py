"""
Shorts Creator Module - AI-powered short-form video generation

This module extends VideoLingo for automated content creation:
- AI script writing
- TTS voiceover generation
- Stock footage/image generation
- TikTok/Reels style video assembly
"""

from .script_generator import ScriptGenerator
from .footage_generator import FootageGenerator
from .video_assembler import VideoAssembler

__all__ = ['ScriptGenerator', 'FootageGenerator', 'VideoAssembler']
