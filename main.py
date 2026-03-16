from maze import Maze


def main():
    maze = Maze(25, 25)
    maze.dfs()
    print(maze)


if __name__ == "__main__":
    main()
