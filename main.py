from classes.board import Board

def main():
    board = Board()
    board.get_properties()
    print(f'{board.sum:06.2f}')

if __name__ == "__main__":
    main()
