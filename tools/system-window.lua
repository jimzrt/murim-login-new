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
      pandoc.RawBlock("typst", [[#block(
  fill: rgb("#f2f5f8"),
  stroke: 1pt + rgb("#657284"),
  radius: 5pt,
  inset: 12pt,
  width: 100%,
)[
#set text(font: "DejaVu Sans Mono", size: 9pt, fill: rgb("#18232f"))
#text(size: 9pt, weight: "bold", fill: rgb("#34495e"))[System]
#line(length: 100%, stroke: 0.5pt + rgb("#c3ccd5"))
]])
    }
    for index = 2, #block.content do
      table.insert(result, block.content[index])
    end
    table.insert(result, pandoc.RawBlock("typst", "]"))
    return result
  end

  return pandoc.Div(block.content, pandoc.Attr("", {"system-window"}, {}))
end
