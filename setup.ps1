# PowerShell Setup Script for Friend Recommendation System
# Run this script to automatically set up the project

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Friend Recommendation System - Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "[1/6] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host ""
Write-Host "[2/6] Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host ""
Write-Host "[3/6] Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host ""
Write-Host "[4/6] Installing Python dependencies..." -ForegroundColor Yellow
pip install -q -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

# Create .env file if not exists
Write-Host ""
Write-Host "[5/6] Configuring environment..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
} else {
    Copy-Item ".env.example" ".env"
    Write-Host "✓ .env file created from template" -ForegroundColor Green
    Write-Host "⚠  Please edit .env with your Neo4j password!" -ForegroundColor Yellow
}

# Verify Neo4j connection
Write-Host ""
Write-Host "[6/6] Checking Neo4j connection..." -ForegroundColor Yellow
Write-Host "Please ensure Neo4j is running on bolt://localhost:7687" -ForegroundColor Cyan

# Done
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "✓ Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Make sure Neo4j is running" -ForegroundColor White
Write-Host "2. Edit .env file with your Neo4j password" -ForegroundColor White
Write-Host "3. Run: python app.py" -ForegroundColor White
Write-Host "4. Open: http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "To start the application now, type: python app.py" -ForegroundColor Yellow
Write-Host ""
