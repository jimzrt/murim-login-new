-- Style only blockquotes explicitly headed "System".
-- Other blockquotes, such as the Product User Manual, stay ordinary quotes.

local function is_system(block)
  local first = block.content[1]
  return first and first.t == "Para" and pandoc.utils.stringify(first) == "System"
end

local function ornament(name)
  local script_dir = pandoc.path.directory(PANDOC_SCRIPT_FILE)
  local repo = pandoc.path.directory(script_dir)
  return pandoc.path.join({repo, "reader", "src", "ornaments", name})
end

function BlockQuote(block)
  if not is_system(block) then
    return block
  end

  if FORMAT:match("typst") then
    local corner = ornament("corner.svg")
    local dragon = ornament("dragon.svg")
    local result = {
      pandoc.RawBlock("typst", string.format([=[#block(
  width: 100%%,
  inset: (y: 8pt),
  breakable: false,
)[
#block(
  width: 100%%,
  fill: gradient.linear(rgb("#3a78b8"), rgb("#2d6aad"), rgb("#1c4a82"), angle: 180deg),
  stroke: 1.25pt + rgb("#e6c86a"),
  inset: (x: 9pt, y: 11pt),
)[
#place(top + left, dx: -9.6pt, dy: -11.6pt, image("%s", width: 17pt))
#place(top + right, dx: 9.6pt, dy: -11.6pt, scale(x: -100%%, origin: right + top)[#image("%s", width: 17pt)])
#place(bottom + left, dx: -9.6pt, dy: 9.6pt, scale(y: -100%%, origin: left + bottom)[#image("%s", width: 17pt)])
#place(bottom + right, dx: 9.6pt, dy: 9.6pt, scale(x: -100%%, y: -100%%, origin: right + bottom)[#image("%s", width: 17pt)])
#set align(center)
#set text(font: "DejaVu Sans", size: 8.2pt, fill: rgb("#ffffff"), weight: "bold")
#set par(leading: 0.55em)
#show strong: set text(fill: rgb("#e6c86a"), weight: "bold")
#box(
  fill: rgb("#245a96"),
  stroke: 0.8pt + rgb("#e6c86a"),
  inset: (x: 8pt, y: 2.4pt),
)[
#grid(
  columns: 3,
  column-gutter: 5pt,
  align: horizon,
  image("%s", height: 8pt),
  text(size: 6.5pt, tracking: 1.8pt, weight: "bold")[SYSTEM],
  scale(x: -100%%)[#image("%s", height: 8pt)],
)
]
#v(0.45em)
]=], corner, corner, corner, corner, dragon, dragon))
    }
    for index = 2, #block.content do
      table.insert(result, block.content[index])
    end
    table.insert(result, pandoc.RawBlock("typst", "] ]"))
    return result
  end

  return pandoc.Div(block.content, pandoc.Attr("", {"system-window"}, {}))
end
