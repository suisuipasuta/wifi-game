import pyxel

class Sumaho:
    def __init__(self):
        # プレイヤーの初期位置
        self.player_x = 9
        self.player_y = 103

        # プレイヤーの4つの角の位置をリストで管理
        self.player_positions = [
            (self.player_x, self.player_y),  # 左上
            (self.player_x + 14, self.player_y),  # 右上
            (self.player_x + 14, self.player_y + 16),  # 右下
            (self.player_x, self.player_y + 16),  # 左下
        ]

        # スタート
        self.start = False

        # ゲームオーバー
        self.gameover = False

        # 得点
        self.point = 0


class App:
    def __init__(self):
        pyxel.init(128, 128)

        self.sumaho = Sumaho()

        # タイルマップ呼び出し
        pyxel.load("sumaho.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        #print(self.sumaho.player_positions[0][1])
        #print(self.sumaho.player_positions[1][0])
        self.update_sumaho()
        

    def draw(self):
        pyxel.cls(0)
        #map
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        #sumaho
        pyxel.blt(self.sumaho.player_positions[0][0], self.sumaho.player_positions[0][1], 0, 49, 0, 14, 16)
        print(self.sumaho.point)

    


    def update_sumaho(self):
        #現在地のタイル単位の座標
        target_x = self.sumaho.player_positions[0][0] // 8
        target_y = self.sumaho.player_positions[0][1] // 8
        #操作の設定
        if pyxel.btn(pyxel.KEY_UP) and not self.is_tile_obstacle(target_x, target_y - 1):
            self.move_player(0, -1)
        elif pyxel.btn(pyxel.KEY_DOWN) and not self.is_tile_obstacle(target_x, target_y + 1):
            self.move_player(0, 1)
        elif pyxel.btn(pyxel.KEY_LEFT) and not self.is_tile_obstacle(target_x - 1, target_y):
            self.move_player(-1, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT) and not self.is_tile_obstacle(target_x + 1, target_y):
            self.move_player(1, 0)


    def is_tile_obstacle(self, x, y):
        # タイルが色14であれば障害物があると判断
        if(
            pyxel.tilemap(0).pget(x,y) == (0,0) 
        ):
            return True
        else:
            return False
    def move_player(self, dx, dy):
    # 移動先の座標をリストに代入
        new_positions = [
            (self.sumaho.player_positions[0][0] + dx, self.sumaho.player_positions[0][1] + dy),
            (self.sumaho.player_positions[1][0] + dx, self.sumaho.player_positions[1][1] + dy),
            (self.sumaho.player_positions[2][0] + dx, self.sumaho.player_positions[2][1] + dy),
            (self.sumaho.player_positions[3][0] + dx, self.sumaho.player_positions[3][1] + dy),
        ]
        # print(new_positions)

    # 四隅で移動判定
        for i in range(4):
            if self.is_tile_obstacle(new_positions[i][0] // 8, new_positions[i][1] // 8):
                print("hikkakatta")
                break
            if i == 3:
                for j in range(4):
                    self.sumaho.player_positions[j] = new_positions[j]
        
App()
