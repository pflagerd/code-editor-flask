from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import subprocess
import tempfile

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Template rendering setup
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/run")
async def run_code(request: Request):
    try:
        data = await request.json()
        code = data.get("code")

        if not code:
            raise HTTPException(status_code=400, detail="No code provided.")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
            temp.write(code.encode("utf-8"))
            temp.flush()
            temp_file_name = temp.name

        try:
            process = subprocess.Popen(
                ["python3", "-u", temp_file_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            stdout, stderr = process.communicate()

            output = stdout.decode("utf-8") + stderr.decode("utf-8")
            return JSONResponse(content={"output": output, "returncode": process.returncode})

        finally:
            os.unlink(temp_file_name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app using a command like: uvicorn filename:app --reload
