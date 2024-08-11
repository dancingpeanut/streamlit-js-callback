import streamlit as st
from streamlit_js_callback import streamlit_js_callback


st.subheader("JS Callback Component")

result1 = streamlit_js_callback("""
console.log("eval 1 + 1")
return 1 + 1
""")
if result1:
    st.text("Received result1: " + str(result1))

result2 = streamlit_js_callback("""
console.log("hello")
sendMessage("hello")
""")
if result2:
    st.text("Received result2: " + str(result2))

st.button("haha")

result3 = streamlit_js_callback("""
    let clickCount = 0
    window.parent.document.querySelectorAll('button[kind="secondary"]').forEach((item) => {
        item.addEventListener("click", function(e) {
            clickCount += 1
            console.log(clickCount)
            sendMessage(clickCount)
        });
    })
""", key="button_click")
if result3:
    st.text(f"Received result3: {result3}")
