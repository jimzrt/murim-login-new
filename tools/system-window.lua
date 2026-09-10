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

function HorizontalRule()
  if not FORMAT:match("typst") then
    return nil
  end
  return pandoc.RawBlock("typst", string.format(
    '#align(center, block(above: 1.6em, below: 1.6em, image("%s", width: 1.35em)))',
    ornament("yin-yang.svg")
  ))
end

function BlockQuote(block)
  if not is_system(block) then
    return block
  end

  if FORMAT:match("typst") then
    local result = {
      pandoc.RawBlock("typst", string.format(
        '#murim-plaque("%s", "%s")[',
        ornament("corner.svg"),
        ornament("dragon.svg")
      )),
    }
    for index = 2, #block.content do
      table.insert(result, block.content[index])
    end
    table.insert(result, pandoc.RawBlock("typst", "]"))
    return result
  end

  return pandoc.Div(block.content, pandoc.Attr("", {"system-window"}, {}))
end
