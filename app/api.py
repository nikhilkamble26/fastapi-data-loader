from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.data_loader import UnifiedDataLoader
from app.core.file_utils import save_upload_file, delete_file
from app.schemas import LoadResponse

router = APIRouter()
loader = UnifiedDataLoader()


@router.post("/load", response_model=LoadResponse)
async def load_file(file: UploadFile = File(...)):
    file_path = save_upload_file(file)

    try:
        documents = loader.load(file_path)
        return {"status": "success", "documents": documents}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        delete_file(file_path)
