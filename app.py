import openai, os
import streamlit as st


from dotenv import load_dotenv

load_dotenv() 


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



def blogbot():

    st.title('Blogbot - Your Personal AI Blog Generator🤖📝')
    """
    Let me help you generate articles while you sip your beer🍺.
    """
    if "messages" not in st.session_state:
        st.session_state["messages"]=[
            {"role": "system", "content": 
            "You are Blog content generator. you help users generate well detailed article based on the prompt and you do not do any other task aside writing blogs.make the articles top standards"},
            {"role": "assistant", "content": 
            "Your name  is BlogBot,  Your created by Mowa."},
        ]
    if prompt := st.chat_input("Enter a topic.."): 
        openai.api_key = OPENAI_API_KEY
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        msg = response['choices'][0]['message']
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)


def resumebot():

    st.title('Resume.ai - Your Personal Resume Builder🤖📄')
    """
    Need a well-grained Resume? I got you!
    """
    if "messages" not in st.session_state:
        st.session_state["messages"]=[
            {"role": "system", "content": 
            "You are a resume builder."},
            {"role": "assistant", "content": 
            "Your name  is Resume.ai,  Your created by Mowa."},
        ]
    if prompt := st.chat_input("Enter the job description.."): 
        openai.api_key = OPENAI_API_KEY
        st.session_state.messages.append({"role": "user", "content": f'create a sample CV for me using the following job description:{prompt}'})
                                         
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        msg = response['choices'][0]['message']
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)


def prdbot():
    st.title('PRD.ai - Your Personal PRD Creator.🤖📄')
    """
    Let's create your next Product Requirement Documents Together.
    """
    if "messages" not in st.session_state:
        st.session_state["messages"]=[
            {"role": "system", "content": 
            "You are a Senior Product Manager and leader with 25 years of experience in product management and creating product requirement documents. You create the most detailed Product Requirement Documents in the world."},
            {"role": "assistant", "content": 
            "Your name  is PRD-Creator,  You help users create well-grained product requirement document based on the product overview provided."},
        ]
    if prompt := st.chat_input("Enter a brief overview of the product..."): 
        openai.api_key = OPENAI_API_KEY
        st.session_state.messages.append({"role": "user", "content": f'outlining the key details such as overview, objectives, team, status of the product, product messaging, supported platforms, out-of-scope items, user persona, target market, use cases, success metrics, design specifications, key features and all functional and non-functional requirements, also critically explain everything listed  under the functional and non functional requirements .Create a comprehensive and well detailed Product Requirements Document (PRD) using this overview:{prompt}'})
                                         
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        msg = response['choices'][0]['message']
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)






PAGES ={
    "Blogbot":  blogbot,
    "Resume.ai": resumebot,
    "PRD-Creator": prdbot
}

def main():
    st.sidebar.title("Bots")
    choice = st.sidebar.selectbox("Select Bot", list(PAGES.keys()))

    PAGES[choice]()


if __name__ == "__main__":
    main()