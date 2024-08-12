import os
import streamlit as st
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("streamlit_js_callback"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_js_callback",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_js_callback", path=build_dir)


def _stylized_container(key):
    """
    Add a spaceless container to the app.

    Insert a container into the app, which receives an iframe that does not
    render anything. Style this container using CSS and a unique key. The style
    targeting `"stVerticalBlockBorderWrapper"` removes 1rem of space added by
    the iframe. While the style targeting the div that contains the iframe
    changes its height from 1.5625rem to 0.

    Parameters
    ----------
    key : str, int or None
        A key associated with this container. This needs to be unique since all
        styles will be applied to the container with this key.

    Returns
    -------
    container : DeltaGenerator
        A container object. Elements can be added to this container using
        either the "with" notation or by calling methods directly on the
        returned object.
    """
    key = f"js_callback_{key}"
    selector = f"div.element-container > div.stHtml > span.{key}"
    css = (
        f"""
        <style>
            div[data-testid="stVerticalBlockBorderWrapper"]:has(> div > div[data-testid="stVerticalBlock"] > {selector}) {{
                display: none;
            }}
        </style>
        """
        f"<span class='{key}'></span>"
    )
    container = st.container(height=0)
    container.html(css)
    return container


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def streamlit_js_callback(code, key=None):
    """Create a new instance of "streamlit_js_callback".

    Parameters
    ----------
    code: str
        The javascript code that is to be executed on the client side. It can be synchronous or asynchronous."
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    string
        The result of code

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.

    with _stylized_container(key=key):
        component_value = _component_func(code=code, key=key, default=None)

    if str(component_value).startswith("Eval code error: "):
        raise Exception(component_value)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value
