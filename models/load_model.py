import joblib

def load_saved_model():
    model = joblib.load('models/intrusion_detection_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    label_encoder = joblib.load('models/label_encoder.pkl')
    return model, scaler, label_encoder

if __name__ == "__main__":
    load_saved_model()
