import pygame
import random
import math
import time
pygame.init()
pygame.mixer.init()
sound_kame_charge = pygame.mixer.Sound("img/kamecharge.wav")
sound_kame_shoot = pygame.mixer.Sound("img/kameshoot.wav")
sound_dash = pygame.mixer.Sound("img/dash.wav")
gonggenki_sound=pygame.mixer.Sound("img/gonggenki.mp3")
nemgenki_sound=pygame.mixer.Sound("img/kiblast.mp3")
genki_sound=pygame.mixer.Sound("img/genki.mp3")
kaioken_sound = pygame.mixer.Sound("img/kaioken.mp3")
kiblast_sound = pygame.mixer.Sound("img/kiblast.mp3")
ssj1_sound = pygame.mixer.Sound("img/ssj1.mp3")
ssj3_sound = pygame.mixer.Sound("img/transform1.mp3")
sound_kame_charge.set_volume(0.6)
sound_kame_shoot.set_volume(0.9)
kiblast_sound.set_volume(0.3)
genki_sound.set_volume(1)
gonggenki_sound.set_volume(0.32)
nemgenki_sound.set_volume(0.3)
sound_dash.set_volume(0.9)
ssj1_sound.set_volume(0.3)
ssj3_sound.set_volume(0.8)
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
white_flash_timer = 0 #lóe mh khi trúng genki dama
pygame.display.set_caption("Hai Dang")
clock = pygame.time.Clock()
# pygame.mixer.music.load("dbgt1.mp3") 
# pygame.mixer.music.play(-1) 
# pygame.mixer.music.set_volume(1.2)
# Load background and icons
# load
bg = pygame.image.load('img/background1.png')
bg = pygame.transform.scale(bg, (800, 400))
icon = pygame.image.load('img/lgoku.png')   
pygame.display.set_icon(icon)
scale = lambda img: pygame.transform.scale(img, (int(img.get_width() * 0.32), int(img.get_height() * 0.32)))
scale1 = lambda img: pygame.transform.scale(img, (int(img.get_width() * 0.28), int(img.get_height() * 0.32)))
scale2 = lambda img: pygame.transform.scale(img, (int(img.get_width() * 0.34), int(img.get_height() * 0.32)))
scale3 = lambda img: pygame.transform.scale(img, (int(img.get_width() * 0.26), int(img.get_height() * 0.32)))
# Load character sprites
ssj3_lightning_imgs = [
    pygame.transform.scale(pygame.image.load('img/971.png'), (40, 40)),
    pygame.transform.scale(pygame.image.load('img/972.png'), (40, 40)),
    pygame.transform.scale(pygame.image.load('img/973.png'), (40, 40)),
    pygame.transform.scale(pygame.image.load('img/974.png'), (40, 40)),
]
ki_ball_imgs = [
    pygame.transform.scale(pygame.image.load('img/2175.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('img/2176.png'), (80, 80))
]
spirit_streak_big = pygame.transform.scale(pygame.image.load('img/53.png'), (12, 12))
spirit_streak_small = pygame.transform.scale(pygame.image.load('img/76.png'), (6, 6))
khien_imgs = [
    pygame.transform.scale(pygame.image.load('img/khien1.png'), (70, 70)),
    pygame.transform.scale(pygame.image.load('img/khien2.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien3.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien2.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien3.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien2.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien3.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien2.png'), (100, 100)),
    pygame.transform.scale(pygame.image.load('img/khien3.png'), (100, 100)),
]
characters = {
    'goku': {
        'left': pygame.transform.scale(pygame.image.load('img/lgoku.png'), (62, 62)),
        'right': pygame.transform.scale(pygame.image.load('img/rgoku.png'), (62, 62)),
        'ui_left': pygame.transform.scale(pygame.image.load('img/lui.png'), (62, 62)),
        'ui_right': pygame.transform.scale(pygame.image.load('img/rui.png'), (62, 62)),
        'kaioken_left': pygame.transform.scale(pygame.image.load('img/lkaioken.png'), (55, 55)),
        'kaioken_right': pygame.transform.scale(pygame.image.load('img/rkaioken.png'), (55, 55)),
        'skill1_color': (0, 255, 255),  # Kame xanh
        'skill2': 'stun',
        'health': 360,
        'damage': 10
    },
    'vegeta': {
        'left': pygame.transform.scale(pygame.image.load('img/lvegeta.png'), (60, 60)),
        'right': pygame.transform.scale(pygame.image.load('img/rvegeta.png'), (60, 60)),
        'khi1_left': pygame.transform.scale(pygame.image.load('img/lkhi1.png'), (80, 80)),
        'khi1_right': pygame.transform.scale(pygame.image.load('img/rkhi1.png'), (80, 80)),
        'skill1_color': (255, 255, 0),  # Kame vàng
        'skill2': 'buff_damage',
        'health': 300,
        'damage': 15,
        'khi7_left': pygame.transform.scale(pygame.image.load('img/lkhi7.png'), (120, 120)),
        'khi7_right': pygame.transform.scale(pygame.image.load('img/rkhi7.png'), (120, 120)),
    },
    'piccolo': {
        'left': pygame.transform.scale(pygame.image.load('img/lpcl.png'), (60, 60)),
        'right': pygame.transform.scale(pygame.image.load('img/rpcl.png'), (60, 60)),
        'pclo_left': pygame.transform.scale(pygame.image.load('img/lpclo.png'), (60, 60)),
        'pclo_right': pygame.transform.scale(pygame.image.load('img/rpclo.png'), (60, 60)),
        'pcl1_left': pygame.transform.scale(pygame.image.load('img/lpcl1.png'), (85, 60)),
        'pcl1_right': pygame.transform.scale(pygame.image.load('img/rpcl1.png'), (85, 60)),
        'skill1_color': (200, 0, 200),  # Masenko tím
        'skill2': 'heal',
        'health': 440,
        'damage': 8
    },
    'broly': {
        'left': pygame.transform.scale(pygame.image.load('img/lbroly.png'), (65, 60)),
        'right': pygame.transform.scale(pygame.image.load('img/rbroly.png'), (65, 60)),
        'lssj_left': pygame.transform.scale(pygame.image.load('img/llssj.png'), (70, 60)),
        'lssj_right': pygame.transform.scale(pygame.image.load('img/rlssj.png'), (70, 60)),
        'ssj4_left': pygame.transform.scale(pygame.image.load('img/lssj4.png'), (58, 65)),
        'ssj4_right': pygame.transform.scale(pygame.image.load('img/rssj4.png'), (58, 65)),
        'skill1_color': (0, 255, 100),  # Màu đặc trưng cho đạn Broly
        'skill2': 'berserker',
        'health': 400,
        'damage': 12
    },
    'gohan': {
        'left': pygame.transform.scale(pygame.image.load('img/lgohan.png'), (40, 60)),
        'right': pygame.transform.scale(pygame.image.load('img/rgohan.png'), (40, 60)),
        'ssj1_left': pygame.transform.scale(pygame.image.load('img/lssj1.png'), (45, 62)),
        'ssj1_right': pygame.transform.scale(pygame.image.load('img/rssj1.png'), (45, 62)),
        'beast_left': pygame.transform.scale(pygame.image.load('img/lbeast.png'), (48, 62)),
        'beast_right': pygame.transform.scale(pygame.image.load('img/rbeast.png'), (48, 62)),
        'maxbeast_left': pygame.transform.scale(pygame.image.load('img/lmaxbeast.png'), (50, 62)),
        'maxbeast_right': pygame.transform.scale(pygame.image.load('img/rmaxbeast.png'), (50, 62)),
        'skill1_color': (255, 255, 100),
        'skill2': 'focus_ki',  # logic riêng cho gohan sẽ dùng tên này
        'health': 380,
        'damage': 10
    },
    'goku_modular': {
        # Chân
        'right': pygame.transform.scale(pygame.image.load('img/dungim.png'), (40, 40)),
        'left': pygame.transform.flip(pygame.transform.scale(pygame.image.load('img/dungim.png'), (40, 40)), True, False),
        'chan_dung': scale(pygame.image.load('img/dungimchan.png')),
        'gong_than': scale(pygame.image.load('img/gongkame.png')),                # Thân khi gồng
        'bang_than': scale(pygame.image.load('img/chuongkame.png')),             # Thân khi bắn beam
        'banchuong_than': scale(pygame.image.load('img/banchuongthan.png')),
        'bang_chan': scale(pygame.image.load('img/gongkame-bankame-chan.png')), 
        'chan_chay': [
            scale(pygame.image.load('img/chaychan1.png')),
            scale(pygame.image.load('img/chaychan2.png')),
            scale(pygame.image.load('img/chaychan3.png')),
            scale(pygame.image.load('img/chaychan4.png')),
        ],
        'than_dung': scale(pygame.image.load('img/dungimthan.png')),
        'than_chay': [
            scale(pygame.image.load('img/chayphaithan.png')),
            scale(pygame.image.load('img/chayphaithan2.png')),
            scale(pygame.image.load('img/chayphaithan3.png')),
            scale(pygame.image.load('img/chayphaithan4.png')),
            scale(pygame.image.load('img/chayphaithan5.png')),
        ],
        'dau_dung': scale(pygame.image.load('img/dungim.png')),
        'dau_chay': scale(pygame.image.load('img/chayphai.png')),
        'danhthuong_than_list': [
            scale(pygame.image.load('img/danhthuong1.png')),
            pygame.transform.scale(pygame.image.load('img/chayphaithan.png'), (int(pygame.image.load('img/chayphaithan.png').get_width() * 0.4), pygame.image.load('img/chayphaithan.png').get_height()*0.32))
        ],
        'chan_danhthuong': [
            scale(pygame.image.load('img/32.png')),
            scale(pygame.image.load('img/gongkame-bankame-chan.png')),
        ],
        'nhay_chan': scale(pygame.image.load('img/nhaychan.png')),
        'nhay_than': scale(pygame.image.load('img/nhaythan.png')),
        'roi_chan': scale(pygame.image.load('img/roichan.png')),
        'roi_than': scale(pygame.image.load('img/roithan.png')),
        'than_thu': scale(pygame.image.load('img/thuthan.png')),
        # skill
        'kaioken_aura': [
            pygame.transform.scale(pygame.image.load('img/975.png'), (78, 75)),
            pygame.transform.scale(pygame.image.load('img/977.png'), (78, 75)),
            pygame.transform.scale(pygame.image.load('img/978.png'), (78, 75)),
            pygame.transform.scale(pygame.image.load('img/986.png'), (78, 75)),
        ],
        # thuoc tinh
        'skill1_color': (0, 255, 255),
        'skill2': 'kaioken',
        'health': 600,
        'damage': 12,
        # ssj1 (dạng T so với các nhân vật khác , ảnh giống dạng base nhưng thêm chữ ssj1 ví dụ ssj1thuthan.png)
        # THÂN
        'ssj1_than_dung': scale(pygame.image.load('img/ssj1dungimthan.png')),
        'ssj1_than_chay': [
            scale(pygame.image.load('img/ssj1chayphaithan.png')),
            scale(pygame.image.load('img/ssj1chayphaithan2.png')),
            scale(pygame.image.load('img/ssj1chayphaithan3.png')),
            scale(pygame.image.load('img/ssj1chayphaithan4.png')),
            scale(pygame.image.load('img/ssj1chayphaithan5.png')),
        ],
        'ssj1_danhthuong_than_list': [
            scale(pygame.image.load('img/ssj1danhthuong1.png')),
            pygame.transform.scale(pygame.image.load('img/ssj1chayphaithan.png'), (int(pygame.image.load('img/ssj1chayphaithan.png').get_width() * 0.4), pygame.image.load('img/ssj1chayphaithan.png').get_height()*0.32)),
        ],

        # CHÂN
        'ssj1_chan_dung': scale(pygame.image.load('img/ssj1dungimchan.png')),
        'ssj1_chan_chay': [
            scale(pygame.image.load('img/ssj1chaychan1.png')),
            scale(pygame.image.load('img/ssj1chaychan2.png')),
            scale(pygame.image.load('img/ssj1chaychan3.png')),
            scale(pygame.image.load('img/ssj1chaychan4.png')),
        ],
        'ssj1_chan_danhthuong': [
            scale1(pygame.image.load('img/ssj1danhchan1.png')),
            scale1(pygame.image.load('img/ssj1bankamechan.png')),
        ],
        'ssj1_nhay_chan': scale(pygame.image.load('img/ssj1nhaychan.png')),
        'ssj1_roi_chan': scale(pygame.image.load('img/ssj1roichan.png')),

        # ĐẦU
        'ssj1_dau_dung': scale(pygame.image.load('img/ssj1dungim.png')),
        'ssj1_dau_chay': scale(pygame.image.load('img/ssj1chayphai.png')),

        # GỒNG & BẮN
        'ssj1_gong_than': scale(pygame.image.load('img/ssj1gongkame.png')),
        'ssj1_bang_than': scale(pygame.image.load('img/ssj1chuongkame.png')),
        'ssj1_banchuong_than': scale(pygame.image.load('img/ssj1banchuongthan.png')),
        'ssj1_bang_chan': scale1(pygame.image.load('img/ssj1bankamechan.png')),

        # NHẢY, RƠI, THU
        'ssj1_than_nhay': scale(pygame.image.load('img/ssj1nhaythan.png')),
        'ssj1_than_roi': scale(pygame.image.load('img/ssj1roithan.png')),
        'ssj1_than_thu': scale(pygame.image.load('img/ssj1thuthan.png')), 
        'ssj1_aura': [
            pygame.transform.scale(pygame.image.load('img/964.png'), (90, 90)),
            pygame.transform.scale(pygame.image.load('img/965.png'), (90, 90)),
            pygame.transform.scale(pygame.image.load('img/966.png'), (90, 90)),
            pygame.transform.scale(pygame.image.load('img/967.png'), (90, 90)),
        ],
        'ssj1_heal_aura': [
            pygame.transform.scale(pygame.image.load('img/35.png'), (110, 110)),
            pygame.transform.scale(pygame.image.load('img/36.png'), (110, 110)),
            pygame.transform.scale(pygame.image.load('img/37.png'), (110, 110)),
            pygame.transform.scale(pygame.image.load('img/38.png'), (110, 110)),
        ],
        # ssj3
        'ssj3_than_dung': scale(pygame.image.load('img/ssj3dungimthan.png')),
        'ssj3_than_chay': [
            scale(pygame.image.load('img/ssj3chayphaithan.png')),
            scale(pygame.image.load('img/ssj3chayphaithan2.png')),
            scale(pygame.image.load('img/ssj3chayphaithan3.png')),
            scale(pygame.image.load('img/ssj3chayphaithan4.png')),
            scale(pygame.image.load('img/ssj3chayphaithan5.png')),
        ],
        'ssj3_danhthuong_than_list': [
            scale2(pygame.image.load('img/ssj3danhthuong1.png')),
            pygame.transform.scale(
                pygame.image.load('img/ssj3chayphaithan.png'),
                (int(pygame.image.load('img/ssj3chayphaithan.png').get_width() * 0.4),
                pygame.image.load('img/ssj3chayphaithan.png').get_height() * 0.32)
            ),
        ],

        'ssj3_chan_dung': scale(pygame.image.load('img/ssj3dungimchan.png')),
        'ssj3_chan_chay': [
            scale(pygame.image.load('img/ssj3chaychan1.png')),
            scale(pygame.image.load('img/ssj3chaychan2.png')),
            scale(pygame.image.load('img/ssj3chaychan3.png')),
            scale(pygame.image.load('img/ssj3chaychan4.png')),
        ],
        'ssj3_chan_danhthuong': [
            scale1(pygame.image.load('img/ssj3danhchan1.png')),
            scale3(pygame.image.load('img/ssj3bankamechan.png')),
        ],

        'ssj3_nhay_chan': scale(pygame.image.load('img/ssj3nhaychan.png')),
        'ssj3_roi_chan': scale(pygame.image.load('img/ssj3roichan.png')),

        'ssj3_dau_dung': scale(pygame.image.load('img/ssj3dungim.png')),
        'ssj3_dau_chay': scale(pygame.image.load('img/ssj3chayphai.png')),

        'ssj3_gong_than': scale(pygame.image.load('img/ssj3gongkame.png')),
        'ssj3_bang_than': scale(pygame.image.load('img/ssj3chuongkame.png')),
        'ssj3_banchuong_than': scale(pygame.image.load('img/ssj3banchuongthan.png')),
        'ssj3_bang_chan': scale3(pygame.image.load('img/ssj3bankamechan.png')),

        'ssj3_than_nhay': scale(pygame.image.load('img/ssj3nhaythan.png')),
        'ssj3_than_roi': scale(pygame.image.load('img/ssj3roithan.png')),
        'ssj3_than_thu': scale(pygame.image.load('img/ssj3thuthan.png')),

        'ssj3_aura': [
            pygame.transform.scale(pygame.image.load('img/964.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('img/965.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('img/966.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('img/967.png'), (100, 100)),
        ],
        
        'ssj3_skill2_prepare': scale(pygame.image.load('img/1581.png')),  # ảnh bay
        'ki_ball1': scale(pygame.image.load('img/2175.png')),
        'ki_ball2': scale(pygame.image.load('img/2176.png')),
    }

}

# Character selection state
show_character_info = True  # Hiển thị màn hình mô tả nhân vật ban đầu
selecting = True
show_instructions = True
game_over = False
winner = ""
player1_choice = None
player2_choice = None
playing_with_ai = False
def handle_ai(player1, ai):
    if ai.is_stunned:
        return
    if ai.ssj1_healing:
        return  # Đang hồi máu → đừng làm gì hết
    if ai.ssj3_skill2_active:return
    if ai.transforming:return
    distance = abs(ai.x - player1.x)
    direction_to_player = 1 if player1.x > ai.x else -1
    ai.facing = 'right' if direction_to_player == 1 else 'left'
    ai.defending= True
    # --- 0. Né nếu bị spam đòn ---
    if ai.hit_recently >= 3:
        if random.random() < 0.4 and ai.dash_timer == 0:
            dash_speed = 120
            dash_dir = -1 if player1.x > ai.x else 1
            ai.x += dash_speed * dash_dir
            ai.dash_timer = 90
            ai.x = max(0, min(ai.x, WIDTH - ai.width))
            ai.hit_recently = 0
            return
        elif random.random() < 0.3:
            if ai.name != 'broly' or not ai.lssj_active:
                ai.defending = True
            ai.hit_recently = 0
            return
    else:
        ai.defending = False

    # --- 1. Né ultimate ---
    if player1.charging_ultimate and distance < 350 and ai.dash_timer == 0:
        action = random.choice(['dash', 'jump', 'dash_jump'])
        
        if action == 'dash' or action == 'dash_jump':
            dash_distance = 120  # tăng khoảng dash để thoát beam
            ai.x += dash_distance * (-direction_to_player)
            ai.x = max(0, min(ai.x, WIDTH - ai.width))
            ai.dash_timer = 60

        if action == 'jump' or action == 'dash_jump':
            if ai.on_ground:
                ai.vel_y = -10
                ai.on_ground = False
        return


    # --- 2. Nhảy né đòn ---
    if random.random() < 0.01 and ai.on_ground:
        if random.random()<0.95:
            if ai.big_beams:return
        if random.random() < 0.5:
            if ai.charging_ultimate:return
        ai.vel_y = -10
        ai.on_ground = False
        sound_dash.play()
    if random.random() < 0.04:
        if random.random()<0.55:
            if ai.big_beams:return
        dash_distance = 120  
        ai.x += dash_distance * (direction_to_player)
        ai.x = max(0, min(ai.x, WIDTH - ai.width))
        ai.dash_timer = 60
    if random.random() < 0.02:
        if random.random()<1.0:
            if ai.big_beams:return
        dash_distance = 50  
        ai.x += dash_distance * (-direction_to_player)
        ai.x = max(0, min(ai.x, WIDTH - ai.width))
        ai.dash_timer = 60
    # --- 3. Kích hoạt T khi máu yếu ---
    if ai.health < 0.75 * characters[ai.name]['health']:
        if ai.ki >= 50 and ai.skill6_cd == 0 and not ai.t_transforming and not ai.used_T:
            ai.use_ki(50)
            ai.t_transforming = True
            ai.t_transform_timer = 60
            ai.time_since_T = 0  # Reset đếm thời gian T
            return
    if ai.charging_ultimate : return
    # --- 4. Heal khi rất yếu ---
    if ai.health < 0.4 * characters[ai.name]['health']:
        if ai.skill2_type == 'heal' and ai.skill2_cd == 0 and ai.ki >= 40:
            ai.use_ki(40)
            ai.health = min(ai.health + 120, characters[ai.name]['health'])
            ai.skill2_cd = 360
        elif ai.ssj1_modular ==  True and player2.skill2_cd == 0 and ai.ki >= 40:
            ai.use_ki(40)
            ai.ssj1_healing = True
            ai.ssj1_heal_timer = 300
            ai.total_healed = 0
            ai.heal_tick_counter = 0
            ai.skill2_cd = 360
            return
    # --- 5. Biến hình O nếu đã dùng T ---
    if ai.used_T:
        if ai.name == 'goku' and ai.ki >= 50 and not ai.ui and ai.ui_cooldown == 0:
            ai.transform_ui()
            return
        elif ai.name == 'vegeta' and ai.ki >= 50 and not ai.khi7 and ai.khi7_cooldown == 0:
            ai.transform_ssj()
            return
        elif ai.name == 'piccolo' and ai.ki >= 50 and not ai.pclo_transform and ai.pclo_cooldown == 0:
            ai.transform_pclo()
            return
        elif ai.name == 'broly' and ai.ki >= 50 and not ai.ssj4_active and ai.can_use_ssj4 and ai.ssj4_cd == 0:
            ai.transform_ssj4()
            return
        elif ai.name == 'gohan' and ai.ki >= 50 and ai.used_T and not ai.beast and not ai.transforming:
            if ai.health >= 0.4 * characters['gohan']['health']:
                if ai.beast_cooldown == 0:
                    ai.transform_beast_upgrade()
                    return
            else:
                if ai.maxbeast_cooldown == 0:
                    ai.transform_beast_upgrade()
                    return
        elif ai.name == 'goku_modular' and ai.ki >= 50 and ai.used_T and not ai.ssj3_modular:
            low_hp = ai.health < 0.25 * characters[ai.name]['health']
            if ai.time_since_T >= 180 or low_hp:
                ai.transform_ssj3()
                return

    # --- 6. Tiến lại gần nếu quá xa ---
    if distance > 250:
        ai.x += 2 * direction_to_player

    # --- 7. Tận dụng clone Piccolo ---
    if ai.name == 'piccolo' and ai.clone_active and distance < 150 and ai.attack_cd == 0:
        handle_melee_attack(ai, player1)
        return

    # --- 8. Đánh nếu đối thủ bị stun hoặc đang sạc ---
    if (player1.is_stunned or player1.t_transforming or player1.transforming) and distance < 70 and ai.attack_cd == 0:
        handle_melee_attack(ai, player1)
        return

    # --- 9. Dùng skill 1 nếu địch không phòng thủ ---
    if ai.skill1_cd == 0 and distance < 300:
        direction = 1 if ai.facing == 'right' else -1
        x = ai.x + 30
        y = ai.y

        # === GOHAN ===
        if ai.name == 'gohan':
            if ai.beast:
                if ai.beast_mode == 'normal':
                    bullet1 = Projectile1(x, y, direction, (150, 0, 255))
                    bullet2 = Projectile1(x + 20, y, direction, (150, 0, 255))
                    ai.projectiles1.extend([bullet1, bullet2])
                else:  # Max beast
                    for i in range(3):
                        bullet = Projectile1(x + i * 20, y, direction, (255, 50, 50))
                        ai.projectiles1.append(bullet)
            elif ai.ssj1:
                bullet = Projectile1(x, y, direction, (255, 255, 0))
                bullet.speed = 12 * direction  # tăng tốc
                ai.projectiles1.append(bullet)
                ai.next_attack_2x = True
            else:
                bullet = Projectile1(x, y, direction, (255, 255, 100))
                ai.projectiles1.append(bullet)

            ai.skill1_cd = 120
            ai.increase_ki(10)
            return

        # === BROLY ===
        elif ai.name == 'broly':
            bullet = Projectile1(x, y, direction, ai.char['skill1_color'])
            ai.projectiles1.append(bullet)
            ai.broly_quick_shot_count += 1
            if ai.broly_quick_shot_count < 4:
                ai.skill1_cd = 6  # 0.1s
                ai.increase_ki(2)
            else:
                ai.skill1_cd = 120  # 2s
                ai.increase_ki(6)
                ai.broly_quick_shot_count = 0
            return

        # === GOKU ===
        elif ai.name == 'goku':
            bullet = Projectile1(x, y, direction, ai.char['skill1_color'])  # Kame xanh
            ai.projectiles1.append(bullet)
            ai.skill1_cd = 120
            ai.increase_ki(10)
            ai.just_shot_skill1 = 10  # hiện trạng thái bắn trong 10 frame
            return
        # === GOKU MODULAR ===
        elif ai.name == 'goku_modular':
            if ai.ssj3_modular:
                bullet = Projectile1(x, y, direction, (255, 255, 0))  # Đạn vàng
            elif ai.ssj1_modular:
                bullet = Projectile1(x, y, direction, (255, 255, 0))  # Đạn vàng
            else:
                bullet = Projectile1(x, y, direction, ai.char['skill1_color'])  # Đạn xanh thường

            ai.projectiles1.append(bullet)
            ai.skill1_cd = 120
            kiblast_sound.play()
            ai.increase_ki(10)
            ai.just_shot_skill1 = 10
            kiblast_sound.play()
            return
        # === VEGETA ===
        elif ai.name == 'vegeta':
            bullet = Projectile1(x, y, direction, ai.char['skill1_color'])  # Kame vàng
            ai.projectiles1.append(bullet)
            ai.skill1_cd = 120
            ai.increase_ki(10)
            return

        # === PICCOLO ===
        elif ai.name == 'piccolo':
            bullet = Projectile1(x, y, direction, ai.char['skill1_color'])  # Masenko tím
            ai.projectiles1.append(bullet)
            ai.skill1_cd = 120
            ai.increase_ki(10)
            return



    # --- 10. Dùng skill 2 theo loại ---
    if ai.name == 'gohan':
        if ai.skill2_cd == 0:
            if ai.beast and ai.beast_mode == 'max':
                if ai.ki >= 40:
                    ai.use_ki(40)
                    ai.final_resolve_active = True
                    ai.final_resolve_timer = 300
                    ai.resolve_damage_taken = 0
                    ai.skill2_cd = 360
                    return
            elif ai.beast and ai.beast_mode == 'normal':
                if ai.ki >= 40 and distance < 100:
                    ai.use_ki(40)
                    player1.stun_timer = 60
                    ai.shield_active = True
                    ai.shield_timer = 150
                    ai.skill2_cd = 360
                    return
            else:
                if ai.ki < 80:
                    ai.use_ki(0)
                    ai.ki_regen_timer = 180
                    ai.skill2_cd = 360
                    return
    elif ai.name == 'goku_modular':
        if ai.skill2_cd == 0 and ai.ki >= 40:
            if ai.ssj3_modular:
                # Base form dùng kaioken
                ai.use_ki(40)
                ai.skill2_cd = 480
                ai.ssj3_skill2_active = True
                ai.ssj3_skill2_phase = 0
                ai.ssj3_skill2_timer = 0
                return
            elif ai.ssj1_modular:
                # SSJ1 dùng để heal
                ai.use_ki(40)
                ai.ssj1_healing = True
                ai.ssj1_heal_timer = 300
                ai.total_healed = 0
                ai.heal_tick_counter = 0
                ai.skill2_cd = 360
                kaioken_sound.play()
                return
            else:
                # Base form dùng kaioken
                ai.use_ki(40)
                ai.kaioken = True
                ai.kaioken_timer = 600
                ai.skill2_cd = 360
                kaioken_sound.play()
                return
    else:
        # các nhân vật khác giữ nguyên
        if ai.skill2_cd == 0 and ai.ki >= 40:
            if ai.skill2_type == 'buff_damage' and not ai.damage_buff:
                ai.use_ki(40)
                ai.damage_buff = True
                ai.damage_buff_timer = 180
                ai.skill2_cd = 360
                return
            elif ai.skill2_type == 'stun' and distance < 100 and not player1.defending:
                ai.use_ki(40)
                player1.stun_timer = 60
                ai.skill2_cd = 360
                return
            elif ai.skill2_type == 'heal' and ai.health < characters[ai.name]['health'] * 0.95:
                ai.use_ki(40)
                ai.health = min(ai.health + 120, characters[ai.name]['health'])
                ai.skill2_cd = 360
                return
            elif ai.skill2_type == 'berserker' and not ai.berserker_active:
                ai.use_ki(40)
                ai.berserker_active = True
                ai.berserker_timer = 240
                ai.skill2_cd = 360
                return


    # --- 11. Đánh thường khi gần ---
    if distance < 70 and ai.attack_cd == 0:
        handle_melee_attack(ai, player1)
        return

    # --- 12. Dùng ultimate nếu có thể ---
    if ai.skill5_cd == 0 and ai.ki >= 60 and distance < 50:
        if random.random() < 0.8:
            if ai.on_ground == False:return
        kaioken_sound.stop()
        kiblast_sound.stop()
        ai.charging_ultimate = True
        ai.ultimate_timer = 35
        if ai.name == 'gohan':
            # Cập nhật hiệu ứng ultimate tùy theo trạng thái
            if ai.beast:
                if ai.beast_mode == 'normal':
                    ai.ultimate_effect = 'stun_near'
                else:
                    ai.ultimate_effect = 'oneshot'
            elif ai.ssj1:
                ai.ultimate_effect = 'slow'
            else:
                ai.ultimate_effect = 'break_guard'
        return
ultimate_flashes = []
class UltimateFlash:
    def __init__(self, player_side, custom_image=None, text="KAMEHAMEHA!!!", text_color=(0, 200, 255)):
        if custom_image:
            self.image = pygame.image.load(custom_image).convert_alpha()
        else:
            self.image = pygame.image.load('img/gokueye4.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 65))
        self.side = player_side
        self.timer = 60
        self.alpha = 0
        self.text_font = pygame.font.SysFont("Arial", 20, bold=True)
        self.text = text
        self.text_color = text_color
    def draw(self, surface):
        # Làm tối background xung quanh
        dim_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dim_surface.fill((0, 0, 0, 150))  # đen, alpha 150
        surface.blit(dim_surface, (0, 0))

        # Fade-in ảnh mắt
        if self.timer > 30 and self.alpha < 255:
            self.alpha += 10
        elif self.timer <= 30:
            self.alpha = max(0, self.alpha - 10)  # fade-out nhẹ

        eye = self.image.copy()
        eye.set_alpha(self.alpha)

        x = 100 if self.side == 'left' else WIDTH - 300
        y = 100
        surface.blit(eye, (x, y))

        # Hiện chữ 
        if self.alpha > 100:
            text = self.text_font.render(self.text, True, self.text_color)
            if self.side == 'left':
                text_rect = text.get_rect(midleft=(100, (HEIGHT // 2)))
            else:
                text_rect = text.get_rect(midright=(WIDTH - 100, (HEIGHT // 2)))
            surface.blit(text, text_rect)

        self.timer -= 1
class SpiritEnergyStreak:
    def __init__(self, x, y, target_x, target_y, big=False):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.vx = (target_x - x) / 30
        self.vy = (target_y - y) / 30
        self.timer = 0
        self.big = big
        self.img = spirit_streak_big if big else spirit_streak_small
        self.active = True

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.timer += 1
        if self.timer >= 30:
            self.active = False

    def draw(self, surface):
        surface.blit(self.img, (int(self.x), int(self.y)))
class KiBall:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.frame_timer = 0
        self.frame_index = 0
        self.active = True

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 400:
            self.active = False
        self.frame_timer += 1
        if self.frame_timer >= 6:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 2
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 40, 40)  # hitbox 40x40
    def draw(self, surface):
        img = ki_ball_imgs[self.frame_index]
        surface.blit(img, (self.x, self.y))
class CloneProjectile:
    def __init__(self, x, y, direction, color=(100, 255, 100)):
        self.x = x
        self.y = y
        self.vx = 5 * direction
        self.radius = 6
        self.color = color
        self.active = True


    def move(self):
        self.x += self.vx
        if self.x < 0 or self.x > 800:
            self.active = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y + 30)), self.radius)


class Projectile:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.radius = 8
        self.vx = 7 * direction
        self.vy=-3
        self.color = color
        self.active = True
    

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # Có thể thêm logic nếu đạn bay ra khỏi màn hình thì deactivate:
        if self.x < 0 or self.x > 800:
            self.active = False
    def apply_gravity(self):
        if not self.on_ground:
            self.vel_y += 0.5  # trọng lực
            self.y += self.vel_y
            if self.y >= 250:
                self.y = 250
                self.vel_y = 0
                self.on_ground = True
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y + 30), self.radius)
class Projectile1:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.radius = 8
        self.speed = 7 * direction
        self.color = color
        self.active = True
    

    def move(self):
        self.x += self.speed
        # Có thể thêm logic nếu đạn bay ra khỏi màn hình thì deactivate:
        if self.x < 0 or self.x > 800:
            self.active = False
    def apply_gravity(self):
        if not self.on_ground:
            self.vel_y += 0.5  # trọng lực
            self.y += self.vel_y
            if self.y >= 250:
                self.y = 250
                self.vel_y = 0
                self.on_ground = True
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y + 30), self.radius)
class Projectile2:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.radius = 8
        self.vx = 7 * direction
        self.vy=3
        self.color = color
        self.active = True
    

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # Có thể thêm logic nếu đạn bay ra khỏi màn hình thì deactivate:
        if self.x < 0 or self.x > 800:
            self.active = False
    def apply_gravity(self):
        if not self.on_ground:
            self.vel_y += 0.5  # trọng lực
            self.y += self.vel_y
            if self.y >= 250:
                self.y = 250
                self.vel_y = 0
                self.on_ground = True



    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y + 30), self.radius)
class BigBeam:
    def __init__(self, x, y, direction, color, width=350, height=40, duration=30, damage=60):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.color = color
        self.duration = duration
        self.damage = damage
        self.active = True
        self.has_hit = False  # Chỉ gây damage 1 lần

    def update(self):
        self.duration -= 1
        if self.duration <= 0:
            self.active = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y + 30 - self.height // 2, self.width, self.height)


    def draw(self, surface):
        rect = self.get_rect()

        # Vẽ glow đơn giản (hình chữ nhật mờ bên ngoài)
        glow_color = (*self.color[:3], 100)  # màu có alpha
        glow_surface = pygame.Surface((rect.width + 10, rect.height + 10), pygame.SRCALPHA)
        pygame.draw.rect(glow_surface, glow_color, glow_surface.get_rect(), border_radius=30)
        surface.blit(glow_surface, (rect.x - 5, rect.y - 5))

        # Vẽ lõi beam chính
        pygame.draw.rect(surface, self.color, rect, border_radius=30)
class Player:
    def __init__(self, name, x, y, controls):
        self.shield_img_index = 0
        self.shield_img_timer = 0
        self.time_since_T = 0  # Đếm thời gian từ khi dùng T cho ai
        self.spirit_energy_streaks = []#tia năng lượng
        self.ssj3_skill2_active = False
        self.ssj3_skill2_phase = 0
        self.ssj3_skill2_timer = 0
        self.ki_ball_flash_timer = 0
        self.ki_ball_toggle = True
        self.ki_balls = []
        #aura và random thân lúc kame
        self.ssj3_gong_random_set=False
        self.ssj3_aura_timer = 0
        self.ssj3_aura_index = 0
        #ssj3 goku
        self.ssj3_modular = False
        self.ssj3_modular_timer = 0
        #ssj1 skill
        self.ssj1_healing = False
        self.ssj1_heal_timer = 0
        self.total_healed = 0
        self.heal_tick_counter = 0
        self.ssj1_heal_aura_index = 0
        self.ssj1_heal_aura_timer = 0
        #ssj1 goku
        self.ssj1_modular = False
        self.ssj1_modular_timer = 0 #ssj1 của goku
        # SSJ1 aura
        self.ssj1_aura_index = 0
        self.ssj1_aura_timer = 0
        # Kaioken aura
        self.kaioken_aura_index = 0
        self.kaioken_aura_timer = 0 #quan li thoi gian frame kaioken
        self.just_shot_skill1 = 0  # frame countdown sau khi bắn
        self.name = name
        self.char = characters[name]
        self.use_modular = (name == 'goku_modular')  # chỉ dùng modular cho goku_modular
        if self.use_modular:
            # Chân
            self.chan_dung = self.char['chan_dung']
            self.chan_danhthuong = self.char.get('chan_danhthuong')
            self.banchuong_than = self.char.get('banchuong_than')  
            self.chan_danh_index = 0
            self.chan_danh_timer = 0
            self.chan_chay = self.char['chan_chay']
            self.chan_nhay = self.char.get('nhay_chan')
            self.chan_roi = self.char.get('roi_chan')
            self.chan_index = 0
            self.chan_timer = 0  # ✅ Cái này BẮT BUỘC PHẢI CÓ
            self.chan_image = self.chan_dung
            # Thân
            self.than_dung = self.char['than_dung']
            self.danhthuong_than_list = self.char['danhthuong_than_list']
            self.danh_index = 0
            self.danh_timer = 0
            self.than_chay = self.char['than_chay']
            self.than_nhay = self.char.get('nhay_than')
            self.than_roi = self.char.get('roi_than')
            self.than_thu = self.char.get('than_thu', self.than_dung)
            self.than_index = 0
            self.than_image = self.than_dung
            # Đầu
            self.dau_dung = self.char['dau_dung']
            self.dau_chay = self.char['dau_chay']
            self.dau_image = self.dau_dung
            #ban kame
            self.gong_than = self.char['gong_than']
            self.bang_than = self.char['bang_than']
            self.bang_chan = self.char['bang_chan']
            self._ssj3_random_image = self.gong_than #biến random thân khi kame ssj3
            # Trạng thái
            self.moving_right = False
            self.moving_left = False
        # Broly
        self.lssj_left = self.char.get('lssj_left', self.char['left'])
        self.lssj_right = self.char.get('lssj_right', self.char['right'])
        self.ssj4_left = self.char.get('ssj4_left', self.char['left'])
        self.ssj4_right = self.char.get('ssj4_right', self.char['right'])

        self.khi7_left = self.char.get('khi7_left', self.char['left'])
        self.khi7_right = self.char.get('khi7_right', self.char['right'])
        # Goku
        self.kaioken_left = self.char.get('kaioken_left', self.char['left'])
        self.kaioken_right = self.char.get('kaioken_right', self.char['right'])

        # Vegeta
        self.khi1_left = self.char.get('khi1_left', self.char['left'])
        self.khi1_right = self.char.get('khi1_right', self.char['right'])

        # Piccolo
        self.pcl1_left = self.char.get('pcl1_left', self.char['left'])
        self.pcl1_right = self.char.get('pcl1_right', self.char['right'])
        self.image_left = self.char['left']
        self.image_right = self.char['right']
        self.facing = 'right'
        # Thêm tốc độ di chuyển gốc
        self.speed = 3
        self.original_speed = self.speed

        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.controls = controls
        self.health = self.char['health']
        self.damage = self.char['damage']
        self.skill2_type = self.char['skill2']
        self.skill1_cd = 0
        self.skill2_cd = 0
        self.skill3_cd = 0
        self.skill4_cd = 0
        self.is_stunned = False
        self.damage_buff = False
        self.heal_effect_timer = 0
        self.stun_timer = 0
        self.attack_cd = 0
        self.damage_buff = False
        self.damage_buff_timer = 0  # thời gian buff còn lại, tính bằng ticks (60 = 1 giây)
        self.next_attack_2x = False #tang x2 dame
        self.projectiles = []
        self.projectiles1=[]
        self.projectiles2=[]
        self.y = 250  # Cố định vị trí
        self.vel_y = 0
        self.on_ground = True
        self.ki = 0
        self.max_ki = 100
        self.defending = False
        self.dash_timer = 0  # Cooldown dash
        self.khi7 = False
        self.transforming = False
        self.transform_timer = 0
        self.khi7_duration = 0       # Thời gian còn lại trong trạng thái khi7 (tính bằng ticks)
        self.khi7_cooldown = 0       # Thời gian hồi chiêu sau khi kết thúc khi7
        self.ui = False
        self.ui_duration = 0
        self.ui_cooldown = 0
        self.pclo_transform = False
        self.pclo_duration = 0
        self.pclo_cooldown = 0
        self.clone_active = False
        self.clone_timer = 0

        self.heal_tick_counter = 0
        self.total_healed = 0

        self.big_beams = []
        self.charging_ultimate = False
        self.ultimate_timer = 0
        self.skill5_cd = 0  # Cooldown chiêu ultimate
        self.skill6_cd = 0
        # Goku - Kaioken
        self.kaioken = False
        self.kaioken_timer = 0

        # Piccolo - Khiên phản sát thương
        self.shield_active = False
        self.shield_timer = 0

        # Vegeta - Hồi sinh & hút máu
        self.vegeta_resurrect = False
        self.vegeta_invincible_timer = 0
        self.vegeta_lifesteal = 0.0

        self.shield_immune_timer = 0
        self.vegeta_lifesteal_timer = 0
    
        self.used_T = False  # Đã dùng T để cho phép dùng O
        self.t_transforming = False
        self.t_transform_timer = 0

        self.vegeta_resurrect_count = 0
        self.hit_recently = 0  # số lần bị đánh trúng gần đây

        self.clone_projectiles = []
        self.clone_shoot_timer = 0

        # Broly T & O
        self.lssj_active = False
        self.lssj_timer = 0
        self.lssj_bonus = 0

        self.recording_hp = 0
        self.can_use_ssj4 = False
        self.ssj4_active = False
        self.ssj4_timer = 0
        self.rage_timer = 0

        self.berserker_active = False
        self.berserker_timer = 0

        self.ssj4_cd = 0

        self.broly_quick_shot_count = 0

        # Gohan
        self.ssj1 = False
        self.ssj1_timer = 0

        self.beast = False
        self.beast_timer = 0
        self.beast_mode = None  # 'normal' hoặc 'max'

        self.last_skill1_hit_time = 0  # Để combo với skill2
        self.final_resolve_active = False
        self.resolve_damage_taken = 0
        self.final_resolve_timer = 0

        self.slow_timer = 0
        self.ki_regen_timer = 0  # Thời gian còn lại để hồi KI mỗi giây (dùng cho Focus Ki)
        self.skill_cooldown_factor = 1.0 #cooldown
         
        self.beast_cooldown = 0
        self.maxbeast_cooldown = 0

    def apply_gravity(self):
        if not self.on_ground:
            self.vel_y += 0.5  # trọng lực
            self.y += self.vel_y
            if self.y >= 250:
                self.y = 250
                self.vel_y = 0
                self.on_ground = True

    def move(self, keys):
        if self.is_stunned:
            return
        if self.ssj3_skill2_active:return
        if keys[self.controls['left']] and self.x > 0:
            if self.transforming:return
            self.x -= 3
            self.facing = 'left'
        if keys[self.controls['right']] and self.x < 800 - self.width:
            if self.transforming:return
            self.x += 3
            self.facing = 'right'

        if keys[self.controls['jump']] and self.on_ground:
            if self.transforming:return
            self.vel_y = -10
            self.on_ground = False
        if self.use_modular:
            if self.transforming:return
            self.moving_right = keys[self.controls['right']]
            self.moving_left = keys[self.controls['left']]
    def apply_gravity(self):
        if not self.on_ground:
            self.vel_y += 0.5
            self.y += self.vel_y
            if self.y >= 250:
                self.y = 250
                self.vel_y = 0
                self.on_ground = True

    def increase_ki(self, amount):
        self.ki += amount
        if self.ki > self.max_ki:
            self.ki = self.max_ki

    def use_ki(self, amount):
        if self.name == 'piccolo' and self.pclo_transform:
            return True
        if self.ki >= amount:
            self.ki -= amount
            return True
        return False
    def vegeta_lifesteal_heal(self, damage):
        if self.name == 'vegeta' and self.vegeta_lifesteal > 0 and damage > 0:
            heal = int(damage * self.vegeta_lifesteal)
            self.health = min(self.health + heal, characters['vegeta']['health'])
    
    def cooldown_tick(self):
        # Nếu đã dùng T mà chưa lên SSJ3 thì tăng bộ đếm
        if self.name == 'goku_modular' and self.used_T and not self.ssj3_modular:
            self.time_since_T += 1
        for streak in self.spirit_energy_streaks:
            streak.update()
        self.spirit_energy_streaks = [b for b in self.spirit_energy_streaks if b.active]
        if self.ssj3_skill2_active:
            self.ssj3_skill2_timer += 1
            # --- PHASE 0: Bay từ từ lên ---
            if self.ssj3_skill2_phase == 0:
                gonggenki_sound.play()
                self.on_ground = False
                self.vel_y = -3  # bay lên nhẹ như nhảy
                self.y += self.vel_y
                self.chan_image = self.char['ssj3_nhay_chan']
                self.than_image = self.char['ssj3_than_nhay']
                self.dau_image  = self.char['ssj3_dau_dung']
                if self.y <= 150:
                    self.y = 150
                    self.vel_y = 0
                    self.ssj3_skill2_phase = 1
                    self.ssj3_skill2_timer = 0
            elif self.ssj3_skill2_phase == 1:
                self.vel_y = 0
                self.y = 150
                # Giai đoạn chuẩn bị bay lên và tạo cầu
                self.than_image = self.char['ssj3_skill2_prepare']
                self.chan_image = self.char['ssj3_roi_chan']
                # Hiệu ứng nhấp nháy cầu
                self.ki_ball_flash_timer += 1
                if self.ki_ball_flash_timer >= 5:
                    self.ki_ball_flash_timer = 0
                    self.ki_ball_toggle = not self.ki_ball_toggle
                # Spawn streaks (ngẫu nhiên 10%)
                if random.random() < 0.2:
                    sx = self.x + random.randint(-250, 250)
                    sy = self.y + random.randint(-140, 140)
                    tx = self.x + 30  # giữa quả cầu
                    ty = self.y - 35
                    big = random.random() < 0.2
                    self.spirit_energy_streaks.append(SpiritEnergyStreak(sx, sy, tx, ty, big))
                if self.ssj3_skill2_timer >= 90:
                    self.ssj3_skill2_phase = 2
                    self.ssj3_skill2_timer = 0

            elif self.ssj3_skill2_phase == 2:
                self.vel_y = 0
                self.y = 150
                if random.random() < 0.2:
                    sx = self.x + random.randint(-250, 250)
                    sy = self.y + random.randint(-140, 140)
                    tx = self.x + 30  # giữa quả cầu
                    ty = self.y - 35
                    big = random.random() < 0.2
                    self.spirit_energy_streaks.append(SpiritEnergyStreak(sx, sy, tx, ty, big))
                # Đổi thân thành rơi
                self.than_image = self.char['ssj3_than_roi']
                # Hiệu ứng nhấp nháy cầu
                self.ki_ball_flash_timer += 1
                if self.ki_ball_flash_timer >= 5:
                    self.ki_ball_flash_timer = 0
                    self.ki_ball_toggle = not self.ki_ball_toggle
                if self.ssj3_skill2_timer >= 30:
                    self.ssj3_skill2_phase = 3
                    self.ssj3_skill2_timer = 0
                    gonggenki_sound.stop()

            elif self.ssj3_skill2_phase == 3:
                nemgenki_sound.play()
                self.vel_y = 0
                self.y = 150
                # Đổi sang gồng và ném 
                enemy = player2 if self == player1 else player1
                self.than_image = self.char['ssj3_gong_than']
                if self.ssj3_skill2_timer == 10:
                    target_x = enemy.x + enemy.width // 2
                    target_y = enemy.y 
                    dx = target_x - self.x
                    dy = target_y - self.y
                    distance = math.sqrt(dx**2 + dy**2)
                    speed = 10
                    vx = speed * (dx / distance)
                    vy = speed * (dy / distance)
                    ball = KiBall(self.x + 30, self.y, vx, vy)
                    self.ki_balls.append(ball)
                if self.ssj3_skill2_timer >= 30:
                    self.ssj3_skill2_active = False
                    self.apply_gravity()
                    self.shield_active=True
                    self.shield_timer=120
        # ssj1 goku hoi mau
        if self.ssj1_healing:
            self.ssj1_heal_timer -= 1
            self.heal_tick_counter += 1
            if self.health>=580:
                self.shield_active=True
                self.shield_timer=120
            # Hồi máu mỗi giây
            if self.heal_tick_counter >= 60:
                self.heal_tick_counter = 0
                if self.total_healed < 250:
                    self.health = min(self.health + 50, self.char['health'])
                    self.total_healed += 50

            # # Ngắt sớm nếu bị làm gián đoạn
            if self.moving_left or self.moving_right or self.attack_cd > 0 or not self.on_ground or self.charging_ultimate:
                if self.total_healed >= 125:
                    self.ssj1_healing = False
                    self.shield_active=True
                    self.shield_timer=300
                    kaioken_sound.stop()
                else :
                    self.health = min(self.health + 100, self.char['health'])
                    self.ssj1_healing = False
                    self.shield_active=True
                    self.shield_timer=360
                    kaioken_sound.stop()
            # Kết thúc khi đủ thời gian hoặc hồi đủ
            if self.ssj1_heal_timer <= 0 or self.total_healed >= 250:
                self.ssj1_healing = False
                kaioken_sound.stop()

        if self.hit_recently > 0:
            self.hit_recently -= 1
        if self.skill1_cd > 0:
            self.skill1_cd -= self.skill_cooldown_factor
            if self.skill1_cd < 0:
                self.skill1_cd = 0
        if self.skill4_cd > 0:
            self.skill4_cd -= self.skill_cooldown_factor
            if self.skill4_cd < 0:
                self.skill4_cd = 0
        if self.skill3_cd > 0:
            self.skill3_cd -= self.skill_cooldown_factor
            if self.skill3_cd < 0:
                self.skill3_cd = 0
        if self.skill2_cd > 0:
            self.skill2_cd -= self.skill_cooldown_factor
            if self.skill2_cd < 0:
                self.skill2_cd = 0
        if self.skill5_cd > 0:
            self.skill5_cd -= self.skill_cooldown_factor
            if self.skill5_cd < 0:
                self.skill5_cd = 0
        if self.dash_timer > 0:  # 👈 Thêm dòng này
            self.dash_timer -= 1
        if self.skill6_cd > 0:
            self.skill6_cd -= self.skill_cooldown_factor
            if self.skill6_cd < 0:
                self.skill6_cd = 0
        if self.vegeta_lifesteal_timer > 0:
            self.vegeta_lifesteal_timer -= 1
        else:
            self.vegeta_lifesteal = 0
        if self.ssj1_modular:
            self.ssj1_modular_timer -= 1
            if self.ssj1_modular_timer <= 0:
                self.ssj1_modular = False
                self.ssj1_healing = False
                kaioken_sound.stop()
        if self.kaioken:
            self.kaioken_timer -= 1
            if self.kaioken_timer % 60 == 0:
                if self.ui:
                    self.health -= 0  # Goku đang ở UI → giảm máu ít hơn
                else:
                    self.health -= 3  # Goku thường → trừ máu bình thường

            if self.kaioken_timer <= 0:
                self.kaioken = False
                kaioken_sound.stop()
                heal_amount = 50 if self.health < 100 else 30
                self.health = min(self.health + heal_amount, self.char['health'])

        if self.shield_active:
            self.shield_img_timer += 1
            if self.shield_img_timer >= 6:  
                self.shield_img_index = (self.shield_img_index + 1) % len(khien_imgs)
                self.shield_img_timer = 0
            self.shield_timer -= 1
            if self.shield_immune_timer > 0:
                self.shield_immune_timer -= 1
            if self.shield_timer <= 0:
                self.shield_active = False

        if self.vegeta_invincible_timer > 0:
            self.vegeta_invincible_timer -= 1
            if self.vegeta_invincible_timer <= 0:
                self.vegeta_resurrect = False
        if self.vegeta_resurrect and self.vegeta_invincible_timer <= 0:
            self.vegeta_lifesteal = 0
        if self.ssj4_cd > 0:
            self.ssj4_cd -= 1
        if self.beast_cooldown > 0:
            self.beast_cooldown -= 1
        if self.maxbeast_cooldown > 0:
            self.maxbeast_cooldown -= 1

        if self.slow_timer > 0:
            self.slow_timer -= 1
            self.speed = self.original_speed * 0.5
        else:
            self.speed = self.original_speed

        # Quản lý thời gian bị stun
        if self.stun_timer > 0:
            self.stun_timer -= 1
            self.is_stunned = True  # Nếu còn thời gian stun
        else:
            self.is_stunned = False  # Hết stun thì được di chuyển

        # Hồi chiêu đánh thường
        # Hồi chiêu đánh thường (Broly tăng tốc khi berserk)
        if self.attack_cd > 0:
            if self.name == 'broly' and self.lssj_active:
                self.attack_cd -= 2  # tăng tốc gấp đôi
            else:
                self.attack_cd -= 1
            if self.attack_cd < 0:
                self.attack_cd = 0
        if self.berserker_active:
            self.berserker_timer -= 1
            if self.berserker_timer <= 0:
                self.berserker_active = False

        # Focus Ki: hồi 10 KI mỗi giây trong 3 giây
        if self.ki_regen_timer > 0:
            self.ki_regen_timer -= 1
            if self.ki_regen_timer % 60 == 0:  # mỗi 1 giây
                self.increase_ki(10)

        # Quản lý thời gian buff damage
        if self.damage_buff_timer > 0:
            self.damage_buff_timer -= 1
        else:
            self.damage_buff = False
    def draw_ki_bar(self, surface):
        bar_x = self.x
        bar_y = self.y - 10
        bar_width = 60
        bar_height = 8

        # Vẽ viền thanh KI
        pygame.draw.rect(surface, (0, 0, 0), (bar_x - 1, bar_y - 1, bar_width + 2, bar_height + 2), 1)

        # Vẽ nền thanh KI màu xám
        pygame.draw.rect(surface, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))

        # Tính tỷ lệ KI
        ki_ratio = self.ki / self.max_ki

        # Vẽ thanh KI màu xanh dương
        pygame.draw.rect(surface, (0, 0, 255), (bar_x, bar_y, int(bar_width * ki_ratio), bar_height))
    def draw(self):
        if self.use_modular:
            if self.ssj3_modular:
                self.chan_dung = self.char.get('ssj3_chan_dung')
                self.chan_chay = self.char.get('ssj3_chan_chay')
                self.chan_danhthuong = self.char.get('ssj3_chan_danhthuong')
                self.chan_nhay = self.char.get('ssj3_nhay_chan')
                self.chan_roi = self.char.get('ssj3_roi_chan')

                self.than_dung = self.char.get('ssj3_than_dung')
                self.than_chay = self.char.get('ssj3_than_chay')
                self.danhthuong_than_list = self.char.get('ssj3_danhthuong_than_list')
                self.than_nhay = self.char.get('ssj3_than_nhay')
                self.than_roi = self.char.get('ssj3_than_roi')
                self.than_thu = self.char.get('ssj3_than_thu')

                self.dau_dung = self.char.get('ssj3_dau_dung')
                self.dau_chay = self.char.get('ssj3_dau_chay')

                self.gong_than = self.char.get('ssj3_gong_than')
                self.bang_than = self.char.get('ssj3_bang_than')
                self.banchuong_than = self.char.get('ssj3_banchuong_than')
                self.bang_chan = self.char.get('ssj3_bang_chan')

            # Nếu đang ở trạng thái SSJ1 → thay toàn bộ asset
            elif self.ssj1_modular:
                self.chan_dung = self.char.get('ssj1_chan_dung')
                self.chan_chay = self.char.get('ssj1_chan_chay')
                self.chan_danhthuong = self.char.get('ssj1_chan_danhthuong')
                self.chan_nhay = self.char.get('ssj1_nhay_chan')
                self.chan_roi = self.char.get('ssj1_roi_chan')

                self.than_dung = self.char.get('ssj1_than_dung')
                self.than_chay = self.char.get('ssj1_than_chay')
                self.danhthuong_than_list = self.char.get('ssj1_danhthuong_than_list')
                self.than_nhay = self.char.get('ssj1_than_nhay')
                self.than_roi = self.char.get('ssj1_than_roi')
                self.than_thu = self.char.get('ssj1_than_thu')

                self.dau_dung = self.char.get('ssj1_dau_dung')
                self.dau_chay = self.char.get('ssj1_dau_chay')

                self.gong_than = self.char.get('ssj1_gong_than')
                self.bang_than = self.char.get('ssj1_bang_than')
                self.banchuong_than = self.char.get('ssj1_banchuong_than')
                self.bang_chan = self.char.get('ssj1_bang_chan')
            else:
                self.chan_dung = self.char.get('chan_dung')
                self.chan_chay = self.char.get('chan_chay')
                self.chan_danhthuong = self.char.get('chan_danhthuong')
                self.chan_nhay = self.char.get('nhay_chan')
                self.chan_roi = self.char.get('roi_chan')

                self.than_dung = self.char.get('than_dung')
                self.than_chay = self.char.get('than_chay')
                self.danhthuong_than_list = self.char.get('danhthuong_than_list')
                self.than_nhay = self.char.get('nhay_than')
                self.than_roi = self.char.get('roi_than')
                self.than_thu = self.char.get('than_thu')

                self.dau_dung = self.char.get('dau_dung')
                self.dau_chay = self.char.get('dau_chay')

                self.gong_than = self.char.get('gong_than')
                self.bang_than = self.char.get('bang_than')
                self.banchuong_than = self.char.get('banchuong_than')
                self.bang_chan = self.char.get('bang_chan')
            # Animation chạy
            if self.moving_right or self.moving_left:
                self.chan_timer += 1
                if self.chan_timer >= 8:
                    self.chan_index = (self.chan_index + 1) % len(self.chan_chay)
                    self.than_index = (self.than_index + 1) % len(self.than_chay)
                    self.chan_timer = 0

            # === CHỌN ẢNH TÙY THEO TRẠNG THÁI ===
            if self.transforming:
                self.chan_image = self.bang_chan
                self.than_image = self.than_nhay
                self.dau_image = self.dau_dung
            elif self.ssj3_skill2_active:
                self.chan_image = self.chan_image  # giữ nguyên
                self.than_image = self.than_image  # giữ nguyên
                self.dau_image = self.dau_image
            elif self.ssj1_healing:
                self.chan_image = self.bang_chan
                self.than_image = self.than_nhay
                self.dau_image = self.dau_dung
            elif self.defending:
                self.chan_image = self.bang_chan
                self.than_image = self.than_thu
                self.dau_image = self.dau_dung
            elif self.charging_ultimate:
                # Đang gồng beam (H bị giữ)
                self.chan_image = self.bang_chan
                if self.ssj3_modular:
                    if not self.ssj3_gong_random_set:
                        self._ssj3_random_image = random.choice([
                            self.char['ssj3_gong_than'],  
                            self.char['ssj3_than_roi'],  
                        ])
                        self.ssj3_gong_random_set = True
                    self.than_image = self._ssj3_random_image
                else:
                    self.than_image = self.gong_than
                self.dau_image = self.dau_dung
            elif self.attack_cd > 0:
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.danh_timer += 1
                    if self.danh_timer >= 20:  # 20 frame thì đổi ảnh đấm 1 lần
                        self.danh_index = (self.danh_index + 1) % len(self.danhthuong_than_list)
                        self.danh_timer = 0
                    if self.danh_index == 1:
                        # dùng chân đá khi chuẩn bị đấm
                        self.chan_danh_timer += 1
                        if self.chan_danh_timer >= 10:
                            self.chan_danh_index = (self.chan_danh_index + 1) % len(self.chan_danhthuong)
                            self.chan_danh_timer = 0
                        self.chan_image = self.chan_danhthuong[self.chan_danh_index]
                        self.dau_image = self.dau_dung
                    else:
                        self.chan_image = self.bang_chan
                        self.dau_image = self.dau_chay
                    self.than_image = self.danhthuong_than_list[self.danh_index]
                    if self.danh_index == 1:
                        self.dau_image = self.dau_dung
                    else:
                        self.dau_image = self.dau_chay
                else:
                    self.danh_timer += 1
                    if self.danh_timer >= 10:  # 20 frame thì đổi ảnh đấm 1 lần
                        self.danh_index = (self.danh_index + 1) % len(self.danhthuong_than_list)
                        self.danh_timer = 0
                    if self.danh_index == 1:
                        # dùng chân đá khi chuẩn bị đấm
                        self.chan_danh_timer += 1
                        if self.chan_danh_timer >= 5:
                            self.chan_danh_index = (self.chan_danh_index + 1) % len(self.chan_danhthuong)
                            self.chan_danh_timer = 0
                        self.chan_image = self.chan_danhthuong[self.chan_danh_index]
                        self.dau_image = self.dau_dung
                    else:
                        self.chan_image = self.bang_chan
                        self.dau_image = self.dau_chay
                    self.than_image = self.danhthuong_than_list[self.danh_index]
                    if self.danh_index == 1:
                        self.dau_image = self.dau_dung
                    else:
                        self.dau_image = self.dau_chay
            elif self.just_shot_skill1 > 0:
                self.chan_image = self.bang_chan  
                self.than_image = self.banchuong_than
                self.dau_image = self.dau_dung
            elif self.big_beams and not self.charging_ultimate:
                # Beam vừa bắn ra → dùng ảnh beam
                self.chan_image = self.bang_chan
                self.than_image = self.bang_than
                self.dau_image = self.dau_dung
            elif not self.on_ground:
                # Nhảy hoặc rơi
                if self.vel_y < 0:
                    # Đang nhảy lên
                    self.chan_image = self.chan_nhay
                    self.than_image = self.than_nhay
                else:
                    # Đang rơi xuống
                    self.chan_image = self.chan_roi
                    self.than_image = self.than_roi
                self.dau_image = self.dau_dung
            elif self.moving_right or self.moving_left:
                self.chan_image = self.chan_chay[self.chan_index]
                self.than_image = self.than_chay[self.than_index]
                self.dau_image = self.dau_chay
            else:
                self.chan_image = self.chan_dung
                self.than_image = self.than_dung
                self.dau_image = self.dau_dung

            # === FLIP TRÁI PHẢI ===
            if self.facing == 'left':
                chan_img = pygame.transform.flip(self.chan_image, True, False)
                than_img = pygame.transform.flip(self.than_image, True, False)
                dau_img = pygame.transform.flip(self.dau_image, True, False)
            else:
                chan_img = self.chan_image
                than_img = self.than_image
                dau_img = self.dau_image

            # === VỊ TRÍ VẼ ===
            chan_rect = chan_img.get_rect(midbottom=(self.x+18 + chan_img.get_width() // 2, self.y + self.height-5))
            # --- Offset điều chỉnh vị trí ảnh thân ---
            # === CHỌN OFFSET THEO THÂN ===
            if self.than_image == self.char['ssj3_skill2_prepare']:
                offset_than_y = 10
                offset_than_x = 0
            elif self.than_image == self.gong_than:
                if self.ssj3_skill2_active:
                    offset_than_y = 8
                    offset_than_x = 3
                elif self.ssj3_modular:
                    offset_than_y = 2
                    offset_than_x = 3
                elif self.ssj1_modular:
                    offset_than_y = 2
                    offset_than_x = 3
                else:
                    offset_than_y = 3
                    offset_than_x = 4
            elif self.than_image == self.bang_than:
                if self.ssj3_modular:
                    offset_than_y = 1.2
                    offset_than_x = 8
                elif self.ssj1_modular:
                    offset_than_y = 1.2
                    offset_than_x = 8
                else:
                    offset_than_y = 1
                    offset_than_x = 6
            elif self.than_image == self.char['danhthuong_than_list'][1]:  # chayphaithan.png
                if self.chan_image== self.char['chan_danhthuong'][0]:
                    offset_than_y = 9.5
                    offset_than_x = -7
                elif self.chan_image == self.char['chan_danhthuong'][1]:
                    offset_than_y = 1
                    offset_than_x = 2
            elif self.than_image == self.char['danhthuong_than_list'][0]:  # danhthuong1.png
                offset_than_y = 1
                offset_than_x = 7
            elif self.than_image == self.char['ssj1_danhthuong_than_list'][1]:  # chayphaithan.png
                if self.chan_image== self.char['ssj1_chan_danhthuong'][0]:
                    offset_than_y = 9.5
                    offset_than_x = -7
                elif self.chan_image == self.char['ssj1_chan_danhthuong'][1]:
                    offset_than_y = 1
                    offset_than_x = 2
            elif self.than_image == self.char['ssj1_danhthuong_than_list'][0]:  # danhthuong1.png
                offset_than_y = 1
                offset_than_x = 7
            elif self.than_image == self.char['ssj3_danhthuong_than_list'][1]:  # ssj3chayphaithan.png
                if self.chan_image== self.char['ssj3_chan_danhthuong'][0]:
                    offset_than_y = 9.5
                    offset_than_x = -7
                elif self.chan_image == self.char['ssj3_chan_danhthuong'][1]:
                    offset_than_y = 1
                    offset_than_x = 2
            elif self.than_image == self.char['ssj3_danhthuong_than_list'][0]:  # ssj3danhthuong1.png
                offset_than_y = 1
                offset_than_x = 8
            elif self.than_image == self.than_thu:
                if self.ssj3_modular:
                    offset_than_y = 1.5
                    offset_than_x = 3.5
                elif self.ssj1_modular:
                    offset_than_y = 3
                    offset_than_x = 3.5
                else:
                    offset_than_y = 3  
                    offset_than_x = 3  
            elif self.than_image == self.than_nhay:
                if self.ssj1_healing or self.transforming:
                    offset_than_y = 0.5   
                    offset_than_x = 0.5
                elif self.ssj1_modular:
                    offset_than_y = 3.5
                    offset_than_x = -3
                else:
                    offset_than_y = 2.5
                    offset_than_x = -3
            elif self.than_image == self.than_roi:
                if self.ssj3_modular and self.charging_ultimate:
                    offset_than_y = 2  
                    offset_than_x = -2
                elif self.ssj3_modular:
                    offset_than_y = 6.5  
                    offset_than_x = -2
                elif self.ssj1_modular:
                    offset_than_y = 3.5  
                    offset_than_x = -3
                else:
                    offset_than_y = 2
                    offset_than_x = -3
            elif self.than_image == self.banchuong_than:
                if self.ssj3_modular:
                    offset_than_y = 4.5    
                    offset_than_x = 5
                else:
                    offset_than_y = 4    
                    offset_than_x = 5       
            else:
                if self.ssj3_modular:
                    offset_than_y = 1.5 if (self.moving_right or self.moving_left) else 4.5
                    offset_than_x = 0
                else:
                    offset_than_y = 1.5 if (self.moving_right or self.moving_left) else 6
                    offset_than_x = 0
            # Nếu đang quay trái, đảo hướng offset ngang
            if self.facing == 'left':
                offset_than_x = -offset_than_x
            than_rect = than_img.get_rect(midbottom=(
                chan_rect.midtop[0] + offset_than_x,
                chan_rect.midtop[1] + offset_than_y
            ))
            # === DỊCH ĐẦU  ===
            offset_dau_x = 0
            if self.than_image == self.char['ssj3_skill2_prepare']:
                offset_dau_y = 29
                offset_dau_x = -8
            elif self.than_image == self.than_thu:
                if self.ssj3_modular:
                    offset_dau_y = 15
                    offset_dau_x = -6.5
                elif self.ssj1_modular:
                    offset_dau_y = 5.5
                    offset_dau_x = -2.2
                else:
                    offset_dau_y = 5.5
                    offset_dau_x = -1.2
            elif self.than_image == self.char['danhthuong_than_list'][1]:  
                if self.chan_image== self.char['chan_danhthuong'][0]:
                    offset_dau_y = 3
                    offset_dau_x = 1
                elif self.chan_image == self.char['chan_danhthuong'][1]:
                    offset_dau_y = 4
                    offset_dau_x = 3
            elif self.than_image == self.char['danhthuong_than_list'][0]:  
                offset_dau_x = -4.7
                offset_dau_y = 4.5
            elif self.than_image == self.char['ssj1_danhthuong_than_list'][1]:  
                if self.chan_image== self.char['ssj1_chan_danhthuong'][0]:
                    offset_dau_y = 3
                    offset_dau_x = 1
                elif self.chan_image == self.char['ssj1_chan_danhthuong'][1]:
                    offset_dau_y = 4
                    offset_dau_x = 3
            elif self.than_image == self.char['ssj1_danhthuong_than_list'][0]:  
                offset_dau_x = -4.7
                offset_dau_y = 4.5
            elif self.than_image == self.char['ssj3_danhthuong_than_list'][1]:  
                if self.chan_image== self.char['ssj3_chan_danhthuong'][0]:
                    offset_dau_y = 10.5
                    offset_dau_x = -3
                elif self.chan_image == self.char['ssj3_chan_danhthuong'][1]:
                    offset_dau_y = 12.5
                    offset_dau_x = -2
            elif self.than_image == self.char['ssj3_danhthuong_than_list'][0]:  
                offset_dau_x = -10.5
                offset_dau_y = 12.5
            elif self.than_image == self.than_nhay:
                if self.ssj3_modular:
                    offset_dau_x = -2
                    offset_dau_y = 18.5
                elif self.ssj1_healing or self.transforming:
                    offset_dau_x = 2.5
                    offset_dau_y = 11.5
                else:
                    offset_dau_x = 2
                    offset_dau_y = 11
            elif self.than_image == self.than_roi:
                if self.ssj3_modular:
                    offset_dau_x = -2.5
                    offset_dau_y = 25.5
                elif self.ssj1_modular:
                    offset_dau_x = 2  
                    offset_dau_y = 16.7  
                else:
                    offset_dau_x = 2
                    offset_dau_y = 16.7
            elif self.than_image == self.banchuong_than:
                if self.ssj3_modular:
                    offset_dau_x = -9
                    offset_dau_y = 14
                elif self.ssj1_modular:
                    offset_dau_x = -6.5
                    offset_dau_y = 5.5
                else:
                    offset_dau_x = -6.5
                    offset_dau_y = 6
            elif self.ssj3_skill2_active and self.than_image == self.gong_than:
                    offset_dau_y = 15
                    offset_dau_x = -3.8
            elif self.charging_ultimate:
                if self.ssj3_modular:
                    offset_dau_y = 14.5
                    offset_dau_x = -2.5
                elif self.ssj1_modular:
                    offset_dau_y = 5.5
                    offset_dau_x = 2
                else:
                    offset_dau_y = 7  # cúi đầu khi gồng
            elif self.big_beams:
                if self.ssj3_modular:
                    offset_dau_y = 14.5
                    offset_dau_x = -10.5
                elif self.ssj1_modular:
                    offset_dau_y = 6
                    offset_dau_x = -5
                else:
                    offset_dau_y = 6  # cúi nhẹ đầu khi bắn
                    offset_dau_x = -4
            else:
                if self.ssj3_modular:
                    offset_dau_y=11.5
                    offset_dau_x=-3.8
                else:
                    offset_dau_y = 3  # bình thường
            if self.facing == 'left':
                offset_dau_x = -offset_dau_x
            dau_rect = dau_img.get_rect(midbottom=(
                than_rect.midtop[0] + offset_dau_x,
                than_rect.midtop[1] + offset_dau_y
            ))

            # === VẼ MODULAR ===
            # Hiệu ứng hào quang Kaioken cho modular
            if self.transforming:
                # Hào quang (ảnh lớn)
                aura_list = self.char.get('ssj1_heal_aura', [])
                self.ssj1_heal_aura_timer += 1
                if self.ssj1_heal_aura_timer >= 4:
                    self.ssj1_heal_aura_index = (self.ssj1_heal_aura_index + 1) % len(aura_list)
                    self.ssj1_heal_aura_timer = 0
                aura_img = aura_list[self.ssj1_heal_aura_index]
                aura_img = pygame.transform.flip(aura_img, True, False) if self.facing == 'left' else aura_img
                aura_rect = aura_img.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2 - 25))
                screen.blit(aura_img, aura_rect.topleft)
                for _ in range(8):  # thử vẽ 4 tia sét mỗi frame
                    if random.random() < 0.05:  # 50% xác suất 1 tia sét hiện ra
                        lightning_img = random.choice(ssj3_lightning_imgs)
                        lightning = lightning_img.copy()
                        lightning.set_alpha(random.randint(255,255))
                        offset_x = random.randint(-30, 50)
                        offset_y = random.randint(-30,30)
                        for _ in range(25):  # hoặc 3 nếu cần
                            screen.blit(lightning, (self.x + offset_x, self.y + offset_y))
            if self.kaioken:
                aura_list = self.char.get('kaioken_aura')
                self.kaioken_aura_timer += 1
                if self.kaioken_aura_timer >= 6:  # 6 frame đổi ảnh
                    self.kaioken_aura_index = (self.kaioken_aura_index + 1) % len(aura_list)
                    self.kaioken_aura_timer = 0
                aura_img = aura_list[self.kaioken_aura_index]
                aura_img = pygame.transform.flip(aura_img, True, False) if self.facing == 'left' else aura_img
                aura_rect = aura_img.get_rect(center=(self.x + self.width // 2 , self.y + self.height // 2 - 12))
                screen.blit(aura_img, aura_rect.topleft)
            if self.ssj1_modular and self.ssj1_healing:
                # Hào quang (ảnh lớn)
                aura_list = self.char.get('ssj1_heal_aura', [])
                self.ssj1_heal_aura_timer += 1
                if self.ssj1_heal_aura_timer >= 4:
                    self.ssj1_heal_aura_index = (self.ssj1_heal_aura_index + 1) % len(aura_list)
                    self.ssj1_heal_aura_timer = 0
                aura_img = aura_list[self.ssj1_heal_aura_index]
                aura_img = pygame.transform.flip(aura_img, True, False) if self.facing == 'left' else aura_img
                aura_rect = aura_img.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2 - 25))
                screen.blit(aura_img, aura_rect.topleft)
            if self.ssj1_modular:
                aura_list = self.char.get('ssj1_aura')
                self.ssj1_aura_timer += 1
                if self.ssj1_aura_timer >= 5:
                    self.ssj1_aura_index = (self.ssj1_aura_index + 1) % len(aura_list)
                    self.ssj1_aura_timer = 0
                aura_img = aura_list[self.ssj1_aura_index]
                aura_img = pygame.transform.flip(aura_img, True, False) if self.facing == 'left' else aura_img
                aura_rect = aura_img.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2 - 18))
                screen.blit(aura_img, aura_rect.topleft)
            if self.ssj3_modular:
                aura_list = self.char.get('ssj3_aura')
                self.ssj3_aura_timer += 1
                if self.ssj3_aura_timer >= 6:
                    self.ssj3_aura_index = (self.ssj3_aura_index + 1) % len(aura_list)
                    self.ssj3_aura_timer = 0
                aura_img = aura_list[self.ssj3_aura_index]
                aura_img = pygame.transform.flip(aura_img, True, False) if self.facing == 'left' else aura_img
                aura_rect = aura_img.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2 - 25))
                screen.blit(aura_img, aura_rect)
            if self.ssj3_modular:
                if self.ssj3_skill2_active:
                    for _ in range(8):  # thử vẽ 4 tia sét mỗi frame
                        if random.random() < 0.05:  # 50% xác suất 1 tia sét hiện ra
                            lightning_img = random.choice(ssj3_lightning_imgs)
                            lightning = lightning_img.copy()
                            lightning.set_alpha(random.randint(255,255))
                            offset_x = random.randint(-30, 50)
                            offset_y = random.randint(-30,30)
                            for _ in range(25):  # hoặc 3 nếu cần
                                screen.blit(lightning, (self.x + offset_x, self.y + offset_y))
                else:
                    for _ in range(4):  # thử vẽ 4 tia sét mỗi frame
                        if random.random() < 0.01:  # 50% xác suất 1 tia sét hiện ra
                            lightning_img = random.choice(ssj3_lightning_imgs)
                            lightning = lightning_img.copy()
                            lightning.set_alpha(random.randint(150,255))
                            offset_x = random.randint(-20, 40)
                            offset_y = random.randint(-20,20)
                            for _ in range(10):  # hoặc 3 nếu cần
                                screen.blit(lightning, (self.x + offset_x, self.y + offset_y))
            screen.blit(chan_img, chan_rect.topleft)
            screen.blit(dau_img, dau_rect.topleft)
            screen.blit(than_img, than_rect.topleft)
            
            # ✅ VẼ BEAM nếu có
            for beam in self.big_beams:
                beam.draw(screen)
            # ✅ HIỆU ỨNG CHO MODULAR 
            if self.is_stunned:
                if (pygame.time.get_ticks() // 150) % 2 == 0:
                    temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                    temp_surface.fill((255, 0, 0, 180))  # đỏ nhạt, trong suốt
                    screen.blit(temp_surface, (self.x, self.y))
            if self.t_transforming:
                if (pygame.time.get_ticks() // 100) % 2 == 0:
                    temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                    temp_surface.fill((255, 255, 0, 180))  # màu vàng nhấp nháy chẳng hạn
                    screen.blit(temp_surface, (self.x, self.y))
            if self.transforming:
                if (pygame.time.get_ticks() // 100) % 2 == 0:
                    temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                    temp_surface.fill((255, 255, 0, 180))  # màu vàng nhấp nháy chẳng hạn
                    screen.blit(temp_surface, (self.x, self.y))
            # --- Nếu đang ở chiêu SSJ3 Skill2 Phase 1: hiển thị 2 quả cầu đồng tâm ---
            if self.ssj3_skill2_active and self.ssj3_skill2_phase in [1,2]:
                img = ki_ball_imgs[0] if self.ki_ball_toggle else ki_ball_imgs[1]
                # Vẽ 2 quả cầu chồng lên nhau (trung điểm trên đầu)
                center_x = self.x + 30
                center_y = self.y - 70
                screen.blit(img, (center_x - img.get_width() // 2, center_y))
                screen.blit(img, (center_x - img.get_width() // 2 , center_y + 3))  # lệch nhẹ tạo hiệu ứng glow
            # Vẽ streaks cho Spirit Bomb
            if self.ssj3_modular and self.ssj3_skill2_active and self.ssj3_skill2_phase in [1, 2]:
                for streak in self.spirit_energy_streaks:
                    streak.draw(screen)
            if self.shield_active:
                khien_img = khien_imgs[self.shield_img_index]
                if khien_img!= khien_imgs[0]:
                    screen.blit(khien_img, (self.x - 21, self.y - 17))
                else:
                    screen.blit(khien_img, (self.x - 6, self.y - 3))
            return  # Kết thúc nếu là modular


        sprite = self.get_current_image()
        sprite_w, sprite_h = sprite.get_width(), sprite.get_height()
        offset_x = (sprite_w - self.width) // 2
        offset_y = (sprite_h - self.height) // 2
        draw_x = self.x - offset_x
        draw_y = self.y - offset_y
        if self.t_transforming:
            if (pygame.time.get_ticks() // 100) % 2 == 0:
                if self.name == 'goku':
                    color = (255, 0, 0, 180)
                elif self.name == 'vegeta':
                    color = (255, 255, 0, 180)
                elif self.name == 'piccolo':
                    color = (200, 100, 200, 180)
                elif self.name == 'broly':
                    color = (0, 255, 100, 180)  # xanh lá sáng – màu đặc trưng Broly
                elif self.name == 'gohan':
                    color = (255,255,0,180)
                else:
                    color = (255, 255, 255, 180)  # fallback màu trắng

                temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                temp_surface.fill(color)
                screen.blit(sprite, (draw_x, draw_y))
                screen.blit(temp_surface, (self.x, self.y))
            else:
                screen.blit(sprite, (draw_x, draw_y))
            return  # Không vẽ lại nữa, tránh đè lên

        # Nhấp nháy màu khi biến hình
        if self.transforming:
            if (pygame.time.get_ticks() // 100) % 2 == 0:
                # Goku nháy trắng, Vegeta nháy vàng
                if self.name == 'goku':
                    color = (200, 255, 255, 180)  
                elif self.name == 'vegeta':
                    color = (255,255,255, 180)  
                elif self.name == 'piccolo':
                    color = (255, 165, 0, 180)  # Tím nhấp nháy cho Piccolo
                elif self.name == 'broly':
                    color = (255, 0, 0, 180)  # xanh lá sáng – màu đặc trưng Broly
                elif self.name == 'gohan':
                    if self.health >= 0.4 * characters['gohan']['health']:
                        color = (150, 0, 255, 180)  # màu beast thường
                    else:
                        color = (255, 50, 100, 180)  # màu MAX beast
                else:
                    color = (255, 255, 255, 180)  # fallback màu trắng

                temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                temp_surface.fill(color)
                screen.blit(sprite, (draw_x, draw_y))
                screen.blit(temp_surface, (self.x, self.y))
            else:
                screen.blit(sprite, (draw_x, draw_y))
        else:
            screen.blit(sprite, (draw_x, draw_y))
        if self.clone_active:
            # Vẽ clone hơi lệch trái/phải một chút để tránh đè lên player
            clone_offset = 80
            clone_x = self.x + clone_offset-60 if self.facing == 'right' else self.x - clone_offset +35
            clone_xx = self.x - clone_offset+35 if self.facing == 'right' else self.x + clone_offset -60

            # Sử dụng đúng ảnh clone riêng của Piccolo
            if self.name == 'piccolo':
                clone_image = self.pcl1_right if self.facing == 'right' else self.pcl1_left
            else:
                clone_image = self.get_current_image()

            screen.blit(clone_image, (clone_x, self.y))
            screen.blit(clone_image, (clone_xx, self.y))
        # Hiệu ứng buff hoặc phòng thủ vẫn giữ nguyên
        if self.damage_buff:
            pygame.draw.rect(screen, (0, 255, 255), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 3)
        if self.defending:
            pygame.draw.rect(screen, (100, 100, 255), (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 3)
        if self.kaioken:
            pygame.draw.rect(screen, (255, 0, 0), (self.x - 3, self.y - 3, self.width + 6, self.height + 6), 2)
        if self.shield_active:
            color = (0, 255, 0)
            width = 4 if self.shield_immune_timer > 0 else 2
            pygame.draw.rect(screen, color, (self.x - 7, self.y - 7, self.width + 14, self.height + 14), width)
        # === Hiệu ứng viền Broly khi biến hình ===
        if self.name == 'broly':
            if self.lssj_active:
                pygame.draw.rect(screen, (0, 255, 100), (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 2)
            if self.ssj4_active:
                pygame.draw.rect(screen, (255, 100, 0), (self.x - 6, self.y - 6, self.width + 12, self.height + 12), 3)
        if self.name == 'gohan':
            if self.ssj1:
                pygame.draw.rect(screen, (255, 255, 50), (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 2)
            if self.beast and self.beast_mode == 'normal':
                pygame.draw.rect(screen, (150, 0, 255), (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 3)
            if self.beast and self.beast_mode == 'max':
                pygame.draw.rect(screen, (255, 50, 100), (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 3)
            if self.final_resolve_active:
                pygame.draw.rect(screen, (255, 255, 255), (self.x - 6, self.y - 6, self.width + 12, self.height + 12), 2)

        # === Rage Pulse hiệu ứng sóng tròn ===
        if self.name == 'broly' and self.ssj4_active:
            if self.rage_timer <= 20:  # Vẽ sóng ngay khi pulse
                center_x = self.x + self.width // 2
                center_y = self.y + self.height // 2
                radius = 60 + self.rage_timer * 2
                pygame.draw.circle(screen, (255, 50, 50), (center_x, center_y), radius, 2)

        if self.name == 'broly' and self.berserker_active:
            pygame.draw.rect(screen, (255, 0, 255), (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 2)

        if self.vegeta_resurrect:
            pygame.draw.rect(screen, (255, 255, 0), (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 3)
        if self.is_stunned:
            if (pygame.time.get_ticks() // 150) % 2 == 0:
                temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                temp_surface.fill((255, 0, 0, 180))  # đỏ nhạt, trong suốt
                screen.blit(sprite, (draw_x, draw_y))  # sprite gốc
                screen.blit(temp_surface, (self.x, self.y))  # phủ màu lên
            else:
                screen.blit(sprite, (draw_x, draw_y))  # không nhấp nháy
        else:
            screen.blit(sprite, (draw_x, draw_y))  # bình thường
        for beam in self.big_beams:
            beam.draw(screen)
        if self.vegeta_lifesteal > 0:
            pygame.draw.rect(screen, (255, 255, 0), (self.x - 6, self.y - 6, self.width + 12, self.height + 12), 2)

    def transform_ssj(self):
        if self.name == 'vegeta' and self.used_T and not self.khi7 and not self.transforming and self.khi7_cooldown==0:
            if self.ki >= 50:
                self.use_ki(50)
                self.transforming = True
                self.transform_timer = 60  # nháy khoảng 1 giây (60 frame)
    def transform_ui(self):
        if self.name == 'goku' and self.used_T and not self.ui and not self.transforming and self.ui_cooldown == 0:
            if self.ki >= 50:
                self.use_ki(50)
                self.transforming = True
                self.transform_timer = 60  # Nhấp nháy 1 giây trước khi biến
    def transform_pclo(self):
        if self.name == 'piccolo' and self.used_T and not self.pclo_transform and not self.transforming and self.pclo_cooldown == 0:
            if self.ki >= 50:
                self.use_ki(50)
                self.transforming = True
                self.transform_timer = 60  # nháy 1 giây trước khi bật
    def transform_ssj4(self):
        if self.name == 'broly' and self.used_T and not self.ssj4_active and not self.transforming and self.ssj4_cd == 0:
            if self.ki >= 50 and self.can_use_ssj4:
                self.use_ki(50)
                self.transforming = True
                self.transform_timer = 60  # 1 giây nhấp nháy
    def transform_beast_upgrade(self):
        if self.name == 'gohan' and self.used_T and not self.beast and not self.transforming and self.ki >= 50:
            self.use_ki(50)
            self.transforming = True
            self.transform_timer = 60
            if self.health >= 0.4 * characters['gohan']['health']:
                self.beast_mode = 'normal'
            else:
                self.beast_mode = 'max'
    def transform_ssj3(self):
        if self.name == 'goku_modular' and self.used_T and not self.ssj3_modular and not self.transforming and self.ki >= 50:
            self.use_ki(50)
            self.transforming = True
            self.transform_timer = 180
            self.defending=True
            self.ki_regen_timer=180
            kaioken_sound.stop()
            ssj3_sound.play()
    def update_state(self):
        if self.name == 'goku':
            self.update_goku_state()
        elif self.name == 'vegeta':
            self.update_vegeta_state()
        elif self.name == 'piccolo':
            self.update_piccolo_state()
        elif self.name == 'broly':
            self.update_broly_state()
        elif self.name == 'gohan':
            self.update_gohan_state()
        elif self.name == 'goku_modular':
            self.update_goku_modular_state()  
    def update_goku_state(self):
        if self.t_transforming:
            self.t_transform_timer -= 1
            if self.t_transform_timer <= 0:
                self.t_transforming = False
                self.used_T = True
                self.kaioken = True
                self.kaioken_timer = 360
                self.skill6_cd = 900

        if self.transforming:
            self.transform_timer -= 1
            if self.transform_timer <= 0:
                self.transforming = False
                self.ui = True
                self.ui_duration = 360
                self.ui_cooldown = 900

        if self.ui:
            self.ui_duration -= 1
            if self.ui_duration <= 0:
                self.ui = False
                self.used_T = False
    
        if self.ui_cooldown > 0:
            self.ui_cooldown -= 1
        if self.charging_ultimate:
            self.ultimate_timer -= 1
            if self.ultimate_timer <= 0:
                self.charging_ultimate = False
                self.use_ki(60)
                self.skill5_cd = 900
                direction = 1 if self.facing == 'right' else -1

                color = (0, 200, 255)
                dmg = 40
                height = 70
                offset = self.width if direction == 1 else -350

                beam = BigBeam(self.x + offset, self.y, direction, color, height=height, damage=dmg)
                self.big_beams.append(beam)
    def update_goku_modular_state(self):
        # Xử lý hiệu ứng bắn beam
        if self.just_shot_skill1 > 0:
            self.just_shot_skill1 -= 1
        if self.t_transforming:
            self.t_transform_timer -= 1
            if self.t_transform_timer <= 0:
                self.t_transforming = False
                self.used_T = True
                self.ssj1_modular = True
                ssj1_sound.play()
                if self is player1:
                    ultimate_flashes.append(UltimateFlash(
                        'left',
                        custom_image="img/ssj1_flash.png",
                        text="SUPER SAIYAN!!",
                        text_color=(255, 255, 0)
                    ))
                else:
                    ultimate_flashes.append(UltimateFlash(
                        'right',
                        custom_image="img/ssj1_flash.png",
                        text="SUPER SAIYAN!!",
                        text_color=(255, 255, 0)
                    ))
                self.ssj1_modular_timer = 600  # SSJ1 kéo dài 6 giây
                self.skill6_cd = 900
        if self.transforming:
            self.transform_timer -= 1
            if self.transform_timer <= 0:
                ssj3_sound.stop()
                ssj1_sound.play()
                kaioken_sound.play()
                if self is player1:
                    ultimate_flashes.append(UltimateFlash(
                        'left',
                        custom_image="img/ssj3_flash.jpg",
                        text="SUPER SAIYAN 3!!",
                        text_color=(255, 255, 0)
                    ))
                else:
                    ultimate_flashes.append(UltimateFlash(
                        'right',
                        custom_image="img/ssj3_flash.jpg",
                        text="SUPER SAIYAN 3!!",
                        text_color=(255, 255, 0)
                    ))
                self.transforming = False
                if self.name == 'goku_modular':
                    self.ssj3_modular = True
                    self.ssj3_modular_timer = 900
                    self.health += 150
        if self.ssj3_modular:
            self.ssj3_modular_timer -= 1
            if self.ssj3_modular_timer <= 0:
                self.ssj3_modular = False
                self.used_T=False
                self.health -= 100
                kaioken_sound.stop()
        # Ultimate (bắn beam giống Goku)
        if self.charging_ultimate:
            self.ultimate_timer -= 1
            if self.ultimate_timer == 19:
                genki_sound.stop()
                gonggenki_sound.stop()
                kiblast_sound.stop()
                sound_kame_charge.play()
            if self.ultimate_timer <= 0:
                self.charging_ultimate = False
                self.ssj3_gong_random_set = False
                self.use_ki(50)
                self.skill5_cd = 700
                direction = 1 if self.facing == 'right' else -1

                if self.name == 'goku_modular':
                    side = 'left' if self is player1 else 'right'
                    ultimate_flashes.append(UltimateFlash(side))
                if self.ssj3_modular:
                    beam_color = (255, 250, 0)      
                    beam_height = 70                
                    beam_damage = 130               
                elif self.ssj1_modular:
                    beam_color = (255, 255, 0)
                    beam_height = 60         
                    beam_damage = 100        
                else:
                    beam_color = (0, 200, 255)
                    beam_height = 40
                    beam_damage = 70

                beam = BigBeam(
                    self.x + (self.width if direction == 1 else -350),
                    self.y,
                    direction,
                    beam_color,
                    height=beam_height,
                    damage=beam_damage
                )
                self.big_beams.append(beam)
                sound_kame_charge.stop()
                sound_kame_shoot.play()

    def update_vegeta_state(self):
        if self.t_transforming:
            self.t_transform_timer -= 1
            if self.t_transform_timer <= 0:
                self.t_transforming = False
                self.used_T = True
                if self.health <= 0:
                    self.vegeta_resurrect = True
                    self.vegeta_invincible_timer = 120
                    self.vegeta_lifesteal = 1.0
                    self.vegeta_lifesteal_timer = 120
                else:
                    max_hp = characters['vegeta']['health']
                    self.vegeta_lifesteal = 0.4 if self.health > 0.5 * max_hp else 0.6
                    self.vegeta_lifesteal_timer = 240
                    self.vegeta_resurrect = False
                self.skill6_cd = 1200

        if self.transforming:
            self.transform_timer -= 1
            if self.transform_timer <= 0:
                self.transforming = False
                self.khi7 = True
                self.khi7_duration = 300 
                self.damage += 10
                self.health += 100

        if self.khi7:
            self.khi7_duration -= 1
            if self.khi7_duration <= 0:
                self.khi7 = False
                self.khi7_cooldown = 900
                self.damage -= 10
                self.health -= 100
                self.used_T = False

        if self.khi7_cooldown > 0:
            self.khi7_cooldown -= 1
        if self.charging_ultimate:
            self.ultimate_timer -= 1
            if self.ultimate_timer <= 0:
                self.charging_ultimate = False
                self.use_ki(60)
                self.skill5_cd = 900
                direction = 1 if self.facing == 'right' else -1

                color = (255, 255, 0)
                dmg = 50
                height = 100
                offset = self.width if direction == 1 else -350

                beam = BigBeam(self.x + offset, self.y, direction, color, height=height, damage=dmg)
                self.big_beams.append(beam)

    def update_piccolo_state(self):
        if self.t_transforming:
            self.t_transform_timer -= 1
            if self.t_transform_timer <= 0:
                self.t_transforming = False
                self.used_T = True
                self.shield_active = True
                self.shield_timer = 360
                self.shield_immune_timer = 120
                self.skill6_cd = 1200

        if self.transforming:
            self.transform_timer -= 1
            if self.transform_timer <= 0:
                self.transforming = False
                self.pclo_transform = True
                self.pclo_transform_timer = 300
                self.pclo_cooldown = 900
                self.clone_active = False
                self.used_T = False
                self.clone_timer = 0
                self.total_healed = 0
                self.heal_tick_counter = 0

        if self.pclo_transform:
            self.pclo_transform_timer -= 1
            if not self.clone_active:
                self.clone_active = True
                self.clone_timer = 180
            else:
                self.clone_timer -= 1
                if self.clone_timer <= 0:
                    self.clone_active = False

            self.heal_tick_counter += 1
            if self.heal_tick_counter >= 60 and self.total_healed < 100:
                self.health += 20
                self.total_healed += 20
                self.heal_tick_counter = 0

            if self.pclo_transform_timer <= 0:
                self.pclo_transform = False
                self.clone_active = False

        if self.pclo_transform and self.clone_active:
            self.clone_shoot_timer += 1
            if self.clone_shoot_timer >= 90:
                self.clone_shoot_timer = 0
                direction = 1 if self.facing == 'right' else -1
                clone1 = CloneProjectile(self.x - 20, self.y - 20, direction, color=(200, 0, 200))
                clone2 = CloneProjectile(self.x + 80, self.y - 20, direction, color=(200, 0, 200))
                self.clone_projectiles.extend([clone1, clone2])

        if self.pclo_cooldown > 0:
            self.pclo_cooldown -= 1
        if self.charging_ultimate:
            self.ultimate_timer -= 1
            if self.ultimate_timer <= 0:
                self.charging_ultimate = False
                self.use_ki(60)
                self.skill5_cd = 900
                direction = 1 if self.facing == 'right' else -1

                color = (200, 0, 200)
                dmg = 90
                height = 12
                offset = self.width if direction == 1 else -350

                beam = BigBeam(self.x + offset, self.y, direction, color, height=height, damage=dmg)
                self.big_beams.append(beam)

    def update_broly_state(self):
        if self.t_transforming:
            self.t_transform_timer -= 1
            if self.t_transform_timer <= 0:
                self.t_transforming = False
                self.used_T = True
                self.lssj_active = True
                self.lssj_timer = 360
                self.lssj_bonus = 0
                self.skill6_cd = 1200
                self.hp_when_used_T = self.health

        if self.lssj_active:
            self.lssj_timer -= 1
            if self.lssj_timer <= 0:
                self.lssj_active = False
                self.lssj_bonus = 0
            else:
                self.defending = False

        if self.used_T and not self.ssj4_active:
            if self.health < self.hp_when_used_T:
                self.recording_hp = self.hp_when_used_T - self.health
                self.can_use_ssj4 = True

        if self.transforming:
            self.transform_timer -= 1
            if self.transform_timer <= 0:
                self.transforming = False
                hp_lost = self.recording_hp
                radius = max(60, int(hp_lost * 0.2))
                damage = max(30, int(hp_lost * 0.6))
                self.health += int(hp_lost * 0.5)
                self.damage += 10
                self.ssj4_active = True
                self.ssj4_timer = 600
                self.rage_timer = 0
                self.ssj4_cd = 1200

                for target in [player1, player2]:
                    if target is not self:
                        explosion_area = pygame.Rect(self.x - radius, self.y - radius, radius * 2, radius * 2)
                        target_rect = pygame.Rect(target.x, target.y, target.width, target.height)
                        if explosion_area.colliderect(target_rect):
                            target.health -= damage

        if self.ssj4_active:
            self.ssj4_timer -= 1
            if self.ssj4_timer <= 0:
                self.ssj4_active = False
            else:
                self.rage_timer += 1
                if self.rage_timer >= 120:
                    self.rage_timer = 0
                    # Gây sát thương quanh – xử lý bên ngoài loop

        if self.berserker_active:
            self.berserker_timer -= 1
            if self.berserker_timer <= 0:
                self.berserker_active = False
        if self.charging_ultimate:
            self.ultimate_timer -= 1
            if self.ultimate_timer <= 0:
                self.charging_ultimate = False
                self.use_ki(60)
                self.skill5_cd = 900
                direction = 1 if self.facing == 'right' else -1

                color = (0, 255, 100)
                dmg = 80
                height = 80
                offset = self.width if direction == 1 else -350

                beam = BigBeam(self.x + offset, self.y, direction, color, height=height, damage=dmg)
                self.big_beams.append(beam)

    def update_gohan_state(self):

        if self.t_transforming:
            self.t_transform_timer -= 1
            if self.t_transform_timer <= 0:
                self.t_transforming = False
                self.used_T = True
                self.ssj1 = True
                self.skill_cooldown_factor = 2  # giảm 50% cooldown
                self.ssj1_timer = 360
                self.damage += 8
                self.skill6_cd = 1200

        if self.transforming:
            self.transform_timer -= 1
            if self.transform_timer <= 0:
                self.transforming = False
                if self.beast_mode is not None:
                    self.beast = True
                    self.beast_timer = 600
                    if self.beast_mode == 'normal':
                        self.health += 80
                        self.damage += 8
                        self.beast_cooldown = 900  # 15 giây
                    else:
                        self.health += 150
                        self.damage += 15
                        self.maxbeast_cooldown = 600  # 10 giây



        if self.ssj1:
            self.ssj1_timer -= 1
            if self.ssj1_timer <= 0:
                self.ssj1 = False
                self.damage -= 8
                self.skill_cooldown_factor = 1.0

        if self.beast:
            self.beast_timer -= 1
            if self.beast_timer <= 0:
                if self.beast_mode == 'normal':
                    self.damage -= 8
                    self.health -= 50  # 👈 thêm hình phạt
                    if self.health < 1:
                        self.health = 1  # tránh chết luôn
                elif self.beast_mode == 'max':
                    self.health -= 100  # 👈 thêm hình phạt
                    self.damage -= 15
                    if self.health < 1:
                        self.health = 1  # tránh chết luôn
                self.beast = False
                self.beast_mode = None
                self.used_T = False

        if self.final_resolve_active:
            self.final_resolve_timer -= 1
            if self.final_resolve_timer <= 0:
                self.final_resolve_active = False
                for target in [player1,player2]:
                    if target != self and abs(self.x - target.x) < 150:
                        target.health -= int(self.resolve_damage_taken * 0.6)  # phản 60%
                self.health = min(self.health + int(self.resolve_damage_taken * 0.4), characters[self.name]["health"])  # hồi lại 40%
                self.resolve_damage_taken = 0

        # ✅ Beam xử lý cuối cùng trong hàm này:
        if self.charging_ultimate:
            self.ultimate_timer -= 1
            if self.ultimate_timer <= 0:
                self.charging_ultimate = False
                self.use_ki(60)
                self.skill5_cd = 900
                direction = 1 if self.facing == 'right' else -1

                if self.beast:
                    if self.beast_mode == 'normal':
                        color = (100, 0, 255)
                        dmg = 90
                        height = 45
                        self.ultimate_effect = 'stun_near'
                    else:
                        color = (200, 0, 100)
                        dmg = 90
                        height = 80
                        self.ultimate_effect = ['stun_near', 'oneshot']
                elif self.ssj1:
                    color = (255, 200, 50)
                    dmg = 55
                    height = 35
                    self.ultimate_effect = 'slow'
                else:
                    color = (100, 255, 200)
                    dmg = 40
                    height = 30
                    self.ultimate_effect = 'break_guard'

                offset = self.width if direction == 1 else -350
                beam = BigBeam(self.x + offset, self.y, direction, color, height=height, damage=dmg)
                beam.effect = self.ultimate_effect
                self.big_beams.append(beam)

    def get_current_image(self):
        if self.name == 'broly':
            if self.ssj4_active:
                return self.ssj4_right if self.facing == 'right' else self.ssj4_left
            elif self.lssj_active:
                return self.lssj_right if self.facing == 'right' else self.lssj_left
            else:
                return self.image_right if self.facing == 'right' else self.image_left

        if self.name == 'goku':
            if self.ui:  # Goku UI
                return self.char['ui_right'] if self.facing == 'right' else self.char['ui_left']
            elif self.kaioken:  # Kaioken
                return self.kaioken_right if self.facing == 'right' else self.kaioken_left
            else:
                return self.image_right if self.facing == 'right' else self.image_left

        if self.name == 'vegeta':
            if self.khi7:  # Oozaru
                return self.khi7_right if self.facing == 'right' else self.khi7_left
            elif self.vegeta_lifesteal_timer > 0:  # Khi1 đang hoạt động
                return self.khi1_right if self.facing == 'right' else self.khi1_left
            else:
                return self.image_right if self.facing == 'right' else self.image_left

        if self.name == 'piccolo':
            if self.pclo_transform:  # Orange
                return self.char['pclo_right'] if self.facing == 'right' else self.char['pclo_left']
            elif self.shield_timer > 0:  # Dạng T
                return self.pcl1_right if self.facing == 'right' else self.pcl1_left
            else:
                return self.image_right if self.facing == 'right' else self.image_left
        if self.name == 'gohan':  # 👈 THÊM ĐOẠN NÀY
            if self.beast:
                if self.beast_mode == 'max':
                    return self.char['maxbeast_right'] if self.facing == 'right' else self.char['maxbeast_left']
                else:
                    return self.char['beast_right'] if self.facing == 'right' else self.char['beast_left']
            elif self.ssj1:
                return self.char['ssj1_right'] if self.facing == 'right' else self.char['ssj1_left']
            else:
                return self.image_right if self.facing == 'right' else self.image_left
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.health = self.char['health']
        self.ki = 0
        self.projectiles = []
        self.projectiles1 = []
        self.projectiles2 = []
        self.facing = 'right'
        # Thêm tốc độ di chuyển gốc
        self.speed = 3
        self.original_speed = self.speed

        self.vel_y = 0
        self.on_ground = True
        self.skill1_cd = 0
        self.skill2_cd = 0
        self.skill3_cd = 0
        self.skill4_cd = 0
        self.is_stunned = False
        self.damage_buff = False
        self.heal_effect_timer = 0
        self.stun_timer = 0
        self.attack_cd = 0
        self.damage_buff_timer = 0
        self.defending = False
        self.dash_timer = 0
        self.khi7 = False
        self.transforming = False
        self.transform_timer = 0
        self.khi7_duration = 0
        self.khi7_cooldown = 0
        self.ui = False
        self.ui_duration = 0
        self.ui_cooldown = 0
        self.pclo_transform = False
        self.pclo_duration = 0
        self.pclo_cooldown = 0
        self.clone_active = False
        self.clone_timer = 0
        self.heal_tick_counter = 0
        self.total_healed = 0
        self.skill6_cd = 0

        # Goku - Kaioken
        self.kaioken = False
        self.kaioken_timer = 0

        # Piccolo - Khiên phản sát thương
        self.shield_active = False
        self.shield_timer = 0

        # Vegeta - Hồi sinh & hút máu
        self.vegeta_resurrect = False
        self.vegeta_invincible_timer = 0
        self.vegeta_lifesteal = 0.0
        self.shield_immune_timer = 0

        self.used_T = False
        self.t_transforming = False
        self.t_transform_timer = 0

        self.vegeta_resurrect_count = 0

        self.hit_recently = 0

        self.clone_projectiles = []
        self.clone_shoot_timer = 0

        # Broly T & O
        self.lssj_active = False
        self.lssj_timer = 0
        self.lssj_bonus = 0

        self.recording_hp = 0
        self.can_use_ssj4 = False
        self.ssj4_active = False
        self.ssj4_timer = 0
        self.rage_timer = 0

        self.berserker_active = False
        self.berserker_timer = 0

        self.ssj4_cd = 0

        self.broly_quick_shot_count = 0

        # Gohan
        self.ssj1 = False
        self.ssj1_timer = 0

        self.beast = False
        self.beast_timer = 0
        self.beast_mode = None  # 'normal' hoặc 'max'

        self.last_skill1_hit_time = 0  # Để combo với skill2
        self.final_resolve_active = False
        self.resolve_damage_taken = 0
        self.final_resolve_timer = 0

        self.slow_timer = 0
        self.ki_regen_timer = 0  # Thời gian còn lại để hồi KI mỗi giây (dùng cho Focus Ki)
        self.skill_cooldown_factor = 1.0

        self.beast_cooldown = 0
        self.maxbeast_cooldown = 0
        #goku_modular
        #aura và random thân lúc kame
        self.ssj3_gong_random_set=False
        self.ssj3_aura_timer = 0
        self.ssj3_aura_index = 0
        #ssj3 goku
        self.ssj3_modular = False
        self.ssj3_modular_timer = 0
        #ssj1 skill
        self.ssj1_healing = False
        self.ssj1_heal_timer = 0
        self.total_healed = 0
        self.heal_tick_counter = 0
        self.ssj1_heal_aura_index = 0
        self.ssj1_heal_aura_timer = 0
        #ssj1 goku
        self.ssj1_modular = False
        self.ssj1_modular_timer = 0 #ssj1 của goku
        # SSJ1 aura
        self.ssj1_aura_index = 0
        self.ssj1_aura_timer = 0
        # Kaioken aura
        self.kaioken_aura_index = 0
        self.kaioken_aura_timer = 0 #quan li thoi gian frame kaioken
        self.just_shot_skill1 = 0  # frame countdown sau khi bắn

font = pygame.font.SysFont(None, 32)
fontt= pygame.font.SysFont(None,17)
def draw_text(text, x, y):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (x, y))
def draw_text1(text,x,y):
    imgg = fontt.render(text, True, (0,0,0))
    screen.blit(imgg ,(x,y))
def draw_instructions():
    screen.blit(bg, (0, 0))  # Vẽ background

    # Vẽ nền mờ dưới phần text
    overlay = pygame.Surface((800, 400))
    overlay.set_alpha(190)
    overlay.fill((255, 255, 255))
    screen.blit(overlay, (0, 0))

    # Tiêu đề
    draw_text1("HUONG DAN CHOI", 320, 10)

    x1, x2 = 40, 430
    lines = [
        ("- Player 1:", "- Player 2:"),
        ("Di chuyen: A/D | Nhay: K | Danh: J | DASH: L", "Left/Right|Nhay: Num2|Danh: Num1|DASH: Num0"),
        ("Skill: U, I(40mana), W, Y", "Skill: Num4, Num5(40mana), Up, Num6"),
        ("Phong thu: S (Giam 50% dame)", "Down (Giam 50% dame)"),
        ("Ultimate: H (60 mana)", "Num8 (60 mana)"),
        ("DAC BIET: O(50mana), T(50mana)", "Num7(50mana), Num9(50mana)"),
        ("Goku: O - GOKU UI (90% ne don)", "Num7 - GOKU UI"),
        ("Vegeta: O - OOZARU (+HP +DAME)", "Num7 - OOZARU"),
        ("Piccolo: O - ORANGE (+HP/s +2 clone)", "Num7 - ORANGE"),
        ("Broly: O - SSJ4 (Tang giap va hoi mau,phan dame)", "Num7 - SSJ4"),
        ("Gohan: O - Beast/Max Beast (HP/dame,Skill manh)", "Num7 - Beast"),
        ("T - KAIOKEN (Tru mau + tang dame)", "Num9 - KAIOKEN"),
        ("T - Bat tu 2s, hut mau theo %", "Num9 - Bat tu + hut mau theo %"),
        ("T - Bat tu 2s dau / 4s phan sat thuong", "Num9 - 2s dau / 4s phan sat thuong"),
        ("T - Tang dame theo sat thuong ganh chiu...", "Num9 - Legendary super saiyan"),
        ("T - Giam cooldown skill , tang toc danh , buff damage","Num9 - Super saiyan 2"),
    ]

    for i, (left, right) in enumerate(lines):
        draw_text1(left, x1, 30 + i * 20)
        draw_text1(right, x2, 30 + i * 20)

    draw_text1("Nhan ENTER de tiep tuc", 290, 360)
def draw_character_info():
    screen.blit(bg, (0, 0))  # Nen
    overlay = pygame.Surface((800, 400))
    overlay.set_alpha(200)
    overlay.fill((255, 255, 255))
    screen.blit(overlay, (0, 0))

    draw_text1("THONG TIN NHAN VAT", 320, 20)

    infos = [
        {
            "name": "GOKU",
            "stat": "HP: 360 | Damage: 10",
            "desc": [
                "Goku co mau trung binh, dame thap.",
                "Kaioken giup tang dame nhung tru mau moi giay.",
                "Goku UI ne 90% don trong 5s.",
                "Phu hop voi choi ky nang, ne don va phan cong."
            ]
        },
        {
            "name": "VEGETA",
            "stat": "HP: 300 | Damage: 15",
            "desc": [
                "Sat thuong cao nhat, mau thap.",
                "Oozaru tang HP va dame trong 5s.",
                "Hoi sinh va hut mau neu dung dung luc.",
                "Thich hop danh lien tuc, ap dao doi thu."
            ]
        },
        {
            "name": "PICCOLO",
            "stat": "HP: 440 | Damage: 8",
            "desc": [
                "Mau cao nhat, dame thap nhat.",
                "Hoi mau manh va co 2 phan than ho tro.",
                "Co khien phan dame khi phong thu.",
                "Tot cho phong thu va danh lau dai."
            ]
        },
        {
            "name": "BROLY",
            "stat": "HP: 400 | Damage: 12",
            "desc": [
                "Can bang giua mau va dame.",
                "LSSJ: tang dame khi bi danh hoac danh trung.",
                "SSJ4: hoi mau + no AOE + gay sat thuong vung.",
                "Choi theo kieu bao luc, khong che rong."
            ]
        },
        {
            "name": "GOHAN",
            "stat": "HP: 380 | Damage: 10",
            "desc": [
                "Bien hinh tuy theo % HP.",
                "SSJ1: giam thoi gian hoi chiêu, ban nhanh.",
                "Beast: co khien, dan doi, beam lam cham.",
                "Max Beast: dame to, phan sat thuong, ket lieu."
            ]
        }
    ]

    y = 50
    for char in infos[:3]:
        draw_text1(f"{char['name']}   |   {char['stat']}", 50, y)
        y += 25
        for line in char["desc"]:
            draw_text1(line, 60, y)
            y += 20
        y += 5  # khoang cach giua cac nhan vat
    y = 50
    for char in infos[3:]:
        draw_text1(f"{char['name']}   |   {char['stat']}", 420, y)
        y += 25
        for line in char["desc"]:
            draw_text1(line,430, y)
            y += 20
        y += 5  # khoang cach giua cac nhan vat
    draw_text1("Nhan ENTER de xem huong dan choi", 450, 320)

def draw_cooldowns(player, x, y):
    offset = 0

    def write(text):
        nonlocal offset
        draw_text1(text, x, y + offset)
        offset += 20

    if player.skill1_cd > 0:
        write(f"U: {player.skill1_cd // 60}s")
    if player.skill2_cd > 0:
        write(f"I: {player.skill2_cd // 60}s")
    if player.skill3_cd > 0:
        write(f"W: {player.skill3_cd // 60}s")
    if player.skill4_cd > 0:
        write(f"Y: {player.skill4_cd // 60}s")
    if player.skill5_cd > 0:
        write(f"ULT: {player.skill5_cd // 60}s")
    if player.skill6_cd > 0:
        write(f"T: {player.skill6_cd // 60}s")

    if player.name == 'vegeta' and player.khi7_cooldown > 0:
        write(f"OOZARU: {player.khi7_cooldown // 60}s")
    if player.name == 'goku' and player.ui_cooldown > 0:
        write(f"GOKU UI: {player.ui_cooldown // 60}s")
    if player.name == 'piccolo' and player.pclo_cooldown > 0:
        write(f"NAMEK: {player.pclo_cooldown // 60}s")
    if player.name == 'broly' and player.ssj4_cd > 0:
        write(f"SSJ4: {player.ssj4_cd // 60}s")
    if player.name == 'gohan':
        if player.beast_cooldown > 0:
            write(f"Beast: {player.beast_cooldown // 60}s")
        if player.maxbeast_cooldown > 0:
            write(f"MAX Beast: {player.maxbeast_cooldown // 60}s")


def draw_cooldowns2(player, x, y):
    offset = 0

    def write(text):
        nonlocal offset
        draw_text1(text, x, y + offset)
        offset += 20

    if player.skill1_cd > 0:
        write(f"Num4: {player.skill1_cd // 60}s")
    if player.skill2_cd > 0:
        write(f"Num5: {player.skill2_cd // 60}s")
    if player.skill3_cd > 0:
        write(f"UP: {player.skill3_cd // 60}s")
    if player.skill4_cd > 0:
        write(f"Num6: {player.skill4_cd // 60}s")
    if player.skill5_cd > 0:
        write(f"Num8: {player.skill5_cd // 60}s")
    if player.skill6_cd > 0:
        write(f"Num9: {player.skill6_cd // 60}s")

    if player.name == 'vegeta' and player.khi7_cooldown > 0:
        write(f"OOZARU: {player.khi7_cooldown // 60}s")
    if player.name == 'goku' and player.ui_cooldown > 0:
        write(f"GOKU UI: {player.ui_cooldown // 60}s")
    if player.name == 'piccolo' and player.pclo_cooldown > 0:
        write(f"NAMEK: {player.pclo_cooldown // 60}s")
    if player.name == 'broly' and player.ssj4_cd > 0:
        write(f"SSJ4: {player.ssj4_cd // 60}s")
    if player.name == 'gohan':
        if player.beast_cooldown > 0:
            write(f"Beast: {player.beast_cooldown // 60}s")
        if player.maxbeast_cooldown > 0:
            write(f"MAX Beast: {player.maxbeast_cooldown // 60}s")


def draw_hp_bar(player, x, y, reverse=False):
    max_hp = characters[player.name]['health']
    hp_ratio = max(player.health, 0) / max_hp  # không cho âm
    pygame.draw.rect(screen, (0, 0, 0), (x - 2, y - 2, 204, 24), 2)  # Viền
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 200, 20))  # Nền đỏ

    if reverse:
        # Máu xanh giảm từ phải sang trái
        bar_width = int(200 * hp_ratio)
        pygame.draw.rect(screen, (0, 255, 0), (x + 200 - bar_width, y, bar_width, 20))
    else:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, int(200 * hp_ratio), 20))
def draw_character_options():
    x = 60
    for name, data in characters.items():
        if name!='goku_modular':
            screen.blit(data['right'], (x, 250))
            draw_text(name.upper(), x, 220)
            x += 120
        else:
            screen.blit(data['dau_dung'],(x+30,260))
            screen.blit(data['than_dung'],(x+34,283))
            screen.blit(data['chan_dung'],(x+36,293))
            draw_text('Goku Kid'.upper(), x, 220)
def handle_melee_attack(attacker, defender):
    if abs(attacker.x - defender.x) < 70 and abs(attacker.y - defender.y) < 50:
        if defender.ui:
            if random.random() < 1.0:  # 10% dính đòn
                return  # né được, bỏ qua

        # Tính sát thương cơ bản
        dmg = attacker.damage + (5 if attacker.damage_buff else 0)
        # Gohan Beast - giảm 20% sát thương
        if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
            dmg = int(dmg * 0.8)
        # Gohan Beast Max- giảm 30% sát thương
        if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'max':
            dmg = int(dmg * 0.7)
        original_dmg = dmg
        if attacker.name == 'gohan' and attacker.next_attack_2x: 
            dmg *= 2
            attacker.next_attack_2x = False
        if attacker.ssj1_modular:
            dmg += 10
        # Goku Kaioken
        if attacker.kaioken and attacker.name in ['goku', 'goku_modular']:
            if not attacker.ui:
                attacker.health -= 5
            dmg += 12

        # Piccolo clone hỗ trợ dame
        if attacker.name == 'piccolo' and attacker.clone_active:
            dmg += random.randint(3, 6)
        # Broly LSSJ tăng dame
        if attacker.name == 'broly' and attacker.lssj_active:
            if attacker.lssj_bonus < 15:
                attacker.lssj_bonus += random.randint(1, 2)
            dmg += attacker.lssj_bonus
        if defender.shield_active:
            dmg = 0
        # Nếu mục tiêu đang đỡ
        if defender.defending:
            # Vegeta bất tử
            if defender.name == 'vegeta' and defender.vegeta_resurrect and defender.vegeta_invincible_timer > 0:
                dmg = 0
            # Gohan Beast - miễn sát thương nếu đang có khiên
            if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal' and defender.shield_active:
                dmg = 0
            if defender.name == 'piccolo' and defender.shield_active and defender.shield_immune_timer > 0:
                dmg = 0
            else:
                dmg //= 2
            if defender.name == 'broly' and defender.lssj_active:
                dmg = int(dmg * 0.75)  # Giảm 25% dame khi LSSJ
            defender.health -= dmg
            # Ghi lại sát thương nhận nếu Gohan đang ở trạng thái phản damage
            if defender.name == 'gohan' and defender.final_resolve_active:
                defender.resolve_damage_taken += dmg

            # Nếu defender là Broly và đang LSSJ → cũng cộng bonus dame
            if defender.name == 'broly' and defender.lssj_active:
                if defender.lssj_bonus < 15:
                    defender.lssj_bonus += random.randint(1, 2)

            # Broly LSSJ tăng dame
            if attacker.name == 'broly' and attacker.berserker_active:
                defender.ki = max(defender.ki -0.5, 0)
                if random.random() < 0.099:
                    defender.stun_timer = 60  
                    defender.is_stunned = True

            defender.increase_ki(5)
            defender.hit_recently += 1
            # Gohan Beast – phản 50% damage nếu có khiên
            if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
                attacker.health -= dmg // 2

            # Piccolo phản damage nếu có khiên
            if defender.name == 'piccolo' and defender.shield_active:
                if defender.shield_immune_timer <= 0:
                    attacker.health -= dmg // 2
                    attacker.increase_ki(5)

        else:
            # Không đỡ
            if defender.name == 'vegeta' and defender.vegeta_resurrect and defender.vegeta_invincible_timer > 0:
                dmg = 0
            # Gohan Beast - miễn sát thương nếu đang có khiên
            if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal' and defender.shield_active:
                dmg = 0
            if defender.name == 'piccolo' and defender.shield_active and defender.shield_immune_timer > 0:
                dmg = 0
            if defender.name == 'broly' and defender.lssj_active:
                dmg = int(dmg * 0.75)  # Giảm 25% dame khi LSSJ
            defender.health -= dmg
            if defender.name == 'gohan' and defender.final_resolve_active:
                defender.resolve_damage_taken += dmg

            # Nếu defender là Broly và đang LSSJ → cũng cộng bonus dame
            if defender.name == 'broly' and defender.lssj_active:
                if defender.lssj_bonus < 15:
                    defender.lssj_bonus += random.randint(1, 2)

            # Broly LSSJ tăng dame
            if attacker.name == 'broly' and attacker.berserker_active:
                defender.ki = max(defender.ki - 0.5, 0)
                if random.random() < 0.099:
                    defender.stun_timer = 60  # 1s
                    defender.is_stunned = True
            defender.increase_ki(5)
            defender.hit_recently += 1

            # Piccolo phản damage nếu có khiên
            if defender.name == 'piccolo' and defender.shield_active:
                if defender.shield_immune_timer <= 0:
                    attacker.health -= dmg // 2
                    attacker.increase_ki(5)
            # Gohan Beast – phản 50% damage nếu có khiên
            if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
                attacker.health -= dmg // 2
        # Vegeta hút máu
        attacker.vegeta_lifesteal_heal(original_dmg)

        # Cooldown và tăng KI cho attacker
        attacker.attack_cd = 20
        attacker.increase_ki(10)
def handle_projectile_hit(attacker, defender, bullet, projectile_type="normal"):
    if not bullet.active or abs(bullet.x - defender.x) > 50 or abs(bullet.y - defender.y) > 50:
        return
    
    dmg = attacker.damage + (5 if attacker.damage_buff else 0)
    original_dmg = dmg
    # Gohan Beast - giảm 20% sát thương
    if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
        dmg = int(dmg * 0.8)
    # Gohan Beast Max- giảm 30% sát thương
    if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'max':
        dmg = int(dmg * 0.7)
    if attacker.name == 'gohan' and attacker.next_attack_2x: 
        dmg *= 2
        attacker.next_attack_2x = False
    if attacker.ssj1_modular:
        dmg += 10
    if attacker.name == 'broly':
        dmg = int(dmg * 0.5)  # giảm còn 50%
    if attacker.kaioken and attacker.name in ['goku', 'goku_modular']:
        if not attacker.ui:
            attacker.health -= 5
        dmg += 12

    if attacker.name == 'piccolo' and attacker.clone_active:
        dmg += random.randint(3, 6)

    if defender.ui:
        if random.random() < 1.0:  # Goku UI né
            bullet.active = False
            return
    if defender.shield_active:
        dmg = 0
    if defender.defending:
        if defender.name == 'vegeta' and defender.vegeta_resurrect and defender.vegeta_invincible_timer > 0:
            dmg = 0
        else:
            dmg //= 2
            if defender.name == 'piccolo' and defender.shield_active and defender.shield_immune_timer > 0:
                dmg = 0
            # Gohan Beast - miễn sát thương nếu đang có khiên
            if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal' and defender.shield_active:
                dmg = 0
        if defender.name == 'broly' and defender.lssj_active:
            dmg = int(dmg * 0.75)  # Giảm 25% dame khi LSSJ
        defender.health -= dmg
        if defender.name == 'gohan' and defender.final_resolve_active:
            defender.resolve_damage_taken += dmg

        # Nếu là Gohan, ghi nhận thời điểm skill1 trúng và tăng KI
        if attacker.name == 'gohan':
            attacker.last_skill1_hit_time = time.time()
        # Nếu defender là Broly và đang LSSJ → cũng cộng bonus dame
        if defender.name == 'broly' and defender.lssj_active:
            if defender.lssj_bonus < 15:
                defender.lssj_bonus += random.randint(1, 2)

        # Broly LSSJ tăng dame
        if attacker.name == 'broly' and attacker.berserker_active:
            defender.ki = max(defender.ki - 0.5, 0)
            if random.random() < 0.099:
                defender.stun_timer = 60  
                defender.is_stunned = True
        if attacker.name == 'broly':
            defender.increase_ki(2)  # hoặc 3 tùy bạn cân bằng
        else:
            defender.increase_ki(5)

        defender.hit_recently += 1
        if defender.name == 'piccolo' and defender.shield_active and defender.shield_immune_timer <= 0:
            attacker.health -= dmg // 2
            if attacker.name == 'broly':
                attacker.increase_ki(2)
            else:
                attacker.increase_ki(5)
        # Gohan Beast – phản 50% damage nếu có khiên
        if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
            attacker.health -= dmg // 2
    else:
        if defender.name == 'vegeta' and defender.vegeta_resurrect and defender.vegeta_invincible_timer > 0:
            dmg = 0
        if defender.name == 'piccolo' and defender.shield_active and defender.shield_immune_timer > 0:
            dmg = 0
        if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal' and defender.shield_active:
            dmg = 0
        if defender.name == 'broly' and defender.lssj_active:
            dmg = int(dmg * 0.75)  # Giảm 25% dame khi LSSJ
        defender.health -= dmg
        if defender.name == 'gohan' and defender.final_resolve_active:
            defender.resolve_damage_taken += dmg

        # Nếu là Gohan, ghi nhận thời điểm skill1 trúng và tăng KI
        if attacker.name == 'gohan':
            attacker.last_skill1_hit_time = time.time()
        # Nếu defender là Broly và đang LSSJ → cũng cộng bonus dame
        if defender.name == 'broly' and defender.lssj_active:
            if defender.lssj_bonus < 15:
                defender.lssj_bonus += random.randint(1, 2)

        # Broly LSSJ tăng dame
        if attacker.name == 'broly' and attacker.berserker_active:
            defender.ki = max(defender.ki - 0.5, 0)
            if random.random() < 0.099:
                defender.stun_timer = 60  # 0.1s
                defender.is_stunned = True
        if attacker.name == 'broly':
            defender.increase_ki(2)  # hoặc 3 tùy bạn cân bằng
        else:
            defender.increase_ki(5)

        defender.hit_recently += 1
        if defender.name == 'piccolo' and defender.shield_active and defender.shield_immune_timer <= 0:
            attacker.health -= dmg // 2
            if attacker.name == 'broly':
                attacker.increase_ki(2)
            else:
                attacker.increase_ki(5)
        # Gohan Beast – phản 50% damage nếu có khiên
        if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
            attacker.health -= dmg // 2

    attacker.vegeta_lifesteal_heal(original_dmg)
    bullet.active = False
def handle_beam_hit(attacker, defender, beam):
    if defender.ui:
        if random.random() < 1.0:  # Goku UI né
            beam.has_hit = True
            return
    if not beam.active or beam.has_hit:
        return

    if not beam.get_rect().colliderect(pygame.Rect(defender.x, defender.y, defender.width, defender.height)):
        return

    dmg = beam.damage
    # Gohan Beast - giảm 20% sát thương
    if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
        dmg = int(dmg * 0.8)
    # Gohan Beast Max- giảm 30% sát thương
    if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'max':
        dmg = int(dmg * 0.7)
    original_dmg = dmg
    if attacker.name == 'gohan' and attacker.next_attack_2x: 
        dmg +=15
        attacker.next_attack_2x = False

    if attacker.kaioken and attacker.name in ['goku', 'goku_modular']:
        if not attacker.ui:
            attacker.health -= 5
        dmg += 12

    if defender.name == 'vegeta' and defender.vegeta_resurrect and defender.vegeta_invincible_timer > 0:
        dmg = 0
    if defender.shield_active:
        dmg = 0
    if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal' and defender.shield_active:
        dmg = 0
    if defender.name == 'piccolo' and defender.shield_active:
        if defender.shield_immune_timer > 0:
            dmg = 0
        else:
            attacker.health -= dmg // 2
            attacker.increase_ki(5)
    # Gohan Beast – phản 50% damage nếu có khiên
        if defender.name == 'gohan' and defender.beast and defender.beast_mode == 'normal':
            attacker.health -= dmg // 2

    defender.health -= dmg
    # 🎯 Xử lý hiệu ứng đặc biệt từ beam Gohan (nếu có)
    if hasattr(beam, 'effect'):
        effect = beam.effect
        if effect == 'slow':
            defender.slow_timer = 120  # làm chậm 2 giây
        elif effect == 'stun_near' and abs(attacker.x - defender.x) < 80:
            defender.is_stunned = True
            defender.stun_timer = 60
        elif effect == 'oneshot' and defender.health < 0.2 * characters[defender.name]['health']:
            defender.health = 0  # kết liễu nếu máu thấp
    # Nếu defender là Broly và đang LSSJ → cũng cộng bonus dame
    if defender.name == 'broly' and defender.lssj_active:
        if defender.lssj_bonus < 15:
            defender.lssj_bonus += random.randint(1, 2)

    # Broly LSSJ tăng dame
    if attacker.name == 'broly' and attacker.berserker_active:
        defender.ki = max(defender.ki - 0.5, 0)
        if random.random() < 0.099:
            defender.stun_timer = 60  # 0.1s
            defender.is_stunned = True
    defender.increase_ki(5)
    defender.hit_recently += 1

    attacker.vegeta_lifesteal_heal(original_dmg)
    beam.has_hit = True


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    if white_flash_timer > 0:
        white_flash_timer -= 1
        flash_surface = pygame.Surface((WIDTH, HEIGHT))
        flash_surface.set_alpha(120)  # Độ sáng (0–255)
        flash_surface.fill((255, 255, 255))  # Màu trắng
        screen.blit(flash_surface, (0, 0))
    for flash in ultimate_flashes:
        flash.draw(screen)
    ultimate_flashes = [f for f in ultimate_flashes if f.timer > 0]
    if show_character_info:
        draw_character_info()
    elif show_instructions:
        draw_instructions()
    elif selecting:
        draw_text("Player 1 chon nhan vat (1-Goku, 2-Vegeta, 3-Piccolo, 4-Broly,5-Gohan,6-Kid Goku):", 50, 20)
        if player1_choice:
            draw_text("Player 2 chon nhan vat (1-Goku, 2-Vegeta, 3-Piccolo, 4-Broly,5-Gohan,6-Kid Goku):", 50, 60)
        draw_character_options()
        draw_text("Nhan C va chon nhan vat de choi voi may", 50, 100)
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t] and player1.skill6_cd == 0 and player1.ki >= 50 and not player1.t_transforming:
            player1.use_ki(50)
            player1.t_transforming = True
            player1.t_transform_timer = 60  # Nhấp nháy 1 giây
        if keys[pygame.K_KP9] and player2.skill6_cd == 0 and player2.ki >= 50 and not player2.t_transforming:
            player2.use_ki(50)
            player2.t_transforming = True
            player2.t_transform_timer = 60

        # Chiêu ultimate dùng phím H
        if keys[pygame.K_h] and player1.ki >= 60 and player1.skill5_cd == 0:
            player1.charging_ultimate = True
            player1.ultimate_timer = 20  # 1 giây charge

        if keys[pygame.K_KP8] and player2.ki >= 60 and player2.skill5_cd == 0:
            player2.charging_ultimate = True
            player2.ultimate_timer = 20
        # Biến hình cho player1
        if keys[pygame.K_o]:
            if player1.name == 'vegeta':
                player1.transform_ssj()
            elif player1.name == 'goku':
                player1.transform_ui()
            elif player1.name == 'piccolo': 
                player1.transform_pclo()
            elif player1.name == 'broly' and player1.can_use_ssj4 and not player1.ssj4_active:
                player1.transform_ssj4()
            elif player1.name == 'gohan':
                player1.transform_beast_upgrade()
            elif player1.name == 'goku_modular':
                player1.transform_ssj3()

        # Biến hình cho player2
        if keys[pygame.K_KP7]:
            if player2.name == 'vegeta':
                player2.transform_ssj()
            elif player2.name == 'goku':
                player2.transform_ui()
            elif player2.name == 'piccolo':
                player2.transform_pclo()
            elif player2.name == 'broly' and player2.can_use_ssj4 and not player2.ssj4_active:
                player2.transform_ssj4()
            elif player2.name == 'gohan':
                player2.transform_beast_upgrade()
            elif player2.name == 'goku_modular':
                player2.transform_ssj3()
        # Tick cooldown cho cả hai
        player1.cooldown_tick()
        player2.cooldown_tick()
        player1.update_state()
        player2.update_state()
        # --- Kiểm tra va chạm quả cầu SSJ3 Skill2 ---
        for ball in player1.ki_balls:
            ball.move()
            if ball.active:
                ball.draw(screen)
            if ball.active and ball.get_rect().colliderect(pygame.Rect(player2.x, player2.y, player2.width, player2.height)):
                ball.active = False
                damage = 100
                player2.health -= damage
                player2.hit_recently = 10
                white_flash_timer = 10
                nemgenki_sound.stop()
                genki_sound.play()

        player1.ki_balls = [b for b in player1.ki_balls if b.active]
        # --- Kiểm tra va chạm quả cầu SSJ3 Skill2 của player2 ---
        for ball in player2.ki_balls:
            ball.move()
            if ball.active:
                ball.draw(screen)
            if ball.active and ball.get_rect().colliderect(pygame.Rect(player1.x, player1.y, player1.width, player1.height)):
                ball.active = False
                damage = 100
                player1.health -= damage
                player1.hit_recently = 10
                white_flash_timer = 10
                nemgenki_sound.stop()
                genki_sound.play()

        # Xóa cầu không còn hoạt động
        player2.ki_balls = [b for b in player2.ki_balls if b.active]
        # Broly - Rage Pulse (mỗi 2 giây gây dame nếu ở gần)
        for attacker, target in [(player1, player2), (player2, player1)]:
            if attacker.name == 'broly' and attacker.ssj4_active:
                if abs(attacker.x - target.x) < 100 and abs(attacker.y - target.y) < 50:
                    if attacker.rage_timer == 0:
                        dmg = 5

                        # ❌ Né nếu Goku đang ở trạng thái UI (90% né)
                        if target.ui and random.random() < 1.0:
                            continue  # Né được đòn này

                        # ❌ Miễn dame nếu Vegeta đang bất tử (T)
                        if target.name == 'vegeta' and target.vegeta_resurrect and target.vegeta_invincible_timer > 0:
                            continue  # Không nhận sát thương

                        # ❌ Miễn dame nếu Piccolo có khiên và đang trong 2s đầu
                        if target.name == 'piccolo' and target.shield_active and target.shield_immune_timer > 0:
                            continue  # Không nhận sát thương

                        # ✅ Giảm sát thương nếu đang phòng thủ
                        if target.defending:
                            dmg //= 2

                        target.health -= dmg


        # Di chuyển
        player1.move(keys)
        if playing_with_ai:
            handle_ai(player1, player2)
        else:
            player2.move(keys)
        player1.apply_gravity()
        player2.apply_gravity()

        # Player 1
        if not player1.is_stunned and not player1.transforming and not player1.ssj3_skill2_active:
            # Skill 1
            if (keys[pygame.K_s] or player1.ssj1_healing) and not (keys[pygame.K_u] or keys[pygame.K_i] or keys[pygame.K_j]):
                player1.defending = True
            else:
                player1.defending = False

            if keys[pygame.K_l] and player1.dash_timer == 0:
                sound_dash.play()
                dash_speed = 100
                direction = 1 if player1.facing == 'right' else -1
                player1.x += dash_speed * direction
                player1.dash_timer = 120  # 1 giây cooldown (60 frame nếu FPS=60)
                player1.x = max(0, min(player1.x, WIDTH - player1.width))
            
            if keys[player1.controls['skill1']] and player1.skill1_cd == 0:
                direction = 1 if player1.facing == 'right' else -1
                if player1.name == 'goku_modular':
                    if player1.ssj1_modular or player1.ssj3_modular:
                        color = (255, 255, 0)  # vàng giống Gohan SSJ1
                    else:
                        color = player1.char['skill1_color']
                    bullet = Projectile1(player1.x + 30, player1.y, direction, color)
                    player1.projectiles1.append(bullet)
                    player1.just_shot_skill1 = 10
                    player1.skill1_cd = 120  
                    kiblast_sound.play()
                    player1.increase_ki(10)
                
                elif player1.name == 'gohan':
                    x = player1.x + 30
                    y = player1.y

                    if player1.beast:
                        if player1.beast_mode == 'normal':
                            bullet1 = Projectile1(x, y, direction, (150, 0, 255))
                            bullet2 = Projectile1(x + 20, y, direction, (150, 0, 255))
                            player1.projectiles1.extend([bullet1, bullet2])
                        else:
                            for i in range(3):
                                bullet = Projectile1(x + i * 20, y, direction, (255, 50, 50))
                                player1.projectiles1.append(bullet)
                    elif player1.ssj1:
                        bullet = Projectile1(x, y, direction, (255, 255, 0))
                        bullet.speed = 12 * direction

                        player1.projectiles1.append(bullet)
                    else:
                        bullet = Projectile1(x, y, direction, (255, 255, 100))  # ⚠️ CHỈ 1 VIÊN
                        player1.projectiles1.append(bullet)

                    player1.skill1_cd = 120
                    player1.increase_ki(10)

                elif player1.name == 'broly':
                    bullet = Projectile1(player1.x + 30, player1.y, direction, player1.char['skill1_color'])
                    player1.projectiles1.append(bullet)
                    player1.broly_quick_shot_count += 1
                    if player1.broly_quick_shot_count < 3:
                        player1.skill1_cd = 6
                        player1.increase_ki(2.5)
                    else:
                        player1.skill1_cd = 180
                        player1.broly_quick_shot_count = 0
                        player1.increase_ki(6)
                else:
                    bullet = Projectile1(player1.x + 30, player1.y, direction, player1.char['skill1_color'])
                    player1.projectiles1.append(bullet)
                    player1.skill1_cd = 120
                    player1.increase_ki(10)


            # Skill 3
            if keys[player1.controls['skill3']] and player1.skill3_cd == 0:
                direction = 1 if player1.facing == 'right' else -1
                bullet = Projectile(player1.x + 30, player1.y, direction, player1.char['skill1_color'])
                player1.projectiles.append(bullet)

                if player1.name == 'broly':
                    player1.broly_quick_shot_count += 1
                    if player1.broly_quick_shot_count < 3:
                        player1.skill3_cd = 6
                        player1.increase_ki(2.5)
                    else:
                        player1.skill3_cd = 180
                        player1.broly_quick_shot_count = 0
                        player1.increase_ki(6)
                else:
                    player1.skill3_cd = 120
                    player1.increase_ki(10)

            if keys[player1.controls['skill4']] and player1.skill4_cd == 0:
                direction = 1 if player1.facing == 'right' else -1
                bullet = Projectile2(player1.x + 30, player1.y, direction, player1.char['skill1_color'])
                player1.projectiles2.append(bullet)

                if player1.name == 'broly':
                    player1.broly_quick_shot_count += 1
                    if player1.broly_quick_shot_count < 3:
                        player1.skill4_cd = 6
                        player1.increase_ki(2.5)
                    else:
                        player1.skill4_cd = 180
                        player1.broly_quick_shot_count = 0
                        player1.increase_ki(6)
                else:
                    player1.skill4_cd = 120
                    player1.increase_ki(10)

            # Skill 2
            KI_COST_SKILL2=40
            if keys[player1.controls['skill2']] and player1.skill2_cd == 0:
                if player1.name == 'gohan':
                    now = time.time()
                    if player1.beast:
                        if player1.beast_mode == 'normal':
                            # Beast Barrier
                            player1.shield_active = True
                            player1.shield_timer = 150
                            player1.skill2_cd = 360
                        else:
                            # Max Beast - Final Resolve
                            player1.final_resolve_active = True
                            player1.resolve_damage_taken = 0
                            player1.final_resolve_timer = 180
                            player1.skill2_cd = 360
                    else:
                        if now - player1.last_skill1_hit_time < 1.5:#tự đông kích hoạt khi bấm I sau khi U trúng địch
                            # Combo đặc biệt
                            player1.damage_buff = True
                            player1.damage_buff_timer = 60
                            player1.skill2_cd = 360
                        elif player1.ki >= KI_COST_SKILL2:
                            if player1.use_ki(KI_COST_SKILL2):
                                player1.damage_buff = True
                                player1.damage_buff_timer = 180
                                player1.ki_regen_timer = 180
                                if player1.ssj1:
                                    player1.damage_buff_timer = 300
                                    player1.next_attack_2x = True  # buff đòn kế tiếp gấp đôi
                                player1.skill2_cd = 360
                elif player1.name == "goku_modular":
                    if player1.ssj3_modular:
                        if player1.ki >= KI_COST_SKILL2:
                            if player1.use_ki(KI_COST_SKILL2):
                                player1.skill2_cd = 480
                                player1.ssj3_skill2_active = True
                                player1.ssj3_skill2_phase = 0
                                player1.ssj3_skill2_timer = 0
                                
                    elif player1.ssj1_modular:
                        if player1.ki >= KI_COST_SKILL2:
                            if player1.use_ki(KI_COST_SKILL2):
                                player1.ssj1_healing = True
                                player1.ssj1_heal_timer = 300  # 5 giây (60fps)
                                player1.total_healed = 0
                                player1.heal_tick_counter = 0
                                player1.skill2_cd = 360
                                kaioken_sound.play()
                    else:
                        if player1.ki >= KI_COST_SKILL2:
                            player1.use_ki(KI_COST_SKILL2)
                            if player1.skill2_type == 'kaioken':
                                player1.kaioken = True
                                player1.kaioken_timer = 360
                                kaioken_sound.play()
                else:
                    if player1.ki >= KI_COST_SKILL2:
                        player1.use_ki(KI_COST_SKILL2)
                        if player1.skill2_type == 'buff_damage':
                            player1.damage_buff = True
                            player1.damage_buff_timer = 180
                        elif player1.skill2_type == 'heal':
                            player1.health = min(player1.health + 90, characters[player1.name]['health'])
                        elif player1.skill2_type == 'stun' and abs(player1.x - player2.x) < 100:
                            player2.is_stunned = True
                            player2.stun_timer = 60
                        elif player1.skill2_type == 'berserker':
                            player1.berserker_active = True
                            player1.berserker_timer = 240

                        player1.skill2_cd = 360


            # Đánh thường
            if keys[player1.controls['attack']] and player1.attack_cd == 0:
                handle_melee_attack(player1, player2)
            

        # Player 2
        if not playing_with_ai and not player2.is_stunned and not player2.transforming and not player2.ssj3_skill2_active:
            # Player 2
            if keys[pygame.K_DOWN] and not (keys[pygame.K_4] or keys[pygame.K_5] or keys[pygame.K_1]):
                player2.defending = True
            else:
                player2.defending = False
            if keys[pygame.K_KP0] and player2.dash_timer == 0:
                dash_speed = 100
                direction = 1 if player2.facing == 'right' else -1
                player2.x += dash_speed * direction
                player2.dash_timer = 120  # 1 giây cooldown (60 frame nếu FPS=60)
                player2.x = max(0, min(player2.x, WIDTH - player2.width))
            if keys[player2.controls['skill1']] and player2.skill1_cd == 0:
                direction = 1 if player2.facing == 'right' else -1
                if player2.name == 'goku_modular':
                    if player2.ssj1_modular:
                        color = (255, 255, 0)  # vàng giống Gohan SSJ1
                    else:
                        color = player2.char['skill1_color']
                    bullet = Projectile1(player2.x + 30, player2.y, direction, color)
                    player2.projectiles1.append(bullet)
                    player2.just_shot_skill1 = 10
                elif player2.name != 'gohan':
                    bullet = Projectile1(player2.x + 30, player2.y, direction, player2.char['skill1_color'])
                    player2.projectiles1.append(bullet)
                    player2.just_shot_skill1 = 10  # hiện trạng thái bắn trong 10 frame
                elif player2.name == 'gohan':
                    x = player2.x + 30
                    y = player2.y

                    if player2.beast:
                        if player2.beast_mode == 'normal':
                            bullet1 = Projectile1(x, y, direction, (150, 0, 255))
                            bullet2 = Projectile1(x + 20, y , direction, (150, 0, 255))
                            player2.projectiles1.extend([bullet1, bullet2])
                        else:
                            for i in range(3):
                                bullet = Projectile1(x + i * 20, y, direction, (255, 50, 50))
                                player2.projectiles1.append(bullet)
                    elif player2.ssj1:
                        bullet = Projectile1(x, y, direction, (255, 255, 0))
                        bullet.speed = 10
                        player2.projectiles1.append(bullet)
                    else:
                        bullet = Projectile1(x, y, direction, (255, 255, 100))  # CHỈ 1 VIÊN
                        player2.projectiles1.append(bullet)

                    player2.skill1_cd = 120
                    player2.increase_ki(10)

                elif player2.name == 'broly':
                    player2.broly_quick_shot_count += 1
                    if player2.broly_quick_shot_count < 3:
                        player2.skill1_cd = 6
                        player2.increase_ki(2.5)
                    else:
                        player2.skill1_cd = 180
                        player2.broly_quick_shot_count = 0
                        player2.increase_ki(6)
                else:
                    player2.skill1_cd = 120
                    player2.increase_ki(10)


            if keys[player2.controls['skill3']] and player2.skill3_cd == 0:
                direction = 1 if player2.facing == 'right' else -1
                bullet = Projectile(player2.x + 30, player2.y, direction, player2.char['skill1_color'])
                player2.projectiles.append(bullet)

                if player2.name == 'broly':
                    player2.broly_quick_shot_count += 1
                    if player2.broly_quick_shot_count < 3:
                        player2.skill3_cd = 6
                        player2.increase_ki(2.5)
                    else:
                        player2.skill3_cd = 180
                        player2.broly_quick_shot_count = 0
                        player2.increase_ki(6)
                else:
                    player2.skill3_cd = 120
                    player2.increase_ki(10)

            if keys[player2.controls['skill4']] and player2.skill4_cd == 0:
                direction = 1 if player2.facing == 'right' else -1
                bullet = Projectile2(player2.x + 30, player2.y, direction, player2.char['skill1_color'])
                player2.projectiles2.append(bullet)

                if player2.name == 'broly':
                    player2.broly_quick_shot_count += 1
                    if player2.broly_quick_shot_count < 3:
                        player2.skill4_cd = 6
                        player2.increase_ki(2.5)
                    else:
                        player2.skill4_cd = 180
                        player2.broly_quick_shot_count = 0
                        player2.increase_ki(6)
                else:
                    player2.skill4_cd = 120
                    player2.increase_ki(10)
            KI_COST_SKILL2=40
            if keys[player2.controls['skill2']] and player2.skill2_cd == 0:
                if player2.name == 'gohan':
                    now = time.time()
                    if player2.beast:
                        if player2.beast_mode == 'normal':
                            # Beast Barrier
                            player2.shield_active = True
                            player2.shield_timer = 150
                            player2.skill2_cd = 360
                        else:
                            # Max Beast - Final Resolve
                            player2.final_resolve_active = True
                            player2.resolve_damage_taken = 0
                            player2.final_resolve_timer = 180
                            player2.skill2_cd = 360
                    else:
                        if now - player2.last_skill1_hit_time < 1.5:
                            # Combo đặc biệt
                            player2.damage_buff = True
                            player2.damage_buff_timer = 60
                            player2.skill2_cd = 360
                        elif player2.ki >= KI_COST_SKILL2:
                            if player2.use_ki(KI_COST_SKILL2):
                                player2.damage_buff = True
                                player2.damage_buff_timer = 180
                                player2.ki_regen_timer = 180  # 🔥 thêm dòng này để hồi KI mỗi giây
                                if player2.ssj1:
                                    player2.damage_buff_timer = 300  # tăng hiệu lực khi ở dạng SSJ1
                                    player2.next_attack_2x = True  # buff đòn kế tiếp gấp đôi
                                player2.skill2_cd = 360
                elif player2.name == "goku_modular":
                    if player2.ssj3_modular:
                        if player2.ki >= KI_COST_SKILL2:
                            if player2.use_ki(KI_COST_SKILL2):
                                player2.skill2_cd = 480
                                player2.ssj3_skill2_active = True
                                player2.ssj3_skill2_phase = 0
                                player2.ssj3_skill2_timer = 0
                                
                    elif player2.ssj1_modular:
                        if player2.ki >= KI_COST_SKILL2:
                            if player2.use_ki(KI_COST_SKILL2):
                                player2.ssj1_healing = True
                                player2.ssj1_heal_timer = 300  # 5 giây (60fps)
                                player2.total_healed = 0
                                player2.heal_tick_counter = 0
                                player2.skill2_cd = 360
                                kaioken_sound.play()
                    else:
                        if player2.ki >= KI_COST_SKILL2:
                            player2.use_ki(KI_COST_SKILL2)
                            if player2.skill2_type == 'kaioken':
                                player2.kaioken = True
                                player2.kaioken_timer = 360
                                kaioken_sound.play()
                else:
                    if player2.ki >= KI_COST_SKILL2:
                        player2.use_ki(KI_COST_SKILL2)
                        if player2.skill2_type == 'buff_damage':
                            player2.damage_buff = True
                            player2.damage_buff_timer = 180
                        elif player2.skill2_type == 'heal':
                            player2.health = min(player2.health + 90, characters[player2.name]['health'])
                        elif player2.skill2_type == 'stun' and abs(player2.x - player1.x) < 100:
                            player1.is_stunned = True
                            player1.stun_timer = 60
                        elif player2.skill2_type == 'berserker':
                            player2.berserker_active = True
                            player2.berserker_timer = 240

                        player2.skill2_cd = 360


            if keys[player2.controls['attack']] and player2.attack_cd == 0:
                handle_melee_attack(player2, player1)
        # Vẽ người chơi
        player1.draw()
        player2.draw()
        for beam in player1.big_beams:
            beam.update()
        for beam in player2.big_beams:
            beam.update()
        # Di chuyển và vẽ đạn Player 1
        for bullet in player1.projectiles:
            bullet.move()
            bullet.draw()
        for bullet in player1.projectiles1:
            bullet.move()
            bullet.draw()
        for bullet in player1.projectiles2:
            bullet.move()
            bullet.draw()
        # Cập nhật đạn clone Piccolo
        for clone_bullet in player1.clone_projectiles:
            if clone_bullet.active:
                clone_bullet.move()
                clone_bullet.draw()
        player1.clone_projectiles = [b for b in player1.clone_projectiles if b.active]
        player1.draw_ki_bar(screen)  # ✅ Vẽ thanh KI cho player1
        player2.draw_ki_bar(screen)  # ✅ Vẽ thanh KI cho player2
        # Di chuyển và vẽ đạn Player 2
        for bullet in player2.projectiles:
            bullet.move()
            bullet.draw()
        for bullet in player2.projectiles1:
            bullet.move()
            bullet.draw()
        for bullet in player2.projectiles2:
            bullet.move()
            bullet.draw()
        # Player 1 bắn đạn trúng player 2
        for bullet in player1.projectiles + player1.projectiles1 + player1.projectiles2:
            handle_projectile_hit(player1, player2, bullet)

        # Player 2 bắn đạn trúng player 1
        for bullet in player2.projectiles + player2.projectiles1 + player2.projectiles2:
            handle_projectile_hit(player2, player1, bullet)

        # Clone bắn
        for bullet in player1.clone_projectiles:
            handle_projectile_hit(player1, player2, bullet)

        for bullet in player2.clone_projectiles:
            handle_projectile_hit(player2, player1, bullet)

        # Big beam
        for beam in player1.big_beams:
            handle_beam_hit(player1, player2, beam)

        for beam in player2.big_beams:
            handle_beam_hit(player2, player1, beam)


        player1.big_beams = [b for b in player1.big_beams if b.active]
        player2.big_beams = [b for b in player2.big_beams if b.active]
        # Xóa đạn không còn active
        player1.projectiles = [b for b in player1.projectiles if b.active]
        player2.projectiles = [b for b in player2.projectiles if b.active]
        player1.projectiles1 = [b for b in player1.projectiles1 if b.active]
        player2.projectiles1 = [b for b in player2.projectiles1 if b.active]
        player1.projectiles2 = [b for b in player1.projectiles2 if b.active]
        player2.projectiles2 = [b for b in player2.projectiles2 if b.active]

        # Hiển thị máu
        draw_hp_bar(player1, 20, 20)  # Player 1 trái → giữ nguyên
        draw_hp_bar(player2, 580, 20, reverse=True)  # Player 2 phải → vẽ ngược
        # Vẽ cooldown skill của player1 ở góc trái
        draw_cooldowns(player1, 20, 50)
        # Vẽ cooldown skill của player2 ở góc phải
        draw_cooldowns2(player2, 730, 50)
        for p in [player1, player2]:
            if (p.name == 'vegeta' and p.health <= 0 
                and p.skill6_cd == 0 and p.ki >= 50 
                and p.vegeta_resurrect_count < 2):
                
                p.vegeta_resurrect = True
                p.vegeta_invincible_timer = 120
                p.vegeta_lifesteal = 1.0
                p.vegeta_lifesteal_timer = 120
                p.use_ki(50)
                p.skill6_cd = 1200
                p.health = 1
                p.vegeta_resurrect_count += 1

        if not game_over and (player1.health <= 0 or player2.health <= 0):
            winner = "Player 1" if player2.health <= 0 else "Player 2"
            game_over = True

        # Nếu game_over, hiển thị kết quả và chờ phím R
        if game_over:
            draw_text(f"{winner} WINS!", 300, 200)
            draw_text("Nhan R de choi lai", 340, 240)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset trạng thái game
                player1_choice = None
                player2_choice = None
                selecting = True
                show_instructions = True
                game_over = False
                winner = ""
                playing_with_ai = False
                # Reset nhân vật
                player1.reset(100, 250)
                player2.reset(600, 250)

                # Xóa đạn
                player1.projectiles.clear()
                player1.projectiles1.clear()
                player1.projectiles2.clear()
                player2.projectiles.clear()
                player2.projectiles1.clear()
                player2.projectiles2.clear()
                kaioken_sound.stop()
                ssj3_sound.stop()
                ssj1_sound.stop()
                kiblast_sound.stop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if show_character_info:
                    show_character_info = False
                    show_instructions = True
                elif show_instructions:
                    show_instructions = False
                    selecting=True
        if event.type == pygame.KEYDOWN and selecting:
            if event.key == pygame.K_c:
                player1_choice = None
                player2_choice = random.choice(['goku','vegeta','piccolo','broly','gohan','goku_modular'])
                playing_with_ai = True
            if not player1_choice:
                if event.key == pygame.K_1:
                    player1_choice = 'goku'
                elif event.key == pygame.K_2:
                    player1_choice = 'vegeta'
                elif event.key == pygame.K_3:
                    player1_choice = 'piccolo'
                elif event.key == pygame.K_4:
                    player1_choice = 'broly'
                elif event.key == pygame.K_5:
                    player1_choice = 'gohan'
                elif event.key == pygame.K_6:
                    player1_choice = 'goku_modular'
            elif not player2_choice:
                if event.key == pygame.K_1:
                    player2_choice = 'goku'
                elif event.key == pygame.K_2:
                    player2_choice = 'vegeta'
                elif event.key == pygame.K_3:
                    player2_choice = 'piccolo'
                elif event.key == pygame.K_4:
                    player2_choice = 'broly'
                elif event.key == pygame.K_5:
                    player2_choice = 'gohan'
                elif event.key == pygame.K_6:
                    player1_choice = 'goku_modular'
            if player1_choice and player2_choice:
                selecting = False
                player1 = Player(player1_choice, 100, 300, {
                    'left': pygame.K_a,
                    'right': pygame.K_d,
                    'attack': pygame.K_j,
                    'jump': pygame.K_k,
                    'skill1': pygame.K_u,
                    'skill2': pygame.K_i,
                    'skill3':pygame.K_w,
                    'skill4':pygame.K_y
                })
                if not playing_with_ai:
                    player2 = Player(player2_choice, 600, 300, {
                        'left': pygame.K_LEFT,
                        'right': pygame.K_RIGHT,
                        'attack': pygame.K_KP1,
                        'jump': pygame.K_KP2,
                        'skill1': pygame.K_KP4,
                        'skill2': pygame.K_KP5,
                        'skill3': pygame.K_UP,
                        'skill4': pygame.K_KP6,
                    })
                    player2.facing = 'left'

                else:
                    player2 = Player('goku_modular', 600, 300, {})  # AI không dùng controls
                    player2.facing = 'left'


            # Player 2 sẽ được thêm sau ở bước tiếp theo

                # Tiếp tục xây dựng logic gameplay sau khi chọn xong nhân vật

    pygame.display.update()
    clock.tick(60)
pygame.quit()

