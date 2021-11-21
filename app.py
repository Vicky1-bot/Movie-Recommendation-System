import pickle
import streamlit as st
import pandas 
import numpy 
def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].Title)

    return recommended_movie_names

page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
  background-size: cover;
    background-repeat: no-repeat;
    background-position: absolute;
    background-attachment: fixed;
    background-color: #4f8bf9;
    title color: #fff;
    
       

  
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

new_title = '<p style="font-family:sans-serif; color:white; font-size: 40px;">MOVIE RECOMMENDATION SYSTEM</p>'
st.markdown(new_title, unsafe_allow_html=True)
#st.markdown(, unsafe_allow_html=True)
movies = pickle.load(open('movie_list1.pkl','rb'))
similarity = pickle.load(open('similarity1.pkl','rb'))

movie_list = movies['Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.subheader(i)
        
