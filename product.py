import streamlit as st
import matplotlib.pyplot as plt
import pydot
import openai

def generate_graph(presentation_text):
    graph = pydot.Dot(graph_type='digraph')
    
    # Split the presentation_text into nodes based on newlines
    nodes = presentation_text.split("\n")
    num_nodes = len(nodes)
    
    # Add nodes to the graph
    for i, node_text in enumerate(nodes):
        node_name = f"node_{i}"
        label = node_text.strip()
        node = pydot.Node(name=node_name, label=label, shape='box', style='filled', fillcolor='lightblue')
        graph.add_node(node)

    # Add edges to the graph
    edges = [(f"node_{i}", f"node_{i+1}") for i in range(num_nodes - 1)]

    for edge in edges:
        graph.add_edge(pydot.Edge(edge[0], edge[1]))

    return graph

def generated_text(query):
    # Your OpenAI API key
    openai.api_key = "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"
                
    # Set the prompt for the presentation
    prompt = '''{} developed a product requirements in the bullet point and put it, in some creative way and make some visual appeling with arrow and tables  for the following description '''.format(query)

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
    st.title("Generate a product reqirement")
    query = st.text_input("Enter the name of the topic:")
    
    if st.button("Generate"):
        presentation_text = generated_text(query)
        st.write(" ")
        st.write("Generate Product requirement:")
        st.write(presentation_text)
        
        # Generate the graph from the generated text
        graph = generate_graph(presentation_text)
        graph_image = graph.create_png()
        
        st.write(" ")
        st.write("Improved Commutative Diagram:")
        st.image(graph_image)

if __name__ == "__main__":
    main()