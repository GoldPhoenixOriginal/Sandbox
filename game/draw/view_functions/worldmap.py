from game.parameters import parameters
from game.world import chunk


def draw():
    fx = (parameters.x + parameters.move_x // parameters.block_size) // 16
    fy = (parameters.y + parameters.move_y // parameters.block_size) // 16
    for chunk_y in range(fy, fy + parameters.blocks_y // 16 + 2, 1):
        for chunk_x in range(fx, fx + parameters.blocks_x // 16 + 2, 1):
            x = ((chunk_x - fx) * 16 - parameters.move_x // parameters.block_size % 16) * parameters.block_size \
                - parameters.move_x % parameters.block_size  # TODO: Оптимизировать
            y = ((chunk_y - fy) * 16 - parameters.move_y // parameters.block_size % 16) * parameters.block_size \
                - parameters.move_y % parameters.block_size  # TODO: Оптимизировать
            if (chunk_x, chunk_y) in parameters.loaded_chunks.keys():  # If already generated
                a = parameters.loaded_chunks.get((chunk_x, chunk_y))  # Load
            else:  # If not
                a = chunk.Chunk(chunk_x, chunk_y)  # Create
                a.make_chunk()  # Generate
                parameters.loaded_chunks[(chunk_x, chunk_y)] = a  # And save
            parameters.screen.blit(a.surface, (x, y))
