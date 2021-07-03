import * as ReactDOM from "react-dom";
import "./js/custom";

import { UploadForm } from "./upload";
import React, { ComponentClass, FunctionComponent } from "react";
import { MarkdownPreview } from "./markdown";

const CreateComponent = (component: FunctionComponent | ComponentClass) => {
    return (element: Element) => {
        ReactDOM.render(React.createElement(component), element);
    };
};

(window as any).ts = {
    UploadForm: CreateComponent(UploadForm),
    MarkdownPreview: CreateComponent(MarkdownPreview),
};
