import cv2
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import ImageTk, Image
from detector import detect_animal
from extractor import extract_features
from myutils import cosine_similarity

class AnimalReIDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Identification by:Collor")
        
        # Define o ícone da janela (para Windows, é necessário um arquivo .ico)
        try:
            self.root.iconbitmap("logo.ico")  # Certifique-se de que "logo.ico" está no diretório
        except Exception as e:
            print("Erro ao carregar o ícone:", e)
        
        # Exibe o logo na GUI (utilizando um arquivo PNG)
        try:
            self.logo_image = ImageTk.PhotoImage(Image.open("logo.png"))
            logo_label = Label(root, image=self.logo_image)
            logo_label.pack()
        except Exception as e:
            print("Erro ao carregar a imagem do logo:", e)
        
        self.label = Label(root, text="Escolha duas imagens para comparar:")
        self.label.pack()

        self.btn1 = Button(root, text="Selecionar Imagem 1", command=self.load_image1)
        self.btn1.pack()

        self.btn2 = Button(root, text="Selecionar Imagem 2", command=self.load_image2)
        self.btn2.pack()

        self.compare_btn = Button(root, text="Comparar", command=self.compare_images)
        self.compare_btn.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

        self.img1_path = None
        self.img2_path = None

    def load_image1(self):
        self.img1_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png")])
        if self.img1_path:
            self.label.config(text=f"Imagem 1 carregada: {self.img1_path}")

    def load_image2(self):
        self.img2_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png")])
        if self.img2_path:
            self.label.config(text=f"Imagem 2 carregada: {self.img2_path}")

    def compare_images(self):
        if not self.img1_path or not self.img2_path:
            messagebox.showerror("Erro", "Por favor selecione as duas imagens.")
            return

        img1 = cv2.imread(self.img1_path)
        img2 = cv2.imread(self.img2_path)

        crop1 = detect_animal(img1)
        crop2 = detect_animal(img2)

        if crop1 is None or crop2 is None:
            self.result_label.config(text="Animal não detectado em uma das imagens.")
            return

        features1 = extract_features(crop1)
        features2 = extract_features(crop2)

        similarity = cosine_similarity(features1, features2)
        resultado = f"Similaridade: {similarity:.4f}\n"

        if similarity > 0.8:
            resultado += "✅ Provavelmente é o mesmo animal!"
        else:
            resultado += "❌ Provavelmente são animais diferentes."

        self.result_label.config(text=resultado)

if __name__ == "__main__":
    root = Tk()
    app = AnimalReIDApp(root)
    root.mainloop()
