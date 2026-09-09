import { defineHastPlugin } from "satteri";

export const systemWindows = defineHastPlugin({
  name: "system-windows",
  element: {
    filter: ["blockquote"],
    visit(node, ctx) {
      const first = node.children.find((child) => child.type === "element");
      if (!first || first.tagName !== "p") {
        return;
      }
      if (ctx.textContent(first).trim() !== "System") {
        return;
      }
      ctx.setProperty(node, "className", ["system-window"]);
      ctx.setProperty(node, "ariaLabel", "System");
    },
  },
});
