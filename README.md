# Pediatric Eye Disease Detector

Initial project setup for developing a deep learning system to detect pediatric eye disorders from medical images in DICOM format.

---

## About the Project (INITIAL PROJECT OVERLAY)

This project aims to build a diagnostic support tool that uses deep learning to analyze pediatric ophthalmic images such as:

- Fundus photographs  
- OCT scans  
- Slit-lamp images  

The goal is early detection of eye diseases in children to assist ophthalmologists and improve screening in resource-limited settings.

---

## Target Diseases

The system is planned to focus on the following pediatric ocular conditions:

- Retinopathy of Prematurity (ROP)  
- Congenital Cataract  
- Pediatric Glaucoma  
- Retinoblastoma  
- Coats Disease  
- Strabismus related abnormalities  
- Refractive error indications

---

## Planned Methodology

1. Read and preprocess DICOM images  
2. Image normalization and resizing  
3. Train deep learning models (CNN / Transformer)  
4. Combine image features with metadata  
   - age  
   - gender  
   - eye laterality  
5. Explain model decisions using Grad-CAM  
6. Evaluate using medical metrics  
   - accuracy  
   - sensitivity  
   - specificity  
   - AUC score

---

## Data Management Plan

Proposed project structure:

pediatric-eye-disease-detector/
│
├── data/          # DICOM images and labels  
├── src/           # model and scripts  
├── notebooks/     # experiments  
├── docs/          # articles and notes  
└── README.md

- All images will follow DICOM standard  
- Labels will be stored separately  
- Metadata will be mapped using patient ID  
- No personal identifiers will be stored

---

## Articles Used and Inspiration

This project is guided by research works on:

- AI based early detection of pediatric eye diseases  
- Deep learning screening using ocular images  
- Explainable AI in ophthalmology  
- Clinical evaluation of medical AI systems  

Major reference:

- JAMA Network Open article on AI for early detection of pediatric eye diseases  
- Related IEEE and ophthalmology deep learning studies  
- DICOM medical imaging guidelines

(Detailed citations will be added later)

---

## Tools and Technologies

- Python  
- PyTorch / TensorFlow  
- pydicom  
- OpenCV  
- NumPy, Pandas  
- Grad-CAM  
- Jupyter Notebook

---

## Current Status

- [ ] Literature study  
- [ ] Dataset preparation  
- [ ] DICOM loader implementation  
- [ ] Baseline model  
- [ ] Explainability module  
- [ ] Documentation

---

## Notes

This is an initial README and will be updated with:

- Dataset details  
- Model architecture  
- Results  
- Usage instructions  
- Screenshots

---
