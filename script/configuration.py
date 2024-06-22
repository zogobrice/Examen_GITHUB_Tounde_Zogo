import os

# Répertoires des données
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
VAL_DIR = os.path.join(DATA_DIR, 'val')
TEST_DIR = os.path.join(DATA_DIR, 'test')

IMAGE_SIZE = (229, 229)
BATCH_SIZE = 32

EPOCHS = 15
LEARNING_RATE = 0.001

# Chemin pour sauvegarder le modèle
MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'model', 'model_final.h5')


EMAIL_SMTP_SERVER = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USERNAME = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'  # Utiliser GitHub Secrets pour sécuriser cette information
EMAIL_RECIPIENTS = ['recipient1@example.com', 'recipient2@example.com']

# Autres configurations pertinentes
RANDOM_SEED = 42
