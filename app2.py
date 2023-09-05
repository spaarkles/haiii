import streamlit as st
import webbrowser

st.set_page_config(page_title="for my onlie", page_icon=":smiling_face_with_3_hearts:", layout="centered")


#DONT TOUCH ASTRA VIDEO
url="https://youtu.be/2XbGKi5Bq4Y?si=iiOaL8BvNISFg6BE&t=16"


url2="https://youtu.be/o0tqEQ331go?si=AnL9ykeIgY_CvWBa"







# header section
with st.container():    
    st.subheader("------------------------------------------")
    st.title("Haiii i wub u<3<3<3<3")
    st.write("""Omg I love you so much I made a website for you ?!?!?!! HELLO EVEN
             I DO EVERYTHING IN THIS LIFE FOR U""")
    
    


# what it do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
    
        with st.container():
            Image="https://image.peco-japan.com/images/357747.gif"
        st.image(Image, caption='is this us')

        Image2="https://media.tenor.com/TkOr09bhVHEAAAAd/cat-fight.gif"
        st.image(Image2, caption='or is this us')

            
    with right_column:
            st.header("I LOVE ONLIE")
            st.header("things you can improve on")
            st.write("""
                    - niceness
                    - being nice
                    - your kindness

                    """
                     )
            

            with st.container():
                 st.slider('how much do u love me heh')
                 st.radio('do you', ['wub me:3', 'hate me>:('])

            if st.button('Click if you love me'):
                webbrowser.open_new(url)
            if st.button('Click if you HATE ME'):
                 webbrowser.open_new(url2)
                
                # Add content to the footer container

footer_container=st.container()

with footer_container:
    col1, col2, col3= st.columns((2,1,1))
    st.subheader("------------------------------------------")
   
   