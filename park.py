import pygame
import random

# Cấu hình kích thước cửa sổ và lưới
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500  # Kích thước cửa sổ (pixels)
GRID_WIDTH, GRID_HEIGHT = 50, 50        # Số ô theo chiều ngang và dọc của lưới
CELL_SIZE = WINDOW_WIDTH // GRID_WIDTH  # Kích thước 1 ô (pixels)

# Định nghĩa lớp Agent đại diện cho khách tham quan
class Agent:
    def __init__(self, x, y, color=(0, 0, 255)):
        self.x = x  # Vị trí x (theo ô)
        self.y = y  # Vị trí y (theo ô)
        self.color = color

    def move(self):
        # Chọn bước di chuyển ngẫu nhiên theo cả hai hướng x và y
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        # Cập nhật vị trí, đảm bảo không vượt ra ngoài lưới
        self.x = max(0, min(GRID_WIDTH - 1, self.x + dx))
        self.y = max(0, min(GRID_HEIGHT - 1, self.y + dy))

def main():
    # Khởi tạo Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Mô hình công viên bằng Pygame")
    clock = pygame.time.Clock()

    # Tạo danh sách agent với vị trí khởi đầu ngẫu nhiên
    num_agents = 10  # Số lượng khách tham quan
    agents = []
    for _ in range(num_agents):
        start_x = random.randint(0, GRID_WIDTH - 1)
        start_y = random.randint(0, GRID_HEIGHT - 1)
        agents.append(Agent(start_x, start_y))

    running = True
    while running:
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Cập nhật vị trí cho mỗi agent
        for agent in agents:
            agent.move()

        # Vẽ lại nền và lưới (tùy chọn)
        screen.fill((255, 255, 255))  # Nền trắng

        # Vẽ lưới: các đường kẻ chia ô (màu xám nhạt)
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (0, y), (WINDOW_WIDTH, y))

        # Vẽ các agent dưới dạng hình tròn nhỏ trong từng ô
        for agent in agents:
            # Tính vị trí pixel trung tâm của ô
            center_x = agent.x * CELL_SIZE + CELL_SIZE // 2
            center_y = agent.y * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, agent.color, (center_x, center_y), CELL_SIZE // 3)

        pygame.display.flip()
        clock.tick(5)  # 5 khung hình mỗi giây (fps)

    pygame.quit()

if __name__ == "__main__":
    main()
