import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

board = chess.Board()

while not board.is_game_over():
    print(board)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    print(result)
    board.push(result.move)

engine.quit()
