# streamlit-js-callback

Eval js code with callbaack.

## Installation instructions

```sh
pip install streamlit-js-callback
```

## Usage instructions

```python
import random
import streamlit as st
from streamlit_js_callback import streamlit_js_callback


print("Start render..")

st.subheader("JS Callback Component")


def use_return():
    result1 = streamlit_js_callback("""
    console.log("eval 1 + 1")
    return 1 + 1
    """)
    if result1:
        st.text("Received by use_return: " + str(result1))


def use_send_message():
    result2 = streamlit_js_callback("""
    console.log("hello")
    sendMessage("hello")
    """)
    if result2:
        st.text("Received by use_send_message: " + str(result2))


def exec_async():
    res = streamlit_js_callback("""
    return await fetch("https://reqres.in/api/products/3").then(function(response) {
        return response.json();
    })
    """)
    if res:
        st.text("Received by exec_async: " + str(res))


def exec_event_listen():
    if st.button("btn1"):
        print("btn1 click")
    result3 = streamlit_js_callback("""
        console.log("init 3..")
        let clickCount = 0
        window.parent.document.querySelectorAll('button[kind="secondary"]').forEach((item) => {
            item.addEventListener("click", function(e) {
                clickCount += 1
                console.log(clickCount)
                sendMessage(clickCount)
            });
        })
    """)
    if result3:
        st.text(f"Received event: {result3}")
        print(f"Received event: {result3}")


use_return()
use_send_message()
exec_async()
exec_event_listen()


# my_key = "my_key"
#
#
# @st.fragment
# def exec_in_context_2():
#     global my_key
#     print("my_key", my_key)
#     result4 = streamlit_js_callback("""
#         const res = String(new Date())
#         console.log(res)
#         return res
#         """, key=my_key)
#     if result4:
#         st.text("Received by exec_in_context: " + str(result4))
#         print(f"Received by exec_in_context: {result4}")
#         my_key = str(random.randint(0, 99999))
#         print("my_key", my_key)
#
#
# @st.fragment
# def exec_in_context():
#     if st.button("btn2"):
#         print("btn2 click")
#         exec_in_context_2()
#         print('exec_in_context finish.')
#
#
# exec_in_context()


print("Finish render")

```
