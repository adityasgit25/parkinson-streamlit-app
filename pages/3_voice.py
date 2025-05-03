# import streamlit as st
# import numpy as np
# import librosa
# # import praat_parselmouth as parselmouth
# import parselmouth
# from parselmouth.praat import call
# import joblib
# import os
# from scipy import signal

# # Load pre-trained scaler and model
# scaler = joblib.load("voice_parkinson_scaler.joblib")
# model = joblib.load("voice_parkinson_model.joblib")
# # st.write(f"Model type: {type(model)}")

# # Fix: Manually patch missing `n_classes_` if needed
# if not hasattr(model, "n_classes_"):
#     try:
#         model.n_classes_ = len(np.unique(model.classes_))
#     except AttributeError:
#         model.classes_ = np.array([0, 1])
#         model.n_classes_ = 2


# def extract_features(file_path):
#     try:
#         # Load audio
#         y, sr = librosa.load(file_path, sr=None)
#         sound = parselmouth.Sound(file_path)

#         # Pitch features
#         pitch = sound.to_pitch()
#         pitch_values = pitch.selected_array['frequency']
#         pitch_values = pitch_values[pitch_values > 0]  # Filter out unvoiced frames
#         fo = np.mean(pitch_values) if len(pitch_values) > 0 else 0
#         fhi = np.max(pitch_values) if len(pitch_values) > 0 else 0
#         flo = np.min(pitch_values) if len(pitch_values) > 0 else 0

#         # Jitter features
#         point_process = call(sound, "To PointProcess (periodic, cc)", 75, 500)
#         jitter_percent = call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         jitter_abs = call(point_process, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         rap = call(point_process, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         ppq = call(point_process, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         ddp = rap * 3

#         # Shimmer features
#         # shimmer = call(sound, "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         # shimmer_db = call(sound, "Get shimmer (local, dB)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         # apq3 = call(sound, "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         # apq5 = call(sound, "Get shimmer (apq5)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         # dda = apq3 * 3

#         # Shimmer features (MUST pass [sound, point_process])
#         shimmer = call([sound, point_process], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         shimmer_db = call([sound, point_process], "Get shimmer (local, dB)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         apq3 = call([sound, point_process], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         apq5 = call([sound, point_process], "Get shimmer (apq5)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0
#         apq11 = call([sound, point_process], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6) or 0  # <--- add this
#         dda = apq3 * 3

#         # HNR and NHR
#         harmonicity = call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
#         hnr = call(harmonicity, "Get mean", 0, 0) or 0
#         nhr = 1 / (10 ** (hnr / 10)) if hnr != 0 else 0

#         # Nonlinear features
#         rpde = np.mean(librosa.feature.rms(y=y)) if len(y) > 0 else 0
#         dfa = np.mean(np.abs(signal.detrend(y))) if len(y) > 0 else 0
#         spread1 = np.std(pitch_values) * -1 if len(pitch_values) > 0 else 0
#         spread2 = np.std(pitch_values) if len(pitch_values) > 0 else 0
#         d2 = 2.0  # Placeholder
#         ppe = (-np.sum(pitch_values * np.log(pitch_values + np.finfo(float).eps)) 
#                if len(pitch_values) > 0 else 0)

#         return np.array([fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
#                          shimmer, shimmer_db, apq3, apq5, apq11, dda, nhr, hnr,
#                          rpde, dfa, spread1, spread2, d2, ppe]).reshape(1, -1)
#     except Exception as e:
#         st.error(f"Feature extraction error: {e}")
#         return np.zeros((1, 22))

# # def main():
# #     st.title("Parkinson’s Disease Detection from Voice")
# #     uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

# #     if uploaded_file is not None:
# #         file_path = "temp.wav"
# #         with open(file_path, "wb") as f:
# #             f.write(uploaded_file.read())

# #         # Extract features and scale
# #         features = extract_features(file_path)
# #         features_scaled = scaler.transform(features)

# #         # Predict
# #         proba = model.predict_proba(features_scaled)
# #         probability = proba[0][1]
# #         st.write(f"Probability of Parkinson’s: {probability:.2f}")
# #         result = "Positive (Parkinson’s Detected)" if probability > 0.5 else "Negative (No Parkinson’s)"
# #         st.success(result)

# #         # Clean up
# #         if os.path.exists(file_path):
# #             os.remove(file_path)

# def main():
#     st.title("Parkinson’s Disease Detection from Voice")
#     uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

#     if uploaded_file is not None:
#         file_path = "temp.wav"
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.read())

#         # Extract features and scale
#         features = extract_features(file_path)
#         features_scaled = scaler.transform(features)

#         # Ensure model is a classifier and properly loaded
#         if hasattr(model, 'predict_proba'):
#             proba = model.predict_proba(features_scaled)
#             probability = proba[0][1]
#             st.write(f"Probability of Parkinson’s: {probability:.2f}")
#             result = "Positive (Parkinson’s Detected)" if probability > 0.5 else "Negative (No Parkinson’s)"
#             st.success(result)
#         else:
#             st.error("Loaded model does not support predict_proba method. It may not be a classifier.")

#         # Clean up
#         if os.path.exists(file_path):
#             os.remove(file_path)


# if __name__ == "__main__":
#     main()

# import streamlit as st
# import numpy as np
# import librosa
# import parselmouth
# from parselmouth.praat import call
# import joblib
# import os
# from scipy import signal
# import warnings
# import xgboost as xgb

# # Suppress warnings
# warnings.filterwarnings("ignore")

# # Load pre-trained scaler and model
# scaler = joblib.load("voice_parkinson_scaler.joblib")
# model = joblib.load("voice_parkinson_model.joblib")

# def extract_features(file_path):
#     try:
#         # Load audio
#         y, sr = librosa.load(file_path, sr=None)

#         # Normalize audio to match training conditions
#         y = y / np.max(np.abs(y))

#         sound = parselmouth.Sound(file_path)

#         # Pitch features
#         pitch = sound.to_pitch()
#         pitch_values = pitch.selected_array['frequency']
#         pitch_values = pitch_values[pitch_values > 0]  # Filter out unvoiced frames
#         fo = np.mean(pitch_values) if len(pitch_values) > 0 else 0
#         fhi = np.max(pitch_values) if len(pitch_values) > 0 else 0
#         flo = np.min(pitch_values) if len(pitch_values) > 0 else 0

#         # Jitter features
#         point_process = call(sound, "To PointProcess (periodic, cc)", 75, 500)
#         jitter_percent = call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         jitter_abs = call(point_process, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         rap = call(point_process, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         ppq = call(point_process, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3) or 0
#         ddp = rap * 3

#         # Shimmer features - using amplitude-based calculations
#         amplitude_envelope = np.abs(librosa.onset.onset_strength(y=y, sr=sr))
        
#         # Calculate shimmer as mean absolute difference between consecutive amplitude points
#         shimmer = np.mean(np.abs(np.diff(amplitude_envelope))) if len(amplitude_envelope) > 1 else 0
        
#         # Calculate shimmer in dB
#         if len(amplitude_envelope) > 1:
#             shimmer_db = 20 * np.mean(np.abs(np.diff(np.log10(amplitude_envelope + 1e-10))))
#         else:
#             shimmer_db = 0
            
#         # APQ3 - average of 3-point shimmer
#         if len(amplitude_envelope) >= 3:
#             apq3 = np.mean([np.mean(np.abs(np.diff(amplitude_envelope[i:i+3]))) 
#                         for i in range(len(amplitude_envelope)-2)])
#         else:
#             apq3 = 0
            
#         # APQ5 - average of 5-point shimmer
#         if len(amplitude_envelope) >= 5:
#             apq5 = np.mean([np.mean(np.abs(np.diff(amplitude_envelope[i:i+5]))) 
#                         for i in range(len(amplitude_envelope)-4)])
#         else:
#             apq5 = 0
            
#         # APQ11 - average of 11-point shimmer (using all points if less than 11)
#         window_size = min(11, len(amplitude_envelope))
#         if window_size > 1:
#             apq11 = np.mean([np.mean(np.abs(np.diff(amplitude_envelope[i:i+window_size]))) 
#                         for i in range(len(amplitude_envelope)-window_size+1)])
#         else:
#             apq11 = 0
            
#         dda = apq3 * 3

#         # HNR and NHR
#         harmonicity = call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
#         hnr = call(harmonicity, "Get mean", 0, 0) or 0
#         nhr = 1 / (10 ** (hnr / 10)) if hnr != 0 else 0

#         # Nonlinear features
#         rpde = np.mean(librosa.feature.rms(y=y)) if len(y) > 0 else 0
#         dfa = np.mean(np.abs(signal.detrend(y))) if len(y) > 0 else 0
        
#         # Spread features based on pitch statistics
#         if len(pitch_values) > 0:
#             spread1 = np.std(pitch_values) * -1
#             spread2 = np.std(pitch_values)
#         else:
#             spread1 = spread2 = 0
            
#         # Placeholder values for D2 and PPE
#         d2 = 2.0
#         ppe = 0.2  # Placeholder value

#         features = np.array([
#             fo, fhi, flo, 
#             jitter_percent, jitter_abs, rap, ppq, ddp,
#             shimmer, shimmer_db, apq3, apq5, apq11, dda, 
#             nhr, hnr, rpde, dfa, d2, ppe,
#             spread1, spread2
#         ]).reshape(1, -1)
        

#         # Optional: display feature values for debugging
#         st.write("Extracted Features:", features)

#         return features
        
#     except Exception as e:
#         st.error(f"Feature extraction error: {str(e)}")
#         return np.zeros((1, 22))

# def predict_parkinson(model, features):
#     """Handle prediction with proper error handling for XGBoost"""
#     try:
#         # First try direct prediction if predict_proba fails
#         prediction = model.predict(features)
#         return float(prediction[0])  # Return 0 or 1 directly
#     except Exception as e:
#         st.error(f"Prediction error: {str(e)}")
#         return 0.5  # Return neutral probability if prediction fails

# def main():
#     st.title("Parkinson's Disease Detection from Voice")
#     uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

#     if uploaded_file is not None:
#         file_path = "temp.wav"
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         try:
#             # Extract features and scale
#             features = extract_features(file_path)
#             features_scaled = scaler.transform(features)

#             # Get prediction
#             prediction = predict_parkinson(model, features_scaled)
            
#             # Display results
#             if prediction > 0.7:
#                 st.error("Positive (Parkinson's Detected)")
#             else:
#                 st.success("Negative (No Parkinson's)")
                
#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")
#         finally:
#             # Clean up
#             if os.path.exists(file_path):
#                 os.remove(file_path)

# if __name__ == "__main__":
#     main()



import streamlit as st
import numpy as np
import librosa
import joblib
from python_speech_features import mfcc

# Load the pre-trained model and scaler
model = joblib.load("voice_parkinson_model.joblib")
scaler = joblib.load("voice_parkinson_scaler.joblib")

def entropy(signal):
    ps = np.square(signal)
    ps = ps / np.sum(ps)
    return -np.sum(ps * np.log2(ps + 1e-12))

def extract_features(signal, sr):
    zcr = np.mean(librosa.feature.zero_crossing_rate(signal))
    energy = np.mean(np.square(signal))
    entropy_of_energy = entropy(signal)
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=signal, sr=sr))
    spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=signal, sr=sr))

    # Spectral flux based on magnitude spectrogram
    stft = np.abs(librosa.stft(signal))
    spectral_flux = np.mean(np.sqrt(np.sum(np.diff(stft, axis=1)**2, axis=0)))

    # MFCC features
    mfccs = mfcc(signal, sr, numcep=13)
    mfccs_mean = np.mean(mfccs, axis=0)

    features = np.array([
        zcr,
        energy,
        entropy_of_energy,
        spectral_centroid,
        spectral_flux,
        spectral_rolloff,
        *mfccs_mean
    ])

    return features

# Streamlit UI
st.title("🎙️ Parkinson's Disease Detection")
st.write("Upload a `.wav` file of a sustained vowel sound to check for Parkinson's disease.")

uploaded_file = st.file_uploader("Upload your voice (.wav)", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')
    try:
        signal, sr = librosa.load(uploaded_file, sr=None)
        features = extract_features(signal, sr).reshape(1, -1)
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        if prediction == 1:
            st.error("⚠️ The model predicts the person **has** Parkinson's Disease.")
        else:
            st.success("✅ The model predicts the person **does not have** Parkinson's Disease.")
    except Exception as e:
        st.error(f"An error occurred while processing the audio:\n\n{e}")
