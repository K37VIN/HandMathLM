import streamlit as st
import streamlit.components.v1 as components
from solver import solve_equation_text

st.set_page_config(page_title="MyScript Math Solver", layout="centered")

st.title("✍️ Handwritten Text-2-Math Solver")
st.markdown("Use the MyScript interface below to **write your math expression**.")
st.markdown("Then **copy the LaTeX output** and paste it into the field below to solve it.")


components.html(
    """
    <iframe 
        src="https://webdemo.myscript.com/views/math/index.html" 
        width="600" 
        height="500"
        style="border:1px solid #ccc;border-radius:10px;">
    </iframe>
    """,
    height=520,
)


st.markdown("### 📥 Paste Detected LaTeX Here")
latex_input = st.text_input("LaTeX Equation", placeholder="e.g., \\frac{d}{dx} x^2")

if latex_input:
    try:
        st.markdown("### 📄 Rendered Equation")
        st.latex(latex_input)

        st.markdown("### 🤖 Solver Output")
        result = solve_equation_text(latex_input)
        st.success(f"✅ Answer: {result}")
    except Exception as e:
        st.error(f"❌ Error solving equation: {e}")
else:
    st.info("Paste LaTeX from the MyScript box above and press Enter.")
