param()

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pytest

Write-Host "Virtual environment created and pytest installed. Activate with: .\\.venv\\Scripts\\Activate.ps1"
