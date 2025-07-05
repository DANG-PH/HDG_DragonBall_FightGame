<p align="center">
  <img src="images/avt9.webp" width="220" alt="Chiến Binh Rồng Thiêng">
</p>

<h2 align="center">Chiến Binh Rồng Thiêng – Game Đối Kháng DragonBall</h2>

<p align="center">
  Dự án cá nhân mô phỏng game đối kháng 1v1, phát triển bằng <strong>Python (Pygame)</strong> và chạy trực tiếp trên trình duyệt thông qua <strong>Pygbag</strong>.
</p>

---

## 🎮 Giới thiệu

**Chiến Binh Rồng Thiêng** là một web game thể loại đối kháng 1vs1 lấy cảm hứng từ vũ trụ **Dragon Ball**. Game cho phép bạn điều khiển các chiến binh quen thuộc như **Goku, Vegeta, Broly, Gohan, Piccolo,...** để giao tranh theo thời gian thực. Mỗi nhân vật có hệ thống chiêu thức đặc trưng, kỹ năng biến hình, và ultimate riêng biệt.

Game sử dụng **Python + Pygame** để xây dựng logic, đồ họa, âm thanh, sau đó được đóng gói WebAssembly bằng **Pygbag** để chạy trên web mà không cần cài đặt gì thêm.

---

## 🔗 Chơi ngay

👉 **Link chơi web game:**  
🎮 [https://dang-ph.github.io/chienbinhrongthieng](https://dang-ph.github.io/chienbinhrongthieng)

---

## ⚙️ Tính năng nổi bật

- 👥 **Chế độ đối kháng 1vs1**: Chơi với bạn bè hoặc đấu với máy (AI).
- 🧠 **AI linh hoạt**: Né beam, biến hình đúng lúc, hồi máu, stun, phản đòn.
- 🌀 **Biến hình đa dạng**:
  - Goku: Kaioken → SSJ1 → SSJ3
  - Vegeta: Khi1 → khi7
  - Broly: LSSJ → SSJ4
  - Gohan: Beast mode thường → Max Beast
  - Piccolo: Full power → Orange
- ⚡ **Chiêu thức độc quyền**: Ultimate Kamehameha, Masenko, Final Flash, Genki Dama, Beast Stun...
- 🖼️ **Hiệu ứng hình ảnh động**: aura, glow, beam, shield, ki ball,...
- 🔊 **Âm thanh sống động**: Voice, skill sounds, biến hình, ultimate...
- 🌐 **Không cần cài đặt**: Chạy trực tiếp trên trình duyệt (nhờ WebAssembly).

---

## 🕹️ Điều khiển

| Người chơi 1              | Người chơi 2 (AI hoặc Player)   |
|---------------------------|----------------------------------|
| `A / D`: di chuyển        | `← / →`: di chuyển              |
| `W`: nhảy                 | `↑`: nhảy                       |
| `J`: đánh thường          | `Num1`: đánh thường             |
| `K`: Skill 1 (bắn đạn)    | `Num2`: Skill 1                 |
| `L`: Skill 2 (buff/heal)  | `Num3`: Skill 2                 |
| `U`: Biến hình (T)        | `Num4`: Biến hình (T)           |
| `I`: Ultimate (O)         | `Num5`: Ultimate (O)            |

> Game hỗ trợ cả chơi 1 người (đấu AI) hoặc 2 người cùng bàn phím.

---

## 📸 Hình ảnh minh họa

<p align="center">
  <img src="images/screenshot1.png" width="400">
  <img src="images/screenshot2.png" width="400">
</p>

---

## 🧠 Cơ chế AI

AI được lập trình để:
- Né ultimate nếu thấy địch đang sạc.
- Biến hình đúng lúc khi máu thấp hoặc KI đầy.
- Dùng kỹ năng 2 khi bị áp đảo.
- Tự động phòng thủ hoặc dash tránh spam.
- Kết liễu đối thủ bằng Ultimate nếu ở gần.

---

## 🚀 Công nghệ sử dụng

- 🐍 Python
- 🎮 Pygame
- 🧪 Pygbag (biên dịch Pygame thành WebAssembly)
- 🎨 Các trình chỉnh Pixel Art (ảnh nhân vật & hiệu ứng)

---

## 📧 Tác giả

- 👤 **Phạm Hải Đăng**  
- 📚 Sinh viên Học viện Công nghệ Bưu chính Viễn thông (PTIT)  
- 📫 Email: dangph.ptit@gmail.com  
- 🌐 GitHub: [DANG-PH](https://github.com/DANG-PH)

---

## ⭐ Đóng góp

Nếu bạn thấy game thú vị:
- Hãy ⭐ repo để ủng hộ
- Gửi pull request để góp ý hoặc thêm tính năng mới
- Chia sẻ đến bạn bè để cùng chiến đấu!

---

<p align="center">
  💥 Cảm ơn bạn đã trải nghiệm Chiến Binh Rồng Thiêng 💥
</p>

