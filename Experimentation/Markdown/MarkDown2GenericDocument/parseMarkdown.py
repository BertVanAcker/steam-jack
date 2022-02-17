from steam_jack.Documentor.CustomMarkdownParser import CustomMarkdownParser



customRenderer = CustomMarkdownParser()
genericDocument = customRenderer.render_markdown2GenericDocument(document="input/TEST.md")
a = 1