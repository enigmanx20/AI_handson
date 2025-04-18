# AI hands-on: Real-Time Segmentation Overlay

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
- ASAP version 1.9.0 (virtual slide viewer)

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

3. Install [ASAP](https://github.com/computationalpathologygroup/ASAP/releases/download/1.9/ASAP-1.9-win64.exe) (Automated Slide Analysis Platform).

4. Install Python 3.8+ and required dependencies:

   ```bash
   pip install -r ./AI_handson/requirements.txt
   ```

5. Change the directory and launch the Jupyter notebook:
    ```bash
   cd ./AI_handson
   ```
   ```bash
   jupyter notebook
   ```

7. Open `main.ipynb` and update the `slide_name` variable to match your slide file name:
 
    ```python
    slide_name = "your_slide_name.svs"
    ```

8. Open the corresponding slide with ASAP.

9. Run the notebook cells sequentially. A window will pop up displaying the live segmentation overlay on the screen.

---

## Model Requirements

- The segmentation model must output a tensor of shape `[batch_size, 6, H, W]`, where 6 is the number of classes.
- Ensure the output channels correspond to the class indices (0–5).

---

## 🎨 Class Color Map

| Class                  | Color  | Preview |
|:----------------------:|:------:|:--------|
| White background       | Black  | ⚫ |
| Tissue / Stroma        | White  | ⚪ |
| Normal epithelium      | Green  | 🟢 |
| Gleason pattern 3      | Blue   | 🔵 |
| Gleason pattern 4      | Orange | 🔶 |
| Gleason pattern 5      | Red    | 🔴 |

---

## Example Demo Movie
![Demo Video](./prostate_demo_4x.gif)

---

## License
Codes: the MIT License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Model: CC BY-SA-NC 4.0 [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Notes

- Only **Windows OS** is supported (due to `win32gui` and native DC capture).
- The segmentation overlay is blended with 50% transparency over the background.
- You can modify the color map and other hyperparameters inside the notebook.
- Tune the magnification or change mpp parameters to maximize the performance. The model is trained around 0.39 mpp (microns per pixel).

---

# Citation
If you use this work, SegPanda dataset, and models, please cite the following paper:
```bibtex
@InProceedings{10.1007/978-3-031-44917-8_25,
  author    = {Kawai, Masakata and Ota, Noriaki and Yamaoka, Shinsuke},
  editor    = {Xue, Zhiyun and Antani, Sameer and Zamzmi, Ghada and Yang, Feng and Rajaraman, Sivaramakrishnan and Huang, Sharon Xiaolei and Linguraru, Marius George and Liang, Zhaohui},
  title     = {Large-Scale Pretraining on Pathological Images for Fine-Tuning of Small Pathological Benchmarks},
  booktitle = {Medical Image Learning with Limited and Noisy Data},
  year      = {2023},
  publisher = {Springer Nature Switzerland},
  address   = {Cham},
  pages     = {257--267},
  isbn      = {978-3-031-44917-8}
}
```
