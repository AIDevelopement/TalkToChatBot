import streamlit as st
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("my_header", "https://github.com/AIDevelopement/TalkToChatBot/blob/main/My_header.pyc")
my_header = importlib.util.module_from_spec(spec)
sys.modules["my_header"] = my_header
spec.loader.exec_module(my_header)

my_header.setup_ui()
my_header.handle_chat()
