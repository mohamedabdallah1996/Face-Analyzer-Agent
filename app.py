from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
from tempfile import NamedTemporaryFile

from constants import SYSTEM_PROMPT, INSTRUCTIONS
from utils import resize_image_for_display

import streamlit as st
import os

os.environ['TAVILY_API_KEY'] = st.secrets['TAVILY_API_KEY']
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']


@st.cache_resource
def get_agent():
    """
    Initialize the agent with the Gemini model and Tavily tools.
    """
    return Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[TavilyTools()],
        markdown=True,
        system_prompt=SYSTEM_PROMPT,
        instructions=INSTRUCTIONS
    )

def analyze_image(image_path, agent):
    """
    Analyze the image using the agent.
    """
    with st.spinner("Analyzing image..."):
        response = agent.run(
            "قم بتحليل الصورة التالية وتقديم وصف شامل بناءً على الإشارات البصرية",
            images=[image_path]
        )
        st.markdown(response.content)

def save_uploaded_file(uploaded_file):
    """
    Save the uploaded file to a temporary location.
    """
    with NamedTemporaryFile(dir='.', suffix='.jpg', delete=False) as f:
        f.write(uploaded_file.getbuffer())
        return f.name


def main():
    st.title("😉 Face Analyzer APP")
    
    if 'selected_example' not in st.session_state:
        st.session_state.selected_example = None
    if 'analyze_clicked' not in st.session_state:
        st.session_state.analyze_clicked = False
    
    tab_examples, tab_upload, tab_camera = st.tabs([
        "📚 Example Faces", 
        "📤 Upload Image", 
        "📸 Take Photo"
    ])

    with tab_examples:
        example_faces = {
            "Man Face": "images/man_1.jpg",
            "Woman Face": "images/woman_covered_face.jpg",
            "Fake Human Face": "images/fake_human_1.jpg",
            "Aniaml Face": "images/gorilla.jpg",
        }

        cols = st.columns(4)
        for i, (name, image_path) in enumerate(example_faces.items()):
            with cols[i]:
                if st.button(name, use_container_width=True):
                    st.session_state.selected_example = image_path
                    st.session_state.analyze_clicked = False

        if st.session_state.selected_example:
            st.divider()
            st.subheader("Selected Example")
            image_path = st.session_state.selected_example
            resized_image = resize_image_for_display(image_path)

            st.image(resized_image, caption="Selected Example", use_container_width=False)
            if st.button("🔍 Analyze", key="analyze_example") and not st.session_state.analyze_clicked:
                analyze_image(image_path, get_agent())
                st.session_state.analyze_clicked = True            


    with tab_upload:
        uploaded_file = st.file_uploader(
            "Upload an image", 
            type=["jpg", "jpeg", "png"], 
            label_visibility="collapsed",
            help="Upload a clear image of human face",
        )

        if uploaded_file:
            resized_image = resize_image_for_display(uploaded_file)
            st.image(resized_image, caption="Uploaded Image", use_container_width=False)
            if st.button("🔍 Analyze", key="analyze_upload"):
                temp_file = save_uploaded_file(uploaded_file)
                analyze_image(temp_file, get_agent())
                os.unlink(temp_file)

    with tab_camera:
        camera_photo = st.camera_input("Take a picture of any person")
        if camera_photo:
            resized_image = resize_image_for_display(camera_photo)
            st.image(resized_image, caption="Camera Image", use_container_width=False)
            if st.button("🔍 Analyze", key="analyze_camera"):
                temp_path = save_uploaded_file(camera_photo)
                analyze_image(temp_path, get_agent())
                os.unlink(temp_path) 
        

if __name__ == "__main__":
    st.set_page_config(
        page_title="Face Analyzer Agent",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main()