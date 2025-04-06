# AI Gun Detection

A weapon detection system using computer vision and deep learning to enhance security surveillance in public spaces.

## 👥 Team
- Lauri Soome
- Maria Sandu
- Adam Young

## 🔍 Problem Statement

Growing concerns around public safety in crowded areas (schools, malls, airports, etc.) necessitate the development of smart surveillance systems. Traditional security systems:

- Rely heavily on human monitoring, which is often slow, error-prone, and reactive
- Lack the intelligence to detect weapons in real-time, resulting in delayed response times and increased casualties
- Timely detection of firearms and potential shooters can save lives!

An AI security system can be a safer alternative to traditional security systems if developed with caution.

## 📊 Dataset

### Mock Attack Dataset
- Manually annotated dataset from a mock attack at a University
- Three surveillance cameras covering two corridors and one entrance
- Total Dataset: 5,149 annotated frames across three camera perspectives
- Dataset after processing: ~1500 images with a firearm (handgun, short rifle) or a knife, ~1500 images with no weapons. Total dataset => ~3k images

| Camera | Location | Features | Duration | Annotated Frames |
|--------|----------|----------|----------|------------------|
| Cam1 | Corridor 1 | Uniform lighting, doors, bins | 5m 4s of movement | 607 frames (2 FPS) |
| Cam7 | Corridor 2 | Similar to Cam1 but more objects (fire extinguisher, wall items) | 29m 16s of movement | 3,511 frames (2 FPS) |
| Cam5 | Module entrance | Black carpet, irregular lighting with rays | 8m 36s of movement | 1,031 frames (2 FPS) |

[1] *Reference: Salazar González et al., "Real-time gun detection in CCTV: An open problem," Neural Networks, 2020.*

## 🧠 Model

### Weapon Detection Model Architecture
- **YOLO v11n**: Smallest variant of the latest YOLO model through Ultralytics

### Training Configuration
- **Dataset**: 3-class weapon detection (Handgun, Knife, Short rifle)
- **Image Size**: 320×320 pixels
- **Training Strategy**:
  - 50 epochs with early stopping (patience=10)
  - Batch size: 64
  - Optimizer: AdamW
  - GPU-accelerated training

## 📈 Results

- We used fiftyone to interpret the test results images to understand model performance
- Performance metrics chart include precision-recall curves and confidence distribution by class

## 🔮 Future Improvements

- Larger Models: YOLO 11s, YOLO 11m, YOLO 11l, YOLO 11x
- Further refinement to minimize false positives and false negatives
- Introduce a human-in-the-loop: Gun detected -> Send to human review
- Focus on improving real-time detection to reduce response times

## 📚 References

[1] Salazar González, J. L., Zaccaro, C., Álvarez-García, J. A., Soria-Morillo, L. M., & Sancho Caparrini, F. (2020). Real-time gun detection in CCTV: An open problem. *Neural Networks*. https://doi.org/10.1016/j.neunet.2020.09.013
