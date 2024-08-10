import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  hasRun: boolean
}

class JSCallbackComponent extends StreamlitComponentBase<State> {
  public state = { hasRun: false }

  sendMessage(msg: string) {
    Streamlit.setComponentValue(msg)
  }

  async componentDidMount() {
    const code = this.props.args["code"]

    if (!this.state.hasRun) {
      try {
        const dynamicFunction = new Function("sendMessage", code)
        dynamicFunction(this.sendMessage.bind(this))
      } catch (e) {
        this.sendMessage("Eval code error: " + String(e))
      }
      this.setState({ hasRun: true })
    }
  }

  public render = (): ReactNode => {
    return null
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(JSCallbackComponent)
