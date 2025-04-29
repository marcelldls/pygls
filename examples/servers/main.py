from pygls.lsp.server import LanguageServer
from lsprotocol import types
import os

server = LanguageServer("example-server", "v0.1")

def log_msg(message: str):
    server.window_show_message(types.ShowMessageParams(types.MessageType.Info,message))

@server.feature(
    types.TEXT_DOCUMENT_COMPLETION,
    types.CompletionOptions(trigger_characters=["."]),
)
def completions(params: types.CompletionParams):
    # document = server.workspace.get_document(params.text_document.uri)
    # current_line = document.lines[params.position.line].strip()

    # if not current_line.endswith("hello."):
    #     return []

    base_completions = [
        types.CompletionItem(label="marcell"),
        types.CompletionItem(label="was"),
        types.CompletionItem(label="here"),
    ]

    log_msg("ls:" + str(os.listdir('.')))
    more_completions = []
    try:
        _read = open("../../.myHint")
        more_completions = [types.CompletionItem(label=item.strip()) for item in _read.readlines()]
    except Exception as e:
        log_msg(str(e))


    return base_completions + more_completions


if __name__ == "__main__":
    server.start_io()
