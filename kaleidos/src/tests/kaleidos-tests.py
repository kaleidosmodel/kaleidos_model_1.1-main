import pytest
from src.ai_assistant import KaleidosAssistant
from src.models.reasoning_engine import KaleidosReasoningEngine
from src.utils.knowledge_base import KaleidosKnowledgeBase

def test_alora_assistant_initialization():
    """Test that Kaleidos Assistant initializes correctly."""
    assistant = KaleidosAssistant()
    assert isinstance(assistant.reasoning_engine, KaleidosReasoningEngine)
    assert isinstance(assistant.knowledge_base, KaleidosKnowledgeBase)

def test_process_input():
    """Test the process_input method returns a response."""
    assistant = KaleidosAssistant()
    response = assistant.process_input("Hello, Kaleidos! How are you today?")
    assert isinstance(response, str)
    assert len(response) > 0

def test_reasoning_engine():
    """Test the Kaleidos Reasoning Engine analysis method."""
    engine = KaleidosReasoningEngine()
    result = engine.analyze("Test input for Kaleidos")
    assert isinstance(result, dict)
    assert "sentiment" in result
    assert "entities" in result
    assert "logical_inference" in result
    assert "complexity" in result

def test_knowledge_base():
    """Test the Kaleidos Knowledge Base query method."""
    kb = KaleidosKnowledgeBase()
    result = kb.query("AI")
    assert isinstance(result, dict)
    assert len(result) > 0
