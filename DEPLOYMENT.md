## Deployment Instructions (Render)

1. Go to [Render.com](https://render.com)
2. Click “New Web Service” → “From GitHub”
3. Select your repository
4. Configure:
   - Runtime: Python 3.11
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2`
   - Port: 8000
5. Hit deploy 

The service will be accessible via the provided public URL.