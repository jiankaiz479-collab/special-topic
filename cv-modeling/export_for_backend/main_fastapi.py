# 這是您 VTON 服務的 API 核心檔案

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# 創建 FastAPI 應用程式實例
# 我們將應用程式命名為 'app'，以便 Uvicorn 找到它
app = FastAPI(title="VTON Model Service API")

# 根路由：用於快速測試服務是否啟動
@app.get("/")
def read_root():
    """根路由：確認服務是否啟動"""
    # 這是您在瀏覽器輸入 http://127.0.0.1:8000/ 時會看到的內容
    return {"message": "VTON Model Service is Running Successfully"}

# 這是您的第一個功能路由： /api/segment (去背功能，之後會加入 Rembg 邏輯)
@app.post("/api/segment")
async def segment_cloth_placeholder():
    """去背功能佔位符：等待加入圖片處理邏輯"""
    return JSONResponse(
        content={"status": "ready", "service": "Segmentation endpoint is active"},
        status_code=200
    )