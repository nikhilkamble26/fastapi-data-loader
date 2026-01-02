from pydantic import BaseModel
from typing import List, Dict, Any


class Document(BaseModel):
    text: str
    metadata: Dict[str, Any]

class LoadResponse(BaseModel):
    status: str
    documents: List[Document]