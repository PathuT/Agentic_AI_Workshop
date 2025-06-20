from langchain import PromptTemplate

parser_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Extract LinkedIn OKR JSON with these fields:
- activity_type, description, evidence_url, student_id, date
Return only valid JSON.

Input:
{text}
"""
)

validator_prompt = PromptTemplate(
    input_variables=["okr_json", "evidence_snippet"],
    template="""
Validate the LinkedIn OKR:
OKR_JSON: {okr_json}
EVIDENCE_SNIPPET: {evidence_snippet}

Return JSON with:
exists: bool
authorship_match: bool
within_time_window: bool
reasons: list
"""
)

scoring_prompt = PromptTemplate(
    input_variables=["parser_json"],
    template="""
Given this OKR JSON, score it:
Input: {parser_json}
Return JSON: {{score:int, relevance:int, credibility:int, completeness:int}}
"""
)

analyzer_prompt = PromptTemplate(
    input_variables=["parser_json","validator_json","score_json"],
    template="""
Identify discrepancies in these:
parser: {parser_json}
validator: {validator_json}
score: {score_json}

Return JSON:
{{
  issues: list,
  suggestions: list
}}
"""
)

compiler_prompt = PromptTemplate(
    input_variables=["all_data"],
    template="""
Compile results summary:
{all_data}
Return final JSON summary.
"""
)

feedback_prompt = PromptTemplate(
    input_variables=["feedback"],
    template="""
Process feedback: {feedback}
Return JSON with status and log ID.
"""
)
