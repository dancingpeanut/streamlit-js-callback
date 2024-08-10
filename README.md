# streamlit-js-callback

Eval js code with callbaack.

## Installation instructions

```sh
pip install streamlit-js-callback
```

## Usage instructions

```python
import streamlit as st

from streamlit_js_callback import streamlit_js_callback

value1 = streamlit_js_callback('sendMessage("I am value1.")')
if value1:
    st.text("Recived value1: " + value1)

st.button("btn")
value2 = streamlit_js_callback("""
    window.parent.document.querySelectorAll('button[kind="secondary"]').forEach((item) => {
        item.addEventListener("click", function(e){
            sendMessage("Click Button!")
        });
    })
""")

if value2:
    st.text("Recived value2: " + value2)

```
