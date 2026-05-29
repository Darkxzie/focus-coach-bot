import streamlit as st

from chatbot import FocusCoachBot


BOT = FocusCoachBot()


def ensure_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "I am Focus Coach. Bring me one goal, one deadline, or one problem, "
                    "and I will turn it into the next move."
                ),
            }
        ]


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background:
                linear-gradient(160deg, #f3f4f6 0%, #d9e4ec 100%);
        }
        .hero {
            background: linear-gradient(135deg, #0f172a 0%, #1f2937 65%, #334155 100%);
            color: #f8fafc;
            padding: 1.2rem;
            border-radius: 18px;
            box-shadow: 0 18px 40px rgba(15, 23, 42, 0.22);
            margin-bottom: 1rem;
        }
        .note-card {
            background: rgba(248, 250, 252, 0.82);
            border-left: 6px solid #0f172a;
            padding: 0.9rem 1rem;
            border-radius: 12px;
            color: #111827;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.header("Focus Prompts")
        for prompt in [
            "I need a plan to finish my project",
            "motivate me",
            "Help me make a work routine",
        ]:
            if st.button(prompt, use_container_width=True):
                handle_prompt(prompt)
        if st.button("Reset chat", use_container_width=True):
            st.session_state.messages = st.session_state.messages[:1]
            st.rerun()


def render_messages() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def handle_prompt(prompt: str) -> None:
    st.session_state.messages.append({"role": "user", "content": prompt})
    reply = BOT.reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})


def main() -> None:
    st.set_page_config(page_title="Focus Coach Bot", page_icon="🎯", layout="centered")
    ensure_state()
    inject_styles()
    st.markdown(
        """
        <div class="hero">
            <h1>Focus Coach Bot</h1>
            <p>A local-only chatbot with a direct coaching style for planning, focus, and task execution.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note-card">Style: direct, structured, and low-fluff. No API key required.</div>',
        unsafe_allow_html=True,
    )
    render_sidebar()
    render_messages()
    if prompt := st.chat_input("State the task."):
        handle_prompt(prompt)
        st.rerun()


if __name__ == "__main__":
    main()
