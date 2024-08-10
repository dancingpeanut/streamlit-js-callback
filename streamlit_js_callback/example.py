import streamlit as st
from streamlit_js_callback import streamlit_js_callback


st.subheader("JS Callback Component")

result = streamlit_js_callback("""
   (async function() {
        return await fetch("https://reqres.in/api/products/3").then(function(response) {
            return response.json();
        })
    })().then((item) => {
        console.log(item)
        sendMessage(JSON.stringify(item))
    })

console.log("-- streamlit_js_callback");
sendMessage("== ==")
return 12345;
""")

if result:
    print("Recived:", result)
    st.text("Recived: " + result)

st.button("haha")

# result = streamlit_js_callback("""
#     window.parent.document.querySelectorAll('button[kind="secondary"]').forEach((item) => {
#         item.addEventListener("click", function(e){
#             console.log(e.target)
#             window.postMessage({type: "jscallback", data: "Click Button!"}, "*");
#         });
#     })
# """)

# if result:
#     print("Recived:", result)
#     st.text("Recived: " + result)
