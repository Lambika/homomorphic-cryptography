# Fully Homomorphic Encryption for Sensitive Medical Data Processing

A comprehensive exploration of Fully Homomorphic Encryption (FHE) applied to sensitive medical data, developed during a 4-month internship at CETIC (Centre d'Excellence en Technologies de l'Information et de la Communication).

---

## 🎯 Project Overview

This project demonstrates practical applications of homomorphic encryption in healthcare, ensuring data privacy by enabling computations directly on encrypted data without decryption. Three distinct use cases illustrate the potential of FHE in real-world scenarios.

---

## Key Features

- ✅ Privacy-preserving medical data analysis  
- ✅ Audio processing on encrypted signals  
- ✅ Federated learning with homomorphic encryption  
- ✅ Client-server architecture with Flask microservices  
- ✅ GDPR-compliant data handling  

---

## 🏗️ Architecture

- **Client:** Encrypts data locally and decrypts results  
- **Server:** Performs computations on encrypted data without access to plaintext  
- **Communication:** Secure data exchange via Flask microservices  

---

## 📊 Use Cases

### 1. Medical Database Pseudonymization  
- **Objective:** Analyze medical records while preserving patient privacy  
- **Dataset:** Medical MNIST with clinical variables (fever, cough, chest pain, etc.)  
- **Operations:** Statistical calculations, disease index computation, threshold comparisons  
- **Technology:** CKKS scheme for approximate real number computations  

### 2. Encrypted Audio Processing  
- **Objective:** Process audio files without accessing their content  
- **Features:**  
  - Silence detection using polynomial approximation  
  - Audio similarity comparison using Wav2Vec2 embeddings  
  - Euclidean distance and cosine correlation on encrypted vectors  
- **Technology:** CKKS scheme with signal processing optimizations  

### 3. Secure Federated Learning  
- **Objective:** Train CNN models across multiple hospitals without sharing raw data  
- **Dataset:** Medical images from two simulated hospitals  
- **Process:** Local training → Homomorphic aggregation → Distributed updated model  
- **Results:** 93.8% accuracy improvement through secure collaboration  
- **Technology:** CKKS scheme with PyTorch integration  

---

## 🛠️ Technologies Used

- **Primary Language:** Python 3.8+  
- **FHE Library:** TenSEAL (Microsoft SEAL wrapper)  
- **ML Framework:** PyTorch  
- **Audio Processing:** Librosa, Wav2Vec2 (Facebook AI)  
- **Web Framework:** Flask  
- **Development Tools:** Jupyter Notebooks, VS Code  
- **Version Control:** Git/GitHub  

---

## 🚀 Installation

### Prerequisites

- Python >= 3.8  
- pip >= 21.0  
