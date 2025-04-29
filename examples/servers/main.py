from pygls.lsp.server import LanguageServer
from lsprotocol import types
import os
from pathlib import Path

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

    _this_file = Path(__file__)
    log_msg("This file: " + str(_this_file))
    log_msg("ls: " + str(list(_this_file.parent.iterdir())))
    more_completions = []
    try:
        _path = _this_file.parent.parent.parent / ".myHints"
        log_msg("Try open: " + str(_path))
        _read = open(_path)
        more_completions = [types.CompletionItem(label=item.strip()) for item in _read.readlines()]
    except Exception as e:
        log_msg(str(e))


    return base_completions + more_completions


if __name__ == "__main__":
    server.start_io()
