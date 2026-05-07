#!/usr/bin/env python3
"""
Launch script for AI Shorts Creator

Run this to start the Shorts Creator interface directly.
"""

import os
import sys

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
os.environ["PATH"] += os.pathsep + current_dir

# Set page config before importing streamlit modules
import streamlit as st
st.set_page_config(
    page_title="AI Shorts Creator",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import and run the shorts creator
from shorts_creator.shorts_ui import shorts_creator_page

if __name__ == "__main__":
    shorts_creator_page()
