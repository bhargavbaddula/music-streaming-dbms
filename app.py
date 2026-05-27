import streamlit as st
import sqlite3
import pandas as pd
conn = sqlite3.connect("music.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    song_id INTEGER PRIMARY KEY,
    song_name TEXT,
    artist TEXT,
    genre TEXT,
    duration INTEGER
)
""")
conn.commit()
st.title("🎵 Music Streaming DBMS")
menu = ["Add Song", "View Songs"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Add Song":
    st.subheader("➕ Add New Song")
    song_name = st.text_input("Song Name")
    artist = st.text_input("Artist")
    genre = st.text_input("Genre")
    duration = st.number_input("Duration (minutes)")
    if st.button("Add Song"):
        cursor.execute("""
        INSERT INTO songs
        (song_name, artist, genre, duration)

        VALUES (?, ?, ?, ?)
        """, (
            song_name,
            artist,
            genre,
            duration
        ))
        conn.commit()
        st.success("Song Added Successfully 🎉")
elif choice == "View Songs":
    st.subheader("🎶 All Songs")
    cursor.execute("SELECT * FROM songs")
    rows = cursor.fetchall()
    df = pd.DataFrame(
        rows,
        columns=[
            "Song ID",
            "Song Name",
            "Artist",
            "Genre",
            "Duration"
        ]
    )
    st.dataframe(df)
conn.close()
