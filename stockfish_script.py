import chess.engine
import docker

# Connect to the Docker engine
docker_client = docker.from_env()

# Start the Stockfish container
stockfish_container = docker_client.containers.run("stockfish", detach=True)

# Connect to the Stockfish engine
engine = chess.engine.SimpleEngine.popen_uci("docker://{}".format(stockfish_container.id))

# Set up the board position
board = chess.Board()
board.push_san("e4")
board.push_san("e5")

# Get the best move from Stockfish
result = engine.play(board, chess.engine.Limit(time=2.0))
best_move = result.move

# Make the best move on the board
board.push(best_move)

# Print the updated board
print(board)

# Stop the Stockfish container
stockfish_container.stop()