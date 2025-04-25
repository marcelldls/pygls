from pygls.lsp.server import LanguageServer
from lsprotocol import types

server = LanguageServer("example-server", "v0.1")


@server.feature(
    types.TEXT_DOCUMENT_COMPLETION,
    types.CompletionOptions(trigger_characters=["."]),
)
def completions(params: types.CompletionParams):
    # document = server.workspace.get_document(params.text_document.uri)
    # current_line = document.lines[params.position.line].strip()

    # if not current_line.endswith("hello."):
    #     return []

    return [
        types.CompletionItem(label="marcell"),
        types.CompletionItem(label="was"),
        types.CompletionItem(label="here"),
    ]


if __name__ == "__main__":
    server.start_io()
