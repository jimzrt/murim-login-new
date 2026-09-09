-- Style only blockquotes explicitly headed "System".
-- Other blockquotes, such as the Product User Manual, stay ordinary quotes.

local function is_system(block)
  local first = block.content[1]
  return first and first.t == "Para" and pandoc.utils.stringify(first) == "System"
end

function BlockQuote(block)
  if not is_system(block) then
    return block
  end

  if FORMAT:match("typst") then
    local result = {
      pandoc.RawBlock("typst", [=[#block(
  stroke: 0.7pt + rgb("#e6c86a"),
  inset: 2.8pt,
  width: 100%,
)[
#block(
  fill: gradient.linear(rgb("#1c4a82"), rgb("#2d6aad"), rgb("#1c4a82"), angle: 180deg),
  stroke: 1.2pt + rgb("#d7b45a"),
  inset: 8pt,
  width: 100%,
)[
#set align(center)
#set text(font: "DejaVu Sans Mono", size: 8pt, fill: rgb("#f4f1e6"))
#set par(leading: 0.55em)
#show strong: set text(fill: rgb("#e6c86a"), weight: "bold")
#block(
  fill: rgb("#245a96"),
  stroke: 0.7pt + rgb("#d7b45a"),
  inset: (x: 8pt, y: 2.5pt),
)[#text(size: 6.5pt, tracking: 1.8pt, weight: "bold")[SYSTEM]]
#v(0.35em)
]=])
    }
    for index = 2, #block.content do
      table.insert(result, block.content[index])
    end
    table.insert(result, pandoc.RawBlock("typst", "] ]"))
    return result
  end

  return pandoc.Div(block.content, pandoc.Attr("", {"system-window"}, {}))
end
