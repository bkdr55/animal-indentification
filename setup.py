from cx_Freeze import setup, Executable

setup(
    name="Sertão Silvestre",
    version="1.0",
    description="Comparador de animais por imagem - Sertão Silvestre by:Collor",
    executables=[Executable("main.py", base="Win32GUI", icon="logo.ico")],
    options={
        "build_exe": {
            "packages": ["tkinter", "cv2", "PIL", "torch", "torchvision", "ultralytics", "numpy"],
            "include_files": ["detector.py", "extractor.py", "myutils.py", "yolov8n.pt", "logo.ico"],
        }
    }
)