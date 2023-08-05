import streamlit as st
import matplotlib.pyplot as plt
import pydot
import openai



def generated_text(query):
    # Your OpenAI API key
    openai.api_key = "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"
                
    # Set the prompt for the presentation
    prompt = '''{} create a product vision statement based on the decription provided'''.format(query)

    # Generate the presentation text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
        presence_penalty=1,
    )

    presentation_text = response.choices[0].text
    return presentation_text.lower()

def main():
    st.title("Generate a  product vision")
    query = st.text_input("Enter the name of the topic:")
    
    if st.button("Generate"):
        presentation_text = generated_text(query)
        st.write(" ")
        st.write("Generate  product vision:")
        st.write(presentation_text)
        
    

if __name__ == "__main__":
    main()