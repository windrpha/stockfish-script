import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(r"stockfish_14_linux_x64_modern/stockfish_14_x64_modern")

board = chess.Board()

while not board.is_game_over():
    print(board)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    print(result)
    board.push(result.move)

engine.quit()
