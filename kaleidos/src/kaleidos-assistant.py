import logging
from typing import Dict, List

class KaleidosKnowledgeBase:
    def __init__(self, log_level=logging.INFO):
        """
        Initialize Kaleidos's Knowledge Base
        
        Args:
            log_level (int): Logging level for the knowledge base
        """
        logging.basicConfig(level=log_level, 
                            format='[Kaleidos KB] %(asctime)s - %(levelname)s: %(message)s')
        self.logger = logging.getLogger(__name__)
        
        self.knowledge: Dict[str, List[str]] = {
            "alora_core_facts": [
                "Kaleidos is an advanced AI assistant",
                "Kaleidos aims to provide intelligent and contextual responses",
                "Continuous learning is a key principle of Kaleidos's design"
            ],
            "tech_facts": [
                "AI is rapidly evolving",
                "Machine learning enables adaptive systems",
                "Natural language processing is crucial for understanding context"
            ]
        }
        
        self.logger.info("Kaleidos Knowledge Base initialized")
        
    def query(self, query: str) -> Dict[str, List[str]]:
        """
        Query the knowledge base for relevant information
        
        Args:
            query (str): Search query
        
        Returns:
            Dict of relevant knowledge sections
        """
        try:
            # Convert query to lowercase for case-insensitive searching
            query_lower = query.lower()
            
            # Search across all knowledge sections
            relevant_knowledge = {
                section: [
                    fact for fact in facts 
                    if query_lower in fact.lower()
                ]
                for section, facts in self.knowledge.items()
            }
            
            # Filter out empty sections
            relevant_knowledge = {
                k: v for k, v in relevant_knowledge.items() if v
            }
            
            self.logger.info(f"Processed query: {query}")
            return relevant_knowledge
        
        except Exception as e:
            self.logger.error(f"Knowledge base query error: {e}")
            return {}
    
    def add_knowledge(self, section: str, fact: str) -> bool:
        """
        Add new knowledge to a specific section
        
        Args:
            section (str): Knowledge section
            fact (str): Fact to add
        
        Returns:
            bool: Whether addition was successful
        """
        try:
            if section not in self.knowledge:
                self.knowledge[section] = []
            
            self.knowledge[section].append(fact)
            self.logger.info(f"Added fact to {section}: {fact}")
            return True
        
        except Exception as e:
            self.logger.error(f"Error adding knowledge: {e}")
            return False
