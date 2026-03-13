from nexus_lm.audio.tts_stack import AudioSynthesisStack
import pytest

def test_audio_uninitialized():
    stack = AudioSynthesisStack("kokoro")
    with pytest.raises(RuntimeError):
        stack.synthesize("test")

def test_audio_synthesis():
    stack = AudioSynthesisStack("vibevoice")
    res = stack.initialize()
    assert "vibevoice backend initialized" in res
    audio = stack.synthesize("Hello")
    assert audio.startswith(b"MOCK_AUDIO")
    assert b"Hello" in audio
