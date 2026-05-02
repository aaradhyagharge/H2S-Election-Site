# MATDAN — One-Click Setup & Run
Write-Host "🇮🇳 Initializing Operation Matdan..." -ForegroundColor Saffron

# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python not found! Please install Python and try again."
    exit
}

# Install requirements
Write-Host "📦 Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# Start Server
Write-Host "🚀 Launching Server at http://localhost:5000" -ForegroundColor Cyan
python app.py
