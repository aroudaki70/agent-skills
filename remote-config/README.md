# Remote Development Setup

## Ollama Remote Access

### On the remote server (where Ollama runs):

```powershell
# Windows - Set environment variable
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "User")

# Restart Ollama service
Get-Service Ollama | Restart-Service

# Or restart the app
```

```bash
# Linux/Mac
export OLLAMA_HOST=0.0.0.0:11434
# Then restart ollama service
sudo systemctl restart ollama
```

### From your local machine:

```powershell
# Set remote URL
$env:OLLAMA_BASE_URL = "http://192.168.1.X:11434"

# Or use the Python script
python remote-config/remote_ollama.py --host 192.168.1.X --list
```

---

## VS Code Remote

### Option 1: SSH Remote (for remote servers)

1. Install "Remote - SSH" extension in VS Code
2. Press `F1` → "Remote-SSH: Connect to Host"
3. Enter `user@server-ip`
4. Open the project folder

### Option 2: GitHub Codespaces

1. Install "GitHub Codespaces" extension
2. Press `F1` → "Codespaces: Create New"
3. Select repo and config

### Option 3: Tunnel (ngrok)

```bash
# Tunnel Ollama port
ngrok tcp 11434

# Then connect to the ngrok URL
```

---

## GitHub Remote (already configured)

```powershell
# Push changes
git push origin main

# Pull changes
git pull origin main

# Check status
git status
```

---

## Environment Variables

Create `.env` file in project root:

```env
# Ollama
OLLAMA_BASE_URL=http://localhost:11434
# Or remote: OLLAMA_BASE_URL=http://192.168.1.100:11434

# MiniMax (for video generation)
MINIMAX_API_KEY=your_key_here
MINIMAX_GROUP_ID=your_group_id
```

---

## Testing Connections

```powershell
# Test Ollama
curl http://localhost:11434/api/tags

# Test GitHub
gh auth status

# Test VS Code Remote
# Just connect via SSH or Codespaces
```