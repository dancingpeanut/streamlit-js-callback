# streamlit-js-callback

Use template from [component-template](https://github.com/streamlit/component-template/tree/master/template)

## Develop

* Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
* Clone this repo.
* Create a new Python virtual environment for the template:
```
$ python3 -m venv .venv  # create venv
$ . .venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```
* Initialize and run the component template frontend:
```
$ cd streamlit_js_callback/frontend
$ npm install    # Install npm dependencies
$ npm run start  # Start the Webpack dev server
```
* From a separate terminal, run the template's Streamlit app:
```
$ . venv/bin/activate  # activate the venv you created earlier
$ pip install -e . # install template as editable package
$ streamlit run streamlit_js_callback/example.py  # run the example
```
* If all goes well, you should see something like this:
![Quickstart Success](quickstart.png)
* Modify the frontend code at `streamlit_js_callback/frontend/src/JSCallbackComponent.tsx`.
* Modify the Python code at `streamlit_js_callback/__init__.py`.
