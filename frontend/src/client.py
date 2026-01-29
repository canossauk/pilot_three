
# 
#  Import LIBRARIES
import httpx
from typing import List, Dict, Any, Optional
#  Import FILES
#  __________________________
# #


BASE_URL = "http://127.0.0.1:8000"

class SchoolClient:
    async def get_students(self) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{BASE_URL}/students/")
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                print(f"An error occurred while requesting {e.request.url!r}.")
                return []
            except httpx.HTTPStatusError as e:
                print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
                return []

    async def add_student(self, name: str, email: str, major: str, age: Optional[int] = None) -> Optional[Dict[str, Any]]:
        student_data = {
            "name": name, 
            "email": email, 
            "major": major,
            "age": age
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{BASE_URL}/students/", json=student_data)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                print(f"Error adding student: {e}")
                return None
