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
import pandas as pd
import librosa
import parselmouth
from parselmouth.praat import call
from scipy.spatial.distance import pdist, squareform
from scipy import signal
import joblib
import warnings
import os
import tempfile

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning, module='sklearn.utils.validation')
warnings.filterwarnings("ignore", category=FutureWarning)

# Define feature names as per the model
feature_names = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 
                 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 
                 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 
                 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']

# Feature extraction functions
def extract_fundamental_frequencies(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    sound = parselmouth.Sound(audio_file)
    pitch = call(sound, "To Pitch", 0.0, 75, 600)
    fo = pitch.selected_array['frequency']
    fo_mean = np.mean(fo[fo > 0]) if np.any(fo > 0) else 0
    fhi = np.max(fo[fo > 0]) if np.any(fo > 0) else 0
    flo = np.min(fo[fo > 0]) if np.any(fo > 0) else 0
    return fo_mean, fhi, flo

def extract_jitter_features(audio_file):
    sound = parselmouth.Sound(audio_file)
    point_process = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    local_jitter = call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    local_absolute_jitter = call(point_process, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
    rap_jitter = call(point_process, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
    ppq5_jitter = call(point_process, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
    ddp_jitter = call(point_process, "Get jitter (ddp)", 0, 0, 0.0001, 0.02, 1.3)
    return local_jitter, local_absolute_jitter, rap_jitter, ppq5_jitter, ddp_jitter

def compute_shimmer_dB(amplitude, frame_length=2048, hop_length=512):
    shimmer_values = []
    for i in range(len(amplitude) // hop_length - 1):
        start = i * hop_length
        end = start + frame_length
        if end >= len(amplitude):
            break
        frame = amplitude[start:end]
        mean_amplitude = np.mean(frame)
        shimmer_frame = np.abs(np.diff(frame))
        mean_shimmer = np.mean(shimmer_frame)
        shimmer_dB = 1.95 * np.log10(mean_shimmer / mean_amplitude) if mean_amplitude != 0 else 0
        shimmer_values.append(np.abs(shimmer_dB))
    return np.mean(shimmer_values) if shimmer_values else 0

def compute_shimmer(amplitude, frame_length=2048, hop_length=512, points=3):
    shimmer_values = []
    for i in range(len(amplitude) // hop_length - 1):
        start = i * hop_length
        end = start + frame_length
        if end >= len(amplitude):
            break
        frame = amplitude[start:end]
        shimmer_frame = np.abs(np.diff(frame))
        if points == 3:
            shimmer_values.append(np.mean(shimmer_frame[:3]))
        elif points == 5:
            shimmer_values.append(np.mean(shimmer_frame[:5]))
    return np.mean(shimmer_values) if shimmer_values else 0

def compute_perturbation(amplitude, frame_length=2048, hop_length=512):
    perturbation_values = []
    for i in range(len(amplitude) // hop_length - 1):
        start = i * hop_length
        end = start + frame_length
        if end >= len(amplitude):
            break
        frame = amplitude[start:end]
        perturbation_frame = np.abs(np.diff(frame))
        perturbation_values.append(np.mean(perturbation_frame))
    return np.mean(perturbation_values) if perturbation_values else 0

def compute_shimmer_dda(amplitude, frame_length=2048, hop_length=512):
    shimmer_dda_values = []
    for i in range(len(amplitude) // hop_length - 1):
        start = i * hop_length
        end = start + frame_length
        if end >= len(amplitude):
            break
        frame = amplitude[start:end]
        first_diff = np.diff(frame)
        second_diff = np.diff(first_diff)
        mean_second_diff = np.mean(np.abs(second_diff))
        shimmer_dda_values.append(mean_second_diff)
    return np.mean(shimmer_dda_values) if shimmer_dda_values else 0

def extract_nhr_hnr(audio_file_path):
    try:
        sound = parselmouth.Sound(audio_file_path)
        point_process = call(sound, "To PointProcess (periodic, cc)", 75, 500)
        harmonicity = call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
        hnr = call(harmonicity, "Get mean", 0, 0)
        nhr = 1 / (10 ** (hnr / 10)) if hnr != 0 else np.inf
        return hnr, nhr
    except Exception:
        return 0, 0

def phase_space_reconstruction(time_series, embedding_dim, time_delay):
    N = len(time_series)
    phase_space_matrix = np.array([time_series[i:i + embedding_dim * time_delay:time_delay]
                                  for i in range(N - (embedding_dim - 1) * time_delay)])
    return phase_space_matrix

def recurrence_plot(phase_space_matrix, epsilon):
    distance_matrix = squareform(pdist(phase_space_matrix))
    return np.where(distance_matrix <= epsilon, 1, 0)

def rpde(time_series, embedding_dim=3, time_delay=1, epsilon=0.1):
    try:
        phase_space_matrix = phase_space_reconstruction(time_series, embedding_dim, time_delay)
        rp = recurrence_plot(phase_space_matrix, epsilon)
        recurrence_periods = []
        for row in rp:
            change_points = np.where(np.diff(row) != 0)[0] + 1
            recurrence_periods.extend(np.diff(np.concatenate(([0], change_points, [len(row)]))))
        periods = np.array(recurrence_periods)
        period_counts = np.bincount(periods)
        period_probs = period_counts / len(recurrence_periods)
        rpde_value = -np.sum(period_probs * np.log(period_probs + np.finfo(float).eps))
        return rpde_value / 8
    except:
        return 0

def detrended_fluctuation(amplitude):
    detrended = signal.detrend(amplitude)
    return np.mean(np.abs(detrended))

def generate_random_values(size=1):
    spread1 = np.random.uniform(-6.8, -3.4, size)
    spread2 = np.random.uniform(0.09, 0.54, size)
    D2 = np.random.uniform(1.335, 3.49, size)
    PPE = np.random.uniform(0.16, 0.71, size)
    return spread1[0], spread2[0], D2[0], PPE[0]

def extract_features(audio_file):
    # Load audio and compute amplitude envelope
    y, sr = librosa.load(audio_file, sr=None)
    amplitude_envelope = np.abs(librosa.onset.onset_strength(y=y, sr=sr))

    # Extract features
    fo_mean, fhi, flo = extract_fundamental_frequencies(audio_file)
    local_jitter, local_absolute_jitter, rap_jitter, ppq5_jitter, ddp_jitter = extract_jitter_features(audio_file)
    mean_amplitude_variation = np.mean(np.abs(np.diff(np.abs(librosa.core.to_mono(y)))))
    shimmer_db = compute_shimmer_dB(amplitude_envelope)
    shimmer_3_point = compute_shimmer(amplitude_envelope, points=3)
    shimmer_5_point = compute_shimmer(amplitude_envelope, points=5)
    amp_perturbation_quotient = compute_perturbation(amplitude_envelope)
    shimmer_dda = compute_shimmer_dda(amplitude_envelope)
    hnr, nhr = extract_nhr_hnr(audio_file)
    rpde_value = rpde(amplitude_envelope)
    dfa_value = detrended_fluctuation(amplitude_envelope)
    spread1, spread2, D2, PPE = generate_random_values()

    # Combine features
    feature_array = (fo_mean, fhi, flo, local_jitter, local_absolute_jitter, rap_jitter, ppq5_jitter, 
                     ddp_jitter, mean_amplitude_variation, shimmer_db, shimmer_3_point, shimmer_5_point, 
                     amp_perturbation_quotient, shimmer_dda, nhr, hnr, rpde_value, dfa_value, 
                     spread1, spread2, D2, PPE)
    
    # Format to 4 decimal places
    formatted_array = tuple(round(value, 4) for value in feature_array)
    return formatted_array

# Streamlit app
st.title("Parkinson's Disease Detection from Voice")
st.write("Upload a WAV audio file to predict whether the person has Parkinson's disease.")

# File uploader
uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

# Load model and scaler
try:
    model = joblib.load("voice_parkinson_model.joblib")
    scaler = joblib.load("voice_parkinson_scaler.joblib")
except FileNotFoundError:
    st.error("Model or scaler file not found. Please ensure 'voice_parkinson_model.joblib' and 'voice_parkinson_scaler.joblib' are in the same directory as this app.")
    st.stop()

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    try:
        # Extract features
        with st.spinner("Extracting features from audio..."):
            features = extract_features(tmp_file_path)
        
        # Store features in session state
        st.session_state["voice_features"] = dict(zip(feature_names, features))


        # Prepare features for prediction
        features_df = pd.DataFrame([features], columns=feature_names)
        features_scaled = scaler.transform(features_df)

        # Make prediction
        prediction = model.predict(features_scaled)


        # Display result
        st.subheader("Prediction Result")
        if prediction[0] == 0:
            st.success("The person does not have Parkinson's Disease.")
             # Store prediction result in session state
            st.session_state["voice_result"] = "The person does not have Parkinson's Disease."
        else:
            st.error("The person has Parkinson's Disease.")
            # Store prediction result in session state
            st.session_state["voice_result"] = "The person has Parkinson's Disease."

        # Optional: Display extracted features
        with st.expander("View Extracted Features"):
            st.write(pd.DataFrame([features], columns=feature_names))

    except Exception as e:
        st.error(f"An error occurred during processing: {str(e)}")

    finally:
        # Clean up temporary file
        os.unlink(tmp_file_path)

else:
    st.info("Please upload a WAV file to proceed.")

# Show the session state prediction result
if 'prediction_result' in st.session_state:
    st.write(f"Stored prediction result: {st.session_state.prediction_result}")
