from typing import Dict

class RouterAgent:
    def invoke(self, inputs: dict) -> dict:
        query = inputs.get("input", "").lower()

        if any(word in query for word in ["latest", "current", "news", "today", "update"]):
            return {"route": "web", "input": query}
        
        elif any(word in query for word in ["dataset", "data", "knowledge base", "document"]):
            return {"route": "rag", "input": query}
        
        else:
            return {"route": "llm", "input": query}




    def invoke(self, inputs: Dict) -> Dict:
        plan = self.plan(None, **inputs)
        return plan
