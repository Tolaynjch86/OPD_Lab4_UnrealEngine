# Connects the team's Git hooks. Run once after git clone, from the repository root:
#   powershell -ExecutionPolicy Bypass -File setup.ps1

git config core.hooksPath .githooks
git config core.quotePath false
Write-Host "core.hooksPath =" (git config --get core.hooksPath)
