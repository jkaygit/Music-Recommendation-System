import streamlit as st
import pickle
import requests
import pandas as pd
import Recommenders as Recommenders



st.title('Music Recommendation System')
music_list = pickle.load(open('music_list.pkl','rb'))
music = pd.DataFrame(music_list)
selected_music = st.selectbox("Select song from Dropdown",music['song'].values)

ir = Recommenders.item_similarity_recommender_py()
ir.create(music, 'user_id', 'song')
user_items = ir.get_user_items(music['user_id'][1000])

if st.button('Recommend'):
    Recommendation = ir.get_similar_items(['The Cove - Jack Johnson', 'The End - Pearl Jam'])
    st.write(Recommendation)

pr = Recommenders.popularity_recommender_py()
pr.create(music, 'user_id', 'song')
if st.button("Get Popular Songs"):
    pop_recommendation = pr.recommend(music['user_id'][5])
    st.write(pop_recommendation)