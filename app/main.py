from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from app.chatgpt_client import ChatGPTClient
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Initialize ChatGPT client
try:
    chatgpt = ChatGPTClient()
except ValueError as e:
    print(f"Warning: {e}")
    chatgpt = None

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "value": None}
    )

@app.post("/", response_class=HTMLResponse)
def index_post(request: Request, user_input: str = Form(...)):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "value": user_input
        }
    )

@app.get("/options", response_class=HTMLResponse)
def options_page(request: Request):
    return templates.TemplateResponse(
        "options.html",
        {"request": request}
    )

@app.get("/first", response_class=HTMLResponse)
def first_page(request: Request):
    return templates.TemplateResponse(
        "first.html",
        {"request": request, "prompt": None, "output": None}
    )

@app.post("/first/stream")
async def first_page_stream(request: Request, prompt: str = Form(...)):
    if not chatgpt or not prompt.strip():
        return StreamingResponse(iter(["Error: No API client or empty prompt"]), media_type="text/plain")

    def generate():
        try:
            for chunk in chatgpt.chat_completion_stream(prompt):
                yield chunk
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/clarity", response_class=HTMLResponse)
def clarity_page(request: Request):
    return templates.TemplateResponse(
        "clarity.html",
        {"request": request, "prompt": None, "output": None}
    )

@app.post("/clarity/stream")
async def clarity_page_stream(request: Request, prompt: str = Form(...)):
    if not chatgpt or not prompt.strip():
        return StreamingResponse(iter(["Error: No API client or empty prompt"]), media_type="text/plain")

    def generate():
        try:
            for chunk in chatgpt.chat_completion_stream(prompt):
                yield chunk
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/format", response_class=HTMLResponse)
def format_page(request: Request):
    return templates.TemplateResponse(
        "format.html",
        {"request": request, "prompt": None, "output": None}
    )

@app.post("/format/stream")
async def format_page_stream(request: Request, prompt: str = Form(...)):
    if not chatgpt or not prompt.strip():
        return StreamingResponse(iter(["Error: No API client or empty prompt"]), media_type="text/plain")

    def generate():
        try:
            for chunk in chatgpt.chat_completion_stream(prompt):
                yield chunk
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/direction", response_class=HTMLResponse)
def direction_page(request: Request):
    return templates.TemplateResponse(
        "direction.html",
        {"request": request, "prompt": None, "output": None}
    )

@app.post("/direction/stream")
async def direction_page_stream(request: Request, prompt: str = Form(...)):
    if not chatgpt or not prompt.strip():
        return StreamingResponse(iter(["Error: No API client or empty prompt"]), media_type="text/plain")

    def generate():
        try:
            for chunk in chatgpt.chat_completion_stream(prompt):
                yield chunk
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/examples", response_class=HTMLResponse)
def examples_page(request: Request):
    return templates.TemplateResponse(
        "examples.html",
        {"request": request, "prompt": None, "output": None}
    )

@app.get("/labor", response_class=HTMLResponse)
def labor_page(request: Request):
    return templates.TemplateResponse(
        "labor.html",
        {"request": request, "prompt": None, "output": None}
    )

@app.post("/labor/stream")
async def labor_page_stream(request: Request, prompt: str = Form(...)):
    if not chatgpt or not prompt.strip():
        return StreamingResponse(iter(["Error: No API client or empty prompt"]), media_type="text/plain")

    def generate():
        try:
            for chunk in chatgpt.chat_completion_stream(prompt):
                yield chunk
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/end", response_class=HTMLResponse)
def end_page(request: Request):
    return templates.TemplateResponse(
        "end.html",
        {"request": request}
    )
