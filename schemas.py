from pydantic import BaseModel
from typing import Optional

class PromptRequest(BaseModel): 
    prompt: str 

class ToolMetadata(BaseModel):
    tool_name: str
    success: bool
    error_message: Optional[str] = None

class PromptResponse(BaseModel):
    response: str  
    metadata: Optional[ToolMetadata] = None



