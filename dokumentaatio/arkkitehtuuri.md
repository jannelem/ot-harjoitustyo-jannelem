```mermaid
classDiagram
  TicTacToe "1" -- "9...225" Tile
  ui "1" -- "1" TicTacToe
  Tile --|> Sprite
  GameService ..> TicTacToe
```
