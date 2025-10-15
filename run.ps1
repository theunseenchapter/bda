# Quick Start Script - Runs the Flask application
# Make sure you've run setup.ps1 first!

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Friend Recommendation System" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
} else {
    Write-Host "Virtual environment not found. Run setup.ps1 first!" -ForegroundColor Red
    exit 1
}

# Check if Neo4j is accessible
Write-Host "Checking Neo4j connection..." -ForegroundColor Yellow
Write-Host ""

# Start Flask app
Write-Host "Starting Flask application..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Access the application at:" -ForegroundColor Green
Write-Host "http://localhost:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Neo4j Browser (if needed):" -ForegroundColor Green
Write-Host "http://localhost:7474" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor White
Write-Host ""

python app.py
