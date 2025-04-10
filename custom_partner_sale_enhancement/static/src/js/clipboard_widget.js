/** @odoo-module **/

import { CharField } from "@web/views/fields/char/char_field";
import { registry } from "@web/core/registry";

export class CopyClipboardField extends CharField {
    setup() {
        super.setup();
        console.log("CopyClipboardField INIT", this.props);
    }

    async onCopyClick() {
        const value = this.props.value;
        if (navigator.clipboard && value) {
            try {
                await navigator.clipboard.writeText(value);
                this.env.services.notification.add("Copied to clipboard!", {
                    type: "success",
                });
            } catch (err) {
                console.error("Clipboard error:", err);
                this.env.services.notification.add("Failed to copy!", {
                    type: "danger",
                });
            }
        }
    }
}

CopyClipboardField.template = "custom_partner_sale_enhancement.CopyClipboardField";

CopyClipboardField.props = {
    value: String,
    name: String,
    readonly: Boolean,
};

registry.category("fields").add("copy_clipboard", CopyClipboardField);
