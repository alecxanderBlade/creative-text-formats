import streamlit as st
import openai

openai.api_key = "sk-proj-xdKZMysWGqguoypSwgaET3BlbkFJKP5lNG6fuEjiiMbjeap7"

def level_1_prompting():
  st.header("Level 1: Choose a Genre")
  genre_options = ("Science Fiction", "Fantasy", "Mystery")
  genre = st.radio("Genre:", genre_options)
  prompt = f"Write a short story in the {genre} genre."
  return response.choices[0].text.strip()

def main():
  st.title("Creative Text Generator")
  st.write("This app helps you create different creative text formats through a series of prompts.")

  level_1_text = level_1_prompting()
  st.subheader("Level 1 Output:")
  st.write(level_1_text)

  # Add more levels of prompting functions here...

if __name__ == "__main__":
  main()
