import os
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Base model to take user inputs
class BookUpdate(BaseModel):
    book_id: int
    new_update_copies: int


@app.put("/")
async def update_book(bookupdate: BookUpdate):
    try:
        SUPABASE_URL = os.environ.get("SUPABASE_URL")
        SUPABASE_API_KEY = os.environ.get("SUPABASE_API_KEY")

        supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

        book_id = bookupdate.book_id
        new_update_copies = bookupdate.new_update_copies

        # Query to update available copies
        data = supabase.table("books").update({"available_copies": new_update_copies}).eq("id", book_id).execute()
        return {"message": f"The book with ID {book_id} has been successfully updated. The new available copies are now {new_update_copies}."}

    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}


# at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
