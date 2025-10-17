import re
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import json

def camel_to_snake_case(name: str) -> str:
    """
    Convert a camelCase string to snake_case.
    
    Args:
        name (str): The camelCase string to convert.
        
    Returns:
        str: The converted snake_case string.
    """

    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def snake_to_camel_case(name: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
        name (str): The snake_case string to convert.

    Returns:
        str: The converted camelCase string.
    """
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def convert_keys_to_snake_case(data: dict) -> dict:
    """
    Convert all keys in a dictionary from camelCase to snake_case.

    Args:
        data (dict): The dictionary with camelCase keys.

    Returns:
        dict: A new dictionary with snake_case keys.
    """
    
    if isinstance(data, dict):
        return {camel_to_snake_case(key) : convert_keys_to_snake_case(value) for key, value in data.items()}
    
    elif isinstance(data, list):
        return [convert_keys_to_snake_case(item) for item in data]
    else:
        return data
    
def convert_keys_to_camel_case(data: dict) -> dict:
    """
    Convert all keys in a dictionary from snake_case to camelCase.

    Args:
        data (dict): The dictionary with snake_case keys.

    Returns:
        dict: A new dictionary with camelCase keys.
    """
    
    if isinstance(data, dict):
        return {snake_to_camel_case(key) : convert_keys_to_camel_case(value) for key, value in data.items()}
    
    elif isinstance(data, list):
        return [convert_keys_to_camel_case(item) for item in data]
    else:
        return data
    
class CaseConversionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        if request.url.path in ["/api/v1/openapi.json", "/api/v1/docs", "/api/v1/redoc"] or request.url.path.startswith("/docs") or request.url.path.startswith("/redoc"):
            return await call_next(request)

        if request.headers.get("content-type", "") == "application/json":
            body = await request.body()

            if body:
                try:
                    raw_data = json.loads(body)
                    snake_case_data = convert_keys_to_snake_case(raw_data)

                    async def receive():
                        return {
                            "type": "http.request",
                            "body": json.dumps(snake_case_data).encode("utf-8"),
                            "more_body": False,
                        }

                    request._receive = receive
                except json.JSONDecodeError:
                    pass

        response = await call_next(request)

        if (response.headers.get("content-type", "").startswith("application/json") and 
            not request.url.path.startswith("/api/v1/openapi")):
            try:
                
                if hasattr(response, 'body_iterator'):
                    # For streaming responses like JSONResponse
                    response_body = [section async for section in response.body_iterator]
                    response_data = b"".join(response_body).decode()

                elif hasattr(response, 'body') and callable(response.body):
                    body = await response.body()
                    response_data = body.decode()

                else:
                    return response
                
                if response_data:
                    data = json.loads(response_data)
                    camel_case_data = convert_keys_to_camel_case(data)
                    
                    new_content = json.dumps(camel_case_data)
                    
                    new_headers = dict(response.headers)
                    if 'content-length' in new_headers:
                        del new_headers['content-length']
                    if 'Content-Length' in new_headers:
                        del new_headers['Content-Length']
                    
                    new_response = Response(
                        content=new_content,
                        status_code=response.status_code,
                        media_type="application/json",
                        headers=new_headers
                    )
                    return new_response
                
            except (json.JSONDecodeError, UnicodeDecodeError, AttributeError) as e:
                print(f"Case conversion middleware error: {e}")
                return response
            except Exception as e:
                print(f"Unexpected middleware error: {e}")
                return response

        return response