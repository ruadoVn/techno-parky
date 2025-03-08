import pygame
import random

def create_park_image(width=1920, height=1080, filename="park_background.png"):
    pygame.init()
    # Tạo một Surface để vẽ
    surface = pygame.Surface((width, height))

    # 1) Tô nền màu xanh lá nhạt
    background_color = (170, 215, 81)  # xanh lá nhạt
    surface.fill(background_color)

    # 2) Vẽ các đoạn đường (màu xám)
    road_color = (200, 200, 200)
    # a) Đường dọc ở giữa
    pygame.draw.rect(surface, road_color, (width * 0.45, 0, width * 0.1, height))
    # b) Đường ngang ở giữa
    pygame.draw.rect(surface, road_color, (0, height * 0.45, width, height * 0.1))

    # 3) Vẽ vòng xuyến (roundabout) ở giữa
    roundabout_color = (200,200,200)  # màu trắng
    pygame.draw.circle(surface, roundabout_color, (width // 2, height // 2), 200)
    
    

    # 4) Vẽ một số cây ngẫu nhiên
    # (nếu muốn tránh vẽ lên đường, bạn có thể kiểm tra toạ độ trước khi vẽ)
    for _ in range(30):
        tree_x = random.randint(0, width)
        tree_y = random.randint(0, height)
        tree_color = (34, 139, 34)  # xanh lá đậm (ForestGreen)
        radius = random.randint(5, 20)
        pygame.draw.circle(surface, tree_color, (tree_x, tree_y), radius)

    # 5) Lưu ảnh ra file PNG
    pygame.image.save(surface, filename)
    print(f"Đã lưu ảnh công viên vào file '{filename}'.")

    pygame.quit()

if __name__ == "__main__":
    create_park_image()
