from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import sys
import os
from typing import Optional

# Add your existing app directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from utils.doc_utils import extract_text_from_pdf, extract_text_from_image
from ai.pipeline import run_agents

app = FastAPI(
    title="Agentic AI Submission Validator API",
    description="API for validating student submissions using multi-agent AI system",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/validate")
async def validate_submission(
    text_input: Optional[str] = Form(None),
    submission_file: Optional[UploadFile] = File(None),
    reference_file: Optional[UploadFile] = File(None),
):
    """
    Validate a submission with optional file uploads and text input.
    Replicates the Streamlit validation functionality.
    """
    try:
        submit_text = ""
        img = None
        
        # Process submission file
        if submission_file:
            if submission_file.content_type == "application/pdf":
                submit_text = extract_text_from_pdf(submission_file.file)
            else:
                # Handle image file
                img_data = await submission_file.read()
                img = Image.open(io.BytesIO(img_data))
                submit_text = extract_text_from_image(img)
        elif text_input and text_input.strip():
            submit_text = text_input.strip()
            
        if not submit_text:
            raise HTTPException(
                status_code=400, 
                detail="Please provide a submission via file or text"
            )
            
        # Process reference file if provided
        ref_file_obj = None
        if reference_file:
            ref_file_obj = io.BytesIO(await reference_file.read())
            ref_file_obj.name = reference_file.filename
            
        # Run the validation pipeline
        result = run_agents(submit_text, ref_file_obj, img)
        
        # Prepare response (matching Streamlit output structure)
        response = {
            "status": "success",
            "result": {
                "plagiarism": result.get('plagiarism', False),
                "parsed": result.get('parsed', {}),
                "credential": result.get('credential', None),
                "web_validation": result.get('web_validation', None)
            }
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Validation failed: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "1.0.0"}