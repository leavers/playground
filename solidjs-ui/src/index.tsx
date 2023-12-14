/* @refresh reload */
import { render } from "solid-js/web";

import "@unocss/reset/normalize.css";
import "virtual:uno.css";
import "./index.css";
import App from "./App";

const root = document.getElementById("root");

render(() => <App />, root!);
