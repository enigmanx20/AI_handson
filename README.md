# AI_handson  
**Realtime Prostate Cancer Segmentation Demo**

---

# Real-Time Segmentation Overlay System

This project captures a specific window on your screen, runs a PyTorch-based segmentation model on it, colorizes the segmentation output based on class labels, and overlays the results onto the live view in real-time.

The GUI is built using **Tkinter**, and **PyTorch** is used for the deep learning inference.

---

## Features

- 🖼️ Real-time background screenshot capturing
- 🧖️ On-the-fly deep learning inference (PyTorch 1.8.2)
- 🎨 Segmentation output colorized by class
- 🪟 Windows-native GUI with Tkinter and Win32 API
- ⚡ Fast inference with mixed precision (`torch.cuda.amp.autocast`)

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**Python Version:**  
- Python 3.8 or newer is recommended.

**Main Libraries:**
- `torch==1.8.2`
- `torchvision==0.9.2`
- `Pillow`
- `pywin32`
- `tkinter` (comes with standard Python installation)

---

## Files

| File                  | Description                                              |
|------------------------|----------------------------------------------------------|
| `main.ipynb`           | Main Jupyter notebook to run the GUI and segmentation overlay |
| `CaptureWindow.py`     | Utility functions to capture Windows screen contents     |
| `requirements.txt`     | Python dependency list                                   |
| `README.md`            | This documentation file                                  |

---

## How to Run

1. Clone the Git repository:

   ```bash
   git clone https://github.com/enigmanx20/AI_handson.git ./
   ```

2. Download the pretrained model from [Google Drive](https://drive.google.com/file/d/1VzFcX_DdhEQvzT-MTsCJy_IgSU752I0u/view?usp=drive_link), then move it into the `AI_handson` directory:

   ```bash
   mv Last_segPANDA200_DeepLabv3_1000itr.pt ./AI_handson
   ```

3. Install [ASAP](https://computationalpathologygroup.github.io/ASAP/) (Automated Slide Analysis Platform).

4. Install Python 3.8+ and required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch the Jupyter notebook:

   ```bash
   jupyter notebook
   ```

6. Open `main.ipynb` and update the `slide_name` variable to match your slide file name:

   ```python
   slide_name = "your_slide_name.svs"
   ```

7. Open the corresponding slide with ASAP.

8. Run the notebook cells sequentially. A window will pop up displaying the live segmentation overlay on the screen.

---

## Model Requirements

- The segmentation model must output a tensor of shape `[batch_size, 6, H, W]`, where 6 is the number of classes.
- Ensure the output channels correspond to the class indices (0–5).

---

## Class Color Map 🎨

| Class | Color  | Preview |
|:-----:|:------:|:--------|
| 0     | Black  | ⚫ |
| 1     | White  | ⚪ |
| 2     | Green  | 🟢 |
| 3     | Blue   | 🔵 |
| 4     | Orange | 🔶 |
| 5     | Red    | 🔴 |

---

## Example (Before/After)

| Original Screenshot          | Segmentation Overlay         |
|:-----------------------------:|:-----------------------------:|
| ![original](./example_original.png) | ![overlay](./example_overlay.png) |

*(You can create these example images after running the system.)*

---

## License

**CC BY-NC-SA 4.0**  
(*Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License*)

---

## Notes

- Only **Windows OS** is supported (due to `win32gui` and native DC capture).
- The segmentation overlay is blended with 50% transparency over the background.
- You can modify the color map and other hyperparameters inside the notebook.

---

# 🎯 Quick Preview

> **Live capture → Deep learning → Colorize → Display** — everything happening seamlessly!
