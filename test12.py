import streamlit as st
from streamlit_oauth import OAuth2Component
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

# Replace with your Google OAuth credentials
CLIENT_ID = "374950109431-6l90208qmjnkmjh7ivhg74tdagk6oe88.apps.googleusercontent.com"
CLIENT_SECRET = "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"
AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REFRESH_TOKEN_URL = "https://oauth2.googleapis.com/token"
REVOKE_TOKEN_URL = "https://oauth2.googleapis.com/revoke"
REDIRECT_URI = "http://localhost:8501/component/streamlit_oauth.authorize_button/index.html"
SCOPE = "openid email profile"

# --- OAuth setup ---
oauth2 = OAuth2Component(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    authorize_endpoint=AUTHORIZE_URL,
    token_endpoint=TOKEN_URL,
    refresh_token_endpoint=REFRESH_TOKEN_URL,
    revoke_token_endpoint=REVOKE_TOKEN_URL,
)

# --- Auth gate ---
if "token" not in st.session_state:
    result = oauth2.authorize_button(name="Login with Google", redirect_uri=REDIRECT_URI, scope=SCOPE, key="google_oauth")
    if result:
        st.session_state.token = result
        st.experimental_rerun()
    st.stop()

st.write("Logged in! ✅")
st.json(st.session_state.token)
