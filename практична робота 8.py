import tkinter as tk
from PIL import Image, ImageTk


class StudentForm:

    def __init__(self, root):
        self.root = root
        self.root.title("Анкета студента")
        self.root.geometry("450x550")

        info_text = (
            "ПІБ: Рябов Максим Олексійович\n"
            "Група: Ік-51\n"
            "Спеціальність: Інженерія програмного забезпечення\n"
            "Курс: 3"
        )
        tk.Label(
            root,
            text=info_text,
            font=("Times New Roman", 14),
            justify=tk.LEFT,
            anchor="w",
        ).pack(padx=20, pady=10, fill=tk.X)

        self.img_frame = tk.Frame(root, width=250, height=300, bg="gray")
        self.img_frame.pack(pady=10)
        self.img_frame.pack_propagate(False)

        self.img1 = self.load_image(
            "b5df7b1a1055b68b27c4933630199bd5.jpg", (250, 300)
        )
        self.img2 = self.load_image("images.jpg", (250, 300))

        self.lbl_portrait = tk.Label(self.img_frame, image=self.img1)
        self.lbl_artistic = tk.Label(self.img_frame, image=self.img2)

        self.lbl_artistic.place(x=0, y=0, relwidth=1, relheight=1)
        self.lbl_portrait.place(x=0, y=0, relwidth=1, relheight=1)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="Портретне фото",
            command=self.show_portrait,
            width=15,
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame, text="Художнє фото", command=self.show_artistic, width=15
        ).pack(side=tk.LEFT, padx=5)

    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size)
            return ImageTk.PhotoImage(img)
        except Exception:
            return None

    def show_portrait(self):
        self.lbl_portrait.lift()

    def show_artistic(self):
        self.lbl_artistic.lift()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentForm(root)
    root.mainloop()