from PIL import Image
import win32gui
import win32ui
import win32con

def get_window_context_and_bitmap(hwnd, width, height):
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    return wDC, dcObj, cDC, dataBitMap

def background_screenshot(dcObj, cDC, dataBitMap, width, height, x=0, y=80):
    cDC.BitBlt((0,0),(width, height) , dcObj, (x,y), win32con.SRCCOPY)
    im = Image.frombuffer('RGB', (width, height), dataBitMap.GetBitmapBits(True), 'raw', 'BGRX', 0, 1)
    return im

def release_DCs(hwnd, wDC, dcObj, cDC, dataBitMap):
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

def background_screenshot_deleteDC(hwnd, width, height):
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(width, height) , dcObj, (0,80), win32con.SRCCOPY)
    #dataBitMap.SaveBitmapFile(cDC, 'screenshot.bmp')
    #bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB', (width, height), bmpstr, 'raw', 'BGRX', 0, 1)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return im